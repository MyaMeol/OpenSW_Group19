# smart_pdf.py
from typing import List, Dict
import re
import fitz  # PyMuPDF
from fpdf import FPDF


# 1) PDF에서 텍스트 추출 (바이트 버전)
def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    texts = []
    for page in doc:
        texts.append(page.get_text())
    doc.close()
    return "\n\n".join(texts)


# 2) 간단 요약
def simple_summarize(text: str, max_chars: int = 800) -> str:
    text = text.strip()
    if not text:
        return ""

    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    joined = " ".join(paragraphs)

    if len(joined) <= max_chars:
        return joined

    return joined[:max_chars] + "..."


# 3) 키워드 추출
def extract_keywords(text: str, top_k: int = 10) -> List[str]:
    text = text.lower()
    tokens = re.findall(r"[a-zA-Z가-힣]{2,}", text)

    stopwords = set([
        "the", "and", "for", "with", "this", "that", "have", "from", "you",
        "are", "was", "were", "they", "them", "their", "into", "your", "about",
        "이것", "저것", "그리고", "하지만", "그러나", "해서", "때문", "위해"
    ])

    freq = {}
    for token in tokens:
        if token in stopwords:
            continue
        freq[token] = freq.get(token, 0) + 1

    sorted_tokens = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, c in sorted_tokens[:top_k]]


# 4) 토픽 분류 (규칙 기반)
def simple_topic_classify(text: str) -> Dict:
    t = text.lower()
    label = "general"

    if "machine learning" in t or "deep learning" in t:
        label = "ai_ml"
    elif "marketing" in t or "customer" in t:
        label = "marketing"
    elif "statistics" in t or "probability" in t:
        label = "statistics"

    return {"top_label": label, "top_score": 0.5}


# 5) PDF 분석 파이프라인
def analyze_pdf(raw_text: str, file_name: str | None = None) -> dict:
    pages = raw_text.split("\n\n")
    chunks = [p for p in pages if p.strip()]

    summary = simple_summarize(raw_text)
    topics = simple_topic_classify(raw_text)
    keywords = extract_keywords(raw_text)

    return {
        "file_name": file_name,
        "page_count": len(pages),
        "chunk_count": len(chunks),
        "summary": summary,
        "topics": topics,
        "keywords": keywords,
    }


# 6) 분석 결과를 PDF 리포트로 생성  (새 버전!!)
def generate_report_pdf(report: dict, output_path: str) -> str:
    pdf = FPDF()
    pdf.add_page()

    # 1. 폰트 등록 (보통 + Bold 둘 다)
    pdf.add_font("Malgun", "",  r"C:\Windows\Fonts\malgun.ttf",   uni=True)   # 보통
    pdf.add_font("Malgun", "B", r"C:\Windows\Fonts\malgunbd.ttf", uni=True)   # 굵게

    # 2. 기본 폰트 설정
    pdf.set_font("Malgun", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    # A4 기준 실제 쓸 수 있는 폭 (여백 제외)
    page_width = pdf.w - pdf.l_margin - pdf.r_margin

    # --- 텍스트 정리 유틸 함수들 ---

    def normalize_text(text: str | None, max_len: int = 4000) -> str:
        """너무 긴 텍스트 자르고, 너무 긴 단어를 쪼갬"""
        if text is None:
            return ""
        text = str(text).replace("\r", " ").strip()

        # 전체 길이 제한
        if len(text) > max_len:
            text = text[:max_len] + "..."

        # 공백 기준으로 나눠서 너무 긴 '단어'는 강제로 쪼개기
        pieces = []
        for word in text.split(" "):
            if len(word) <= 40:
                pieces.append(word)
            else:
                # 40자씩 잘라서 중간에 공백 넣어줌
                for i in range(0, len(word), 40):
                    pieces.append(word[i:i+40])
        return " ".join(pieces)

    def write_block(label: str, value: str | None):
        """제목 + 내용 한 블록 출력"""
        # 제목 굵게
        pdf.set_font("Malgun", style="B", size=12)
        pdf.multi_cell(page_width, 7, label)
        pdf.ln(1)

        # 내용 일반체
        pdf.set_font("Malgun", size=11)
        text = normalize_text(value)
        pdf.multi_cell(page_width, 6, text)
        pdf.ln(4)

    # --- 실제 내용 쓰기 ---

    pdf.set_font("Malgun", style="B", size=14)
    pdf.multi_cell(page_width, 9, "Smart PDF Analysis Report")
    pdf.ln(6)

    write_block("File:", report.get("file_name", "-"))
    write_block("Page count:", str(report.get("page_count", "-")))

    write_block("Summary:", report.get("summary", ""))

    topic_info = report.get("topics", {})
    topic_str = f"{topic_info.get('top_label', 'general')} (score: {topic_info.get('top_score', 0):.2f})"
    write_block("Topics:", topic_str)

    keywords = report.get("keywords", [])
    if isinstance(keywords, list):
        keywords_text = ", ".join(map(str, keywords))
    else:
        keywords_text = str(keywords)
    write_block("Keywords:", keywords_text)

    pdf.output(output_path)
    return output_path
