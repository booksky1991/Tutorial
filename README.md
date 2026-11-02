# 파일 정리 프로그램 (Tutorial)

파일을 확장자별 카테고리에 따라 자동으로 분류하고 정리하는 프로그램입니다.

---

## 주요 기능

1. **확장자별 자동 분류**
   - 파일의 확장자를 분석하여 해당하는 카테고리 디렉터리로 자동 분류합니다.
   - 지원하는 기본 카테고리:
     - **Documents (문서):** `.txt`, `.pdf`, `.docx`, `.doc`, `.xlsx`, `.pptx`, `.hwp` 등
     - **Images (이미지):** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg` 등
     - **Videos (영상):** `.mp4`, `.avi`, `.mkv`, `.mov` 등
     - **Audio (음향):** `.mp3`, `.wav`, `.flac` 등
     - **Archives (압축 파일):** `.zip`, `.tar`, `.gz`, `.rar`, `.7z` 등
     - **Others (기타):** 위에 해당하지 않는 모든 파일

2. **단일 디렉터리 일괄 정리**
   - 지정된 폴더 내의 파일들을 각 카테고리 폴더로 이동시키고, 정리된 파일 수 요약을 반환합니다.

---

## 실행 방법

프로젝트 루트 디렉터리에서 `uv`를 사용하여 프로그램을 실행합니다.

```bash
uv run main.py
```

---

## 코드 사용 예시

파이썬 코드에서 직접 모듈을 가져와 특정 디렉터리를 정리할 수 있습니다.

```python
from tutorial import organize_directory

# 정리할 디렉터리 경로 지정
target_directory = "./my_folder"

# 파일 정리 실행
result = organize_directory(target_directory)
print(f"정리 결과: {result}")
```
