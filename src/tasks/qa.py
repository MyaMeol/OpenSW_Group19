from transformers import pipeline

def load_model():
    """
    Pretrained Question Answering 모델 로드
    """
    model_name = "distilbert-base-uncased-distilled-squad"
    qa = pipeline("question-answering", model=model_name)
    return qa

def run_qa(question, context):
    """
    Q&A 수행
    """
    qa = load_model()
    result = qa(question=question, context=context)
    return result

if __name__ == "__main__":
    print("=== Q&A 콘솔 프로그램 ===")
    print("질문을 입력하면, 지문을 기반으로 답변을 생성합니다.\n")

    context = input("지문(context)을 입력하세요:\n> ")
    question = input("\n질문(question)을 입력하세요:\n> ")

    output = run_qa(question, context)

    print("\n=== 결과 ===")
    print("Answer:", output["answer"])
    print("Score :", output["score"])

