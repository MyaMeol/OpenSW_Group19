from __future__ import annotations
from typing import Any, Optional
from transformers import pipeline

# 기본: 한국어 → 영어
_DEFAULT_MODEL = "Helsinki-NLP/opus-mt-ko-en"
_translator: Optional[Any] = None
_loaded_model: Optional[str] = None


def load_translator(model_name: str = _DEFAULT_MODEL) -> Any:
    global _translator, _loaded_model
    if _translator is None or _loaded_model != model_name:
        _translator = pipeline("translation", model=model_name)
        _loaded_model = model_name
    return _translator


def run_translation(translator: Any, text: str) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    out = translator(text)
    return (out[0].get("translation_text", "") if out else "").strip()
