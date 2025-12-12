from __future__ import annotations
from typing import Any, Dict, List, Optional
from transformers import pipeline

_MODEL_NAME = "facebook/bart-large-mnli"
_classifier: Optional[Any] = None

DEFAULT_LABELS: List[str] = [
    "education", "technology", "science", "economy",
    "health", "sports", "politics", "entertainment", "general"
]


def load_topic_classifier(model_name: str = _MODEL_NAME) -> Any:
    global _classifier
    if _classifier is None:
        _classifier = pipeline("zero-shot-classification", model=model_name)
    return _classifier


def run_topic_classification(classifier: Any, text: str, labels: List[str] = DEFAULT_LABELS) -> Dict:
    text = (text or "").strip()
    if not text:
        return {"error": "text가 비어 있습니다.", "top_label": "general", "top_score": 0.0}

    out = classifier(text, candidate_labels=labels)
    if not out:
        return {"top_label": "general", "top_score": 0.0}

    top_label = out["labels"][0] if out.get("labels") else "general"
    top_score = float(out["scores"][0]) if out.get("scores") else 0.0
    return {
        "top_label": top_label,
        "top_score": top_score,
        "labels": out.get("labels", []),
        "scores": out.get("scores", []),
    }
