# Korean Name Generator MCP Server

키워드 기반으로 재밌는 한국 이름을 생성하는 MCP 서버입니다.

## 기능

- 키워드를 입력받아 관련된 한국 이름을 생성
- 다양한 스타일의 이름 생성 (cute, cool, elegant, funny, traditional)
- 성별에 따른 이름 생성 옵션
- 이름의 의미 해석 기능
- 키워드 카테고리별 제안 기능

## 설치

### 1. 가상환경 생성 및 활성화
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate     # Windows
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

## 사용법

### MCP 서버 실행
```bash
python main.py
```

### 사용 가능한 도구들

1. **`generate_korean_name`**: 키워드 기반 한국 이름 생성
   - 매개변수: keywords, gender, style, count
   - 예시: `["봄", "귀여운", "고양이"]` → "김봄이", "이꽃애" 등

2. **`get_name_meaning`**: 생성된 이름의 의미 해석
   - 매개변수: name
   - 예시: "김봄이" → 각 글자의 의미 설명

3. **`suggest_name_keywords`**: 사용 가능한 키워드 카테고리 제안
   - 자연/계절, 감정/성격, 색깔, 취미/관심사, 동물, 직업/꿈

## 키워드 예시

- **자연/계절**: 봄, 여름, 가을, 겨울, 바다, 산, 달, 별
- **감정/성격**: 용감, 똑똑, 귀여운, 재미, 차분, 활발
- **색깔**: 빨간, 파란, 노란, 하얀, 검은
- **동물**: 고양이, 강아지, 토끼, 곰, 새
- **취미**: 음악, 그림, 책, 운동, 요리, 게임

## 스타일 옵션

- `cute`: 귀여운 스타일 (예: 김봄이, 이꽃애)
- `cool`: 멋진 스타일 (예: 김용준, 이강민)
- `elegant`: 우아한 스타일 (예: 김봄화, 이꽃연)
- `funny`: 재미있는 스타일 (예: 김뽀삐, 이꿀둥)
- `traditional`: 전통적인 스타일 (예: 김봄자, 이꽃순)
