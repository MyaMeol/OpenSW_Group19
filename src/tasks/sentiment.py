from __future__ import annotations
from typing import Any, Dict, Optional
from transformers import pipeline

_MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
_sentiment_pipe: Optional[Any] = None


def load_sentiment_model(model_name: str = _MODEL_NAME) -> Any:
    global _sentiment_pipe
    if _sentiment_pipe is None:
        _sentiment_pipe = pipeline("sentiment-analysis", model=model_name)
    return _sentiment_pipe


def run_sentiment(sentiment_model: Any, text: str) -> Dict:
    text = (text or "").strip()
    if not text:
        return {"error": "text가 비어 있습니다.", "label": "", "score": 0.0}

    out = sentiment_model(text)
    # pipeline 반환은 list[dict] 형태
    d = out[0] if isinstance(out, list) and out else {}
    return {"label": d.get("label", ""), "score": float(d.get("score", 0.0))}
