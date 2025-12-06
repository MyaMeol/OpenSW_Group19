# topic_sentence_generator.py
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import nltk

nltk.download('punkt')

# 임베딩 모델 
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# BERTopic 생성
topic_model = BERTopic(embedding_model=embedding_model)

# 요약/생성 모델
label_generator = pipeline("text2text-generation", model="facebook/bart-large-cnn")


def generate_topic_sentence(topic_words):
    # 토픽 키워드를 기반으로 짧은 주제 문장 생성
    text = ", ".join([w[0] for w in topic_words])
    summary = label_generator(text, max_length=20, min_length=5, num_beams=4)
    return summary[0]["generated_text"]


def extract_topic_labels(text: str):
    from nltk.tokenize import sent_tokenize
    docs = sent_tokenize(text)

    if len(docs) < 2:
        return {"error": "문장이 2개 이상일 때 토픽이 안정적으로 생성됩니다"}

    topics, probs = topic_model.fit_transform(docs)
    topic_info = topic_model.get_topic_info()

    topic_labels = {}

    for topic_id in topic_info["Topic"]:
        if topic_id == -1:
            continue
        words = topic_model.get_topic(topic_id)
        label = generate_topic_sentence(words)
        topic_labels[topic_id] = label

    return topic_labels


if __name__ == "__main__":
    text = input("분석할 문장을 입력하세요:\n")
    result = extract_topic_labels(text)

    print("\n=== 추출된 주제 문장 ===")
    print(result)  # 주제 문장만 출력
