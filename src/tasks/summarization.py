from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def run(text):
    """
    Summarization Task using facebook/bart-large-cnn
    긴 문장을 요약하여 반환한다.
    """
    # 입력 문장을 토크나이징
    inputs = tokenizer(text, max_length=1024, truncation=True, return_tensors="pt")

    # 요약 생성
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=130,
        min_length=30,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    # 디코딩하여 텍스트로 변환
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text


if __name__ == "__main__":
    # 사용자 입력
    user_text = input("요약하고 싶은 긴 문장을 입력하세요:\n")

    result = run(user_text)

    print("\n=== 요약 결과 ===")
    print(result)

