# grammar.py
from transformers import pipeline

# 처음 호출할 때만 모델을 다운로드해서 시간이 좀 걸릴 수 있음
_grammar_corrector = None


def get_grammar_pipeline():
    global _grammar_corrector
    if _grammar_corrector is None:
        # 영어 grammar correction 용으로 많이 쓰이는 모델 중 하나
        _grammar_corrector = pipeline(
            "text2text-generation",
            model="prithivida/grammar_error_correcter_v1"
        )
    return _grammar_corrector


def correct_grammar(text: str) -> str:
    """
    영어 문장을 grammar correction 해서 반환.
    """
    nlp = get_grammar_pipeline()

    # 이 모델은 입력 앞에 'gec:' 프리픽스를 붙이는 방식을 쓴다.
    prompt = "gec: " + text

    result = nlp(
        prompt,
        max_length=len(text.split()) * 2,  # 너무 긴 문장이면 늘려도 됨
        clean_up_tokenization_spaces=True
    )[0]["generated_text"]

    return result.strip()
