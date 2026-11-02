from pathlib import Path
import shutil

EXTENSION_CATEGORIES: dict[str, str] = {
    # 문서
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    ".hwp": "Documents",
    # 이미지
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    # 비디오
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    # 오디오
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    # 압축파일
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
}


def get_category(extension: str) -> str:
    """확장자에 따른 분류 폴더명을 반환합니다."""
    return EXTENSION_CATEGORIES.get(extension.lower(), "Others")


def organize_directory(target_dir: str | Path) -> dict[str, int]:
    """지정된 디렉터리의 파일들을 확장자별 카테고리 폴더로 정리합니다."""
    base_path = Path(target_dir)

    if not base_path.exists() or not base_path.is_dir():
        print(f"경로를 찾을 수 없거나 디렉터리가 아닙니다: {base_path}")
        return {}

    summary: dict[str, int] = {}

    for item in base_path.iterdir():
        if not item.is_file():
            continue

        category = get_category(item.suffix)
        category_dir = base_path / category
        category_dir.mkdir(exist_ok=True)

        destination = category_dir / item.name
        shutil.move(str(item), str(destination))
        summary[category] = summary.get(category, 0) + 1

    return summary

