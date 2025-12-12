from __future__ import annotations
from typing import Callable, Dict, Any
from pypdf import PdfReader


def extract_text_from_pdf_path(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    texts = []
    for page in reader.pages:
        t = page.extract_text() or ""
        texts.append(t)
    return "\n\n".join(texts).strip()


def analyze_pdf(
    summarizer: Any,
    topic_classifier: Any,
    keyword_extractor: Callable[[str, int], list],
    pdf_path: str,
) -> Dict:
    raw_text = extract_text_from_pdf_path(pdf_path)
    if not raw_text:
        return {"pdf_path": pdf_path, "error": "PDF에서 텍스트를 추출하지 못했습니다."}

    summary = ""
    try:
        # summarization.py의 run_summarization 형태를 그대로 사용한다고 가정
        from . import summarization as sum_mod
        summary = sum_mod.run_summarization(summarizer, raw_text, max_len=130, min_len=30)
    except Exception as e:
        summary = f"(summary error) {e}"

    topic = {}
    try:
        from . import topic_classification as tc_mod
        topic = tc_mod.run_topic_classification(topic_classifier, raw_text)
    except Exception as e:
        topic = {"error": str(e), "top_label": "general", "top_score": 0.0}

    kws = []
    try:
        kws = keyword_extractor(raw_text, 10)
    except Exception as e:
        kws = [f"(keywords error) {e}"]

    return {
        "pdf_path": pdf_path,
        "raw_text_length": len(raw_text),
        "summary": summary,
        "topic": topic,
        "keywords": kws,
    }
