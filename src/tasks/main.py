from fastapi import FastAPI, UploadFile, File, Body
from pydantic import BaseModel

from pdf_analysis import extract_pdf_pages, document_index
from grammar import correct_grammar

app = FastAPI()

class GrammarRequest(BaseModel):
    text: str

@app.post("/pdf/analyze")
async def analyze_pdf(file: UploadFile = File(...)):
    """
    PDF 업로드 → 텍스트 추출 + 인덱스 생성
    """
    pdf_bytes = await file.read()

    pages = extract_pdf_pages(pdf_bytes)
    full_text = "\n".join(pages)

    # ✅ similarity 검색을 위해 전역 인덱스 생성
    document_index.build(full_text, source_pdf_name=file.filename)

    # 아직 팀원 기능 없으니까 임시 요약/토픽/키워드
    summary = full_text[:300] + "..." if len(full_text) > 300 else full_text
    topics = ["mock-topic-1", "mock-topic-2"]
    keywords = ["mock-keyword-1", "mock-keyword-2", "mock-keyword-3"]

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
    """
    query를 넣으면 인덱싱된 PDF에서 비슷한 chunk top_k개 반환
    """
    results = document_index.search(query, top_k=top_k)
    return {
        "query": query,
        "top_k": top_k,
        "results": results,
    }

@app.post("/grammar/correct")
async def grammar_correct(req: GrammarRequest):
    """
    영어 문장 grammar correction API
    """
    corrected = correct_grammar(req.text)
    return {
        "original": req.text,
        "corrected": corrected,
    }
