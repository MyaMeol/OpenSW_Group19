from __future__ import annotations
from typing import Any, Dict, Optional
from transformers import pipeline

_model: Optional[Any] = None


def load_grammar_model(model_name: str = "prithivida/grammar_error_correcter_v1") -> Any:
    global _model
    if _model is None:
        _model = pipeline("text2text-generation", model=model_name)
    return _model


def run_grammar_correction(grammar_model: Any, text: str) -> Dict:
    text = (text or "").strip()
    if not text:
        return {"original": "", "corrected": ""}

    prompt = "gec: " + text
    out = grammar_model(prompt, max_length=max(32, len(text.split()) * 2), do_sample=False)
    corrected = (out[0].get("generated_text", "") if out else "").strip()
    return {"original": text, "corrected": corrected}
