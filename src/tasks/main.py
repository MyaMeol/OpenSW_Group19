from fastapi import FastAPI, UploadFile, File, Body
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .pdf_analysis import extract_pdf_pages, document_index
from .grammar import correct_grammar
from .smart_pdf import analyze_pdf, generate_report_pdf


app = FastAPI()


class GrammarRequest(BaseModel):
    text: str


@app.post("/pdf/analyze")
async def analyze_pdf_endpoint(file: UploadFile = File(...)):
    pdf_bytes = await file.read()

    pages = extract_pdf_pages(pdf_bytes)
    full_text = "\n".join(pages)

    document_index.build(full_text, source_pdf_name=file.filename)

    summary = full_text[:300] + "..." if len(full_text) > 300 else full_text
    topics = ["mock-topic-1", "mock-topic-2"]
    keywords = ["mock1", "mock2", "mock3"]

    return {
        "file_name": file.filename,
        "page_count": len(pages),
        "chunk_count": len(document_index.chunks),
        "summary": summary,
        "topics": topics,
        "keywords": keywords,
        "preview": full_text[:1000],
    }


@app.post("/similarity/search")
async def similarity_search(
    query: str = Body(..., embed=True),
    top_k: int = Body(5, embed=True),
):
    results = document_index.search(query, top_k=top_k)
    return {"query": query, "top_k": top_k, "results": results}


@app.post("/grammar/correct")
async def grammar_correct(req: GrammarRequest):
    corrected = correct_grammar(req.text)
    return {"original": req.text, "corrected": corrected}

@app.post(
    "/pdf/smart",
    responses={
        200: {
            "content": {
                "application/pdf": {
                    "schema": {
                        "type": "string",
                        "format": "binary",
                    }
                }
            },
            "description": "Smart PDF analysis report as PDF file",
        }
    },
)
async def smart_pdf_endpoint(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    pages = extract_pdf_pages(pdf_bytes)
    full_text = "\n".join(pages)

    report = analyze_pdf(full_text, file.filename)

    output_path = f"report_{file.filename}.pdf"
    generate_report_pdf(report, output_path)

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename=f"report_{file.filename}.pdf",
    )

