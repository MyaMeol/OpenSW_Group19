# pdf_analysis.py
import fitz
from typing import List, Optional
from sentence_transformers import SentenceTransformer, util

def extract_pdf_pages(pdf_bytes: bytes) -> List[str]:
    """
    PDF 바이트를 받아서 페이지별 텍스트 리스트로 반환
    """
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = []
    for page in doc:
        text = page.get_text("text")
        pages.append(text)
    return pages

# ===== 1) 긴 텍스트를 chunk 로 나누기 =====
def split_into_chunks(text: str, max_chars: int = 500) -> List[str]:
    """
    너무 긴 텍스트를 max_chars 단위로 잘라 chunk 리스트로 만든다.
    줄바꿈 기준으로 적당히 나누고, 그래도 길면 쪼갬.
    """
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks: List[str] = []
    current = ""

    for p in paragraphs:
        # 현재 chunk에 이 문단을 붙였을 때 너무 길면 끊기
        if len(current) + len(p) + 1 > max_chars:
            if current:
                chunks.append(current)
            # 문단 자체가 너무 길면 강제로 쪼개서 넣기
            if len(p) > max_chars:
                for i in range(0, len(p), max_chars):
                    chunks.append(p[i:i + max_chars])
                current = ""
            else:
                current = p
        else:
            if current:
                current += "\n" + p
            else:
                current = p

    if current:
        chunks.append(current)

    return chunks


# ===== 2) sentence-transformers 모델 & 임베딩 =====
_model: Optional[SentenceTransformer] = None


def get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        # 가벼운 임베딩 모델
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _model


def embed_texts(texts: List[str]):
    model = get_model()
    return model.encode(texts, convert_to_tensor=True)


# ===== 3) 전역 문서 인덱스 =====
class DocumentIndex:
    def __init__(self):
        self.chunks: List[str] = []
        self.embeddings = None   # torch.Tensor
        self.source_pdf_name: Optional[str] = None

    def build(self, full_text: str, source_pdf_name: Optional[str] = None):
        """
        전체 텍스트를 받아 chunk 리스트를 만들고, 임베딩까지 미리 생성
        """
        self.chunks = split_into_chunks(full_text)
        if not self.chunks:
            self.embeddings = None
            return

        self.embeddings = embed_texts(self.chunks)
        self.source_pdf_name = source_pdf_name

    def search(self, query: str, top_k: int = 5):
        """
        쿼리(질문 등)에 대해 가장 비슷한 chunk top_k개 반환
        """
        if self.embeddings is None or not self.chunks:
            return []

        query_emb = embed_texts([query])[0]
        cos_scores = util.cos_sim(query_emb, self.embeddings)[0]
        top_results = cos_scores.topk(k=min(top_k, len(self.chunks)))

        results = []
        for score, idx in zip(top_results.values, top_results.indices):
            i = int(idx)
            results.append({
                "chunk_index": i,
                "text": self.chunks[i],
                "score": float(score)
            })
        return results


# 서버에서 쓸 전역 인스턴스 하나
document_index = DocumentIndex()