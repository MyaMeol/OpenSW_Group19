# StudyTextLab - Loaders

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"


def load_text_from_user() -> str:
    """
    여러 줄 텍스트를 입력받음.
    (Ctrl+D / Ctrl+Z+Enter 로 종료)
    """
    print("\n여러 줄 텍스트를 입력한 뒤, 입력 종료 시 Ctrl+D(또는 Ctrl+Z+Enter)를 누르세요.")
    print("-" * 60)
    lines: list[str] = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    text = "\n".join(lines).strip()
    return text


def load_text_from_txt_file(path: Path) -> str:
    """주어진 TXT 파일 경로에서 텍스트를 읽어옴."""
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def select_txt_file_interactive() -> Path | None:
    """
    data/ 폴더 안의 .txt 파일 목록을 보여주고
    번호로 선택하게 함. 선택된 파일 Path 반환.
    """
    DATA_DIR.mkdir(exist_ok=True)
    txt_files = sorted(DATA_DIR.glob("*.txt"))

    if not txt_files:
        print("\n[data/] 폴더에 .txt 파일이 없습니다. 먼저 파일을 넣어 주세요.\n")
        return None

    print("\n[data/] 폴더의 TXT 파일 목록:")
    for idx, p in enumerate(txt_files, start=1):
        print(f"[{idx}] {p.name}")
    choice = input("열고 싶은 파일 번호를 입력하세요 (엔터: 취소): ").strip()
    if not choice:
        return None

    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(txt_files):
            raise ValueError
    except ValueError:
        print("\n잘못된 번호입니다.\n")
        return None

    return txt_files[idx]


def select_pdf_file_interactive() -> Path | None:
    """
    data/ 폴더 안의 .pdf 파일 목록을 보여주고
    번호로 선택하게 함. 선택된 파일 Path 반환.
    """
    DATA_DIR.mkdir(exist_ok=True)
    pdf_files = sorted(DATA_DIR.glob("*.pdf"))

    if not pdf_files:
        print("\n[data/] 폴더에 .pdf 파일이 없습니다. 먼저 파일을 넣어 주세요.\n")
        return None

    print("\n[data/] 폴더의 PDF 파일 목록:")
    for idx, p in enumerate(pdf_files, start=1):
        print(f"[{idx}] {p.name}")
    choice = input("분석할 파일 번호를 입력하세요 (엔터: 취소): ").strip()
    if not choice:
        return None

    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(pdf_files):
            raise ValueError
    except ValueError:
        print("\n잘못된 번호입니다.\n")
        return None

    return pdf_files[idx]
