from __future__ import annotations
from typing import Any, Dict, Optional
from sentence_transformers import SentenceTransformer, util

_model: Optional[SentenceTransformer] = None


def load_embedder(model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(model_name)
    return _model


def compute_similarity(embedder: Any, text_a: str, text_b: str) -> Dict:
    a = (text_a or "").strip()
    b = (text_b or "").strip()

    if not a or not b:
        return {"error": "비교할 두 텍스트가 필요합니다.", "similarity": None}

    emb = embedder.encode([a, b], convert_to_tensor=True)
    score = util.cos_sim(emb[0], emb[1]).item()
    return {"similarity": float(score)}
