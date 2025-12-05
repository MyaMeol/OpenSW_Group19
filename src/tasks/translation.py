from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-ko-en"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def run(text):
    """
    Translation Task: Korean → English
    사용자로부터 입력된 한국어 문장을 영어로 번역해 반환한다.
    """
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

if __name__ == "__main__":
    # 사용자에게 한국어 문장 입력받기
    user_input = input("번역할 한국어 문장을 입력하세요: ")
    result = run(user_input)

    print("\n=== 번역 결과 ===")
    print("Input :", user_input)
    print("Output:", result)
