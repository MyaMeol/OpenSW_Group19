# keywords.py
from keybert import KeyBERT

# Sentence-Transformer 기반 키워드 모델 로드
model = KeyBERT("sentence-transformers/all-MiniLM-L6-v2")

def extract_keywords(text: str, top_k: int = 5):
    # text: 입력 문장/문서
    # top_k: 추출할 키워드 개수    
    
    results = model.extract_keywords(
        text,
        top_n=top_k,
        use_maxsum=True,     # 단어 중복 제거 
        nr_candidates=20
    )

    return [kw[0] for kw in results]


def run():
    text = input("주제어를 추출할 문장을 입력하세요:\n")
    keywords = extract_keywords(text)

    print("\n=== 주제어(Keyphrase) 추출 결과 ===")
    for idx, word in enumerate(keywords, 1):
        print(f"{idx}. {word}")


if __name__ == "__main__":
    run()
