from __future__ import annotations
from typing import List, Optional
from keybert import KeyBERT

_kw_model: Optional[KeyBERT] = None


def _get_kw_model() -> KeyBERT:
    global _kw_model
    if _kw_model is None:
        _kw_model = KeyBERT("sentence-transformers/all-MiniLM-L6-v2")
    return _kw_model


def extract_keywords(text: str, top_k: int = 10) -> List[str]:
    text = (text or "").strip()
    if not text:
        return []

    model = _get_kw_model()
    results = model.extract_keywords(
        text,
        top_n=top_k,
        use_maxsum=True,
        nr_candidates=max(20, top_k * 4),
    )
    return [kw for kw, _score in results]
