from transformers import pipeline

def load_sentiment():
    """
    Sentiment Analysis 모델 로드
    """
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    analyzer = pipeline("sentiment-analysis", model=model_name)
    return analyzer

def run_sentiment(text):
    analyzer = load_sentiment()
    result = analyzer(text)
    return result[0]

if __name__ == "__main__":
    print("=== Sentiment 분석 프로그램 ===")
    user_input = input("감성 분석할 문장을 입력하세요:\n> ")

    output = run_sentiment(user_input)

    print("\n=== 분석 결과 ===")
    print("Label:", output["label"])
    print("Score:", output["score"])

