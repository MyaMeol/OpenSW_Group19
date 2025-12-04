# StudyTextLab - UI Utilities

import os
from typing import Any


def clear_screen() -> None:
    """터미널 화면을 지움 (플랫폼 별 분기)."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title: str) -> None:
    clear_screen()
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)


def print_current_text_preview(text: str, max_chars: int = 120) -> None:
    print("\n[현재 텍스트 미리보기]")
    if not text.strip():
        print("  (현재 텍스트 없음)")
        print("-" * 60)
        return

    preview = text.replace("\n", " ")
    if len(preview) > max_chars:
        preview = preview[: max_chars - 3] + "..."
    print(f"  {preview}")
    print("-" * 60)


def print_main_menu() -> None:
    print("텍스트 관리")
    print("  [T] 텍스트 직접 입력")
    print("  [F] data/ 폴더에서 TXT 파일 선택")
    print("  [C] 현재 텍스트 지우기")
    print()
    print("NLP 기능")
    print("  [1] Q&A (질문-답변)")
    print("  [2] Summarization (요약)")
    print("  [3] Translation (번역)")
    print("  [4] Sentiment Analysis (감정 분석)")
    print("  [5] Topic Classification (주제 분류)")
    print("  [6] Keyword Extraction (키워드 추출)")
    print("  [7] Similarity Check (유사도 검사)")
    print("  [8] Grammar Correction (문법 교정)")
    print("  [P] PDF Smart Analysis (요약+주제+키워드)")
    print()
    print("히스토리 & 종료")
    print("  [H] 히스토리 보기")
    print("  [Q] 종료")
    print("-" * 60)


def prompt_command() -> str:
    cmd = input("명령을 입력하세요: ").strip().lower()
    return cmd


def prompt_question() -> str:
    return input("\n[Q&A] 질문을 입력하세요: ").strip()


def print_error(msg: str) -> None:
    print(f"\n[ERROR] {msg}\n")


def print_info(msg: str) -> None:
    print(f"\n[INFO] {msg}\n")


def print_result_block(title: str, data: Any) -> None:
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

    # data 타입에 따라 출력 방식 다르게
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"- {k}: {v}")
    elif isinstance(data, list):
        for i, item in enumerate(data, start=1):
            print(f"[{i}] {item}")
    else:
        print(data)

    print("=" * 60 + "\n")


def print_history_list(files: list[str]) -> None:
    print("\n=== Saved Histories ===")
    for idx, name in enumerate(files, start=1):
        print(f"[{idx}] {name}")
    print("=======================\n")
