from __future__ import annotations
from typing import Any, Dict, Optional
from transformers import pipeline

_MODEL_NAME = "distilbert-base-uncased-distilled-squad"
_qa_pipe: Optional[Any] = None


def load_qa_pipeline(model_name: str = _MODEL_NAME) -> Any:
    """Q&A pipeline을 1회 로딩 후 재사용."""
    global _qa_pipe
    if _qa_pipe is None:
        _qa_pipe = pipeline("question-answering", model=model_name)
    return _qa_pipe


def run_qa(qa_pipe: Any, context: str, question: str) -> Dict:
    """main에서 호출할 표준 인터페이스."""
    context = (context or "").strip()
    question = (question or "").strip()

    if not context or not question:
        return {"error": "context/question이 비어 있습니다.", "answer": "", "score": 0.0}

    result = qa_pipe(question=question, context=context)
    return {
        "answer": result.get("answer", ""),
        "score": float(result.get("score", 0.0)),
        "start": int(result.get("start", -1)),
        "end": int(result.get("end", -1)),
    }
