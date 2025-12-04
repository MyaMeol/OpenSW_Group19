# StudyTextLab - History Manager

from pathlib import Path
from datetime import datetime
import json
from typing import Any

ROOT_DIR = Path(__file__).resolve().parent.parent
HISTORY_DIR = ROOT_DIR / "history"
HISTORY_DIR.mkdir(exist_ok=True)


def save_history(task_name: str, input_data: dict, output_data: dict | list | Any) -> None:
    """
    Task 실행 결과를 JSON 파일로 저장.
    파일 이름: YYYYMMDD_HHMMSS_taskname.json
    """
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{ts}_{task_name}.json"
    path = HISTORY_DIR / filename

    payload = {
        "task": task_name,
        "timestamp": ts,
        "input": input_data,
        "output": output_data,
    }

    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def list_history_files() -> list[str]:
    """history/ 폴더에 저장된 JSON 파일 이름 목록을 반환."""
    files = sorted(HISTORY_DIR.glob("*.json"))
    return [f.name for f in files]


def load_history_file(filename: str) -> dict:
    """주어진 JSON 히스토리 파일을 읽어서 dict로 반환."""
    path = HISTORY_DIR / filename
    if not path.exists():
        return {"error": "해당 히스토리 파일이 존재하지 않습니다."}

    with path.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return {"error": "히스토리 파일을 읽는 중 JSON 파싱 에러가 발생했습니다."}
    return data
