from __future__ import annotations
from typing import Any, Optional
from transformers import pipeline

_MODEL_NAME = "facebook/bart-large-cnn"
_summarizer: Optional[Any] = None


def load_summarizer(model_name: str = _MODEL_NAME) -> Any:
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline("summarization", model=model_name)
    return _summarizer


def run_summarization(summarizer: Any, text: str, max_len: int = 130, min_len: int = 30) -> str:
    text = (text or "").strip()
    if not text:
        return ""

    # 너무 짧으면 요약이 오히려 이상해질 수 있어 그대로 반환
    if len(text.split()) < 20:
        return text

    out = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return (out[0].get("summary_text", "") if out else "").strip()
