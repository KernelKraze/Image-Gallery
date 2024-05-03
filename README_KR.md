# 🖼️ 이미지 갤러리 프로젝트

이미지 갤러리 프로젝트에 오신 것을 환영합니다! 이 저장소는 라즈베리 파이에서 이미지 및 비디오 컬렉션을 표시하고 관리하는 견고한 솔루션을 제공합니다.

## 📂 프로젝트 구조

📁 Project Root

📝 CreateJson.py
🖼️ banner.png
📝 check_thumb.py
📝 create_gallery_pages.py
📷 default_thumb.png
📝 generate_thumbnails.py
🖥️ index.html
📝 media.json
📜 script.js
🎨 wel-come.svg
    📁 .static
        📁 css
            🎨 global.css



## 🚀 시작하기

1. **CreateJson.py**: 이 스크립트는 미디어 디렉터리를 스캔하여 챕터와 페이지로 미디어 파일을 정리하고 메타데이터가 포함된 `media.json` 파일을 생성합니다.

2. **check_thumb.py**: 이 스크립트는 `media.json`에 나열된 모든 미디어 항목의 썸네일이 존재하는지 확인합니다.

3. **create_gallery_pages.py**: 이 스크립트는 페이징 기능이 있는 갤러리 HTML 페이지를 생성합니다.

4. **generate_thumbnails.py**: 이 스크립트는 FFmpeg을 사용하여 모든 미디어 파일의 썸네일을 생성합니다.

5. **index.html**: 이미지 갤러리의 주요 진입점입니다.

6. **script.js**: 갤러리 상호 작용을 처리하는 JavaScript 파일로, 모달에 이미지나 비디오를 표시하는 등의 기능을 제공합니다.

7. **banner.png** 및 **wel-come.svg**: 갤러리 배너 이미지입니다.

8. **default_thumb.png**: 특정 썸네일이 없는 미디어 항목에 대한 기본 썸네일입니다.

9. **.static/css/global.css**: 갤러리의 스타일링을 위한 전역 CSS 파일입니다.

## ✨ 기능

- 🖼️ **이미지 및 비디오 지원**: 갤러리는 이미지와 비디오를 모두 지원합니다.
- 📋 **미디어 메타데이터**: 챕터 및 페이지에 따라 파일 이름 패턴을 기반으로 미디어 파일을 정리합니다.
- 🖼️ **썸네일**: 미디어 파일에 대한 썸네일을 생성하고 사용합니다.
- 📃 **HTML 갤러리 페이지**: 페이징된 HTML 갤러리 페이지를 자동으로 생성합니다.
- 🎯 **사용자 친화적인 인터페이스**: 모달 및 네비게이션 기능이 있는 인터랙티브 갤러리입니다.

## 🛠️ 사용 방법

1. **미디어 폴더 만들기**: 먼저, 미디어 파일을 위한 디렉터리를 만드세요. 디렉터리 이름은 `{number}photo` 형식으로 지정하고, `{number}`에는 챕터나 식별자를 입력하세요.

2. **스크립트 실행**:
   - `CreateJson.py`를 실행하여 메타데이터가 포함된 `media.json` 파일을 생성하세요.
   - `generate_thumbnails.py`를 실행하여 미디어 파일의 썸네일을 만드세요.

3. **썸네일 확인**: 일부 썸네일이 누락되었다고 생각하면, `check_thumb.py`를 실행하여 자동으로 문제를 확인하고 수정하세요.

4. **자산 준비**: 다음 자산을 준비하세요:
   - `banner.png`
   - `default_thumb.png`
   - `wel-come.svg`

   또는, 이 자산을 커스터마이징하려면 직접 소스 코드를 조정할 수 있습니다.


## 📜 라이선스

이 프로젝트는 MIT 라이선스로 허가됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.
