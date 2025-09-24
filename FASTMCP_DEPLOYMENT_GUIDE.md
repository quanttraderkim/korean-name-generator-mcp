# FastMCP Cloud 배포 가이드

이 문서는 FastMCP Cloud를 사용하여 MCP 서버를 배포하는 완전한 워크플로우를 설명합니다.

## 🚀 전체 배포 프로세스

### 1단계: 프로젝트 설정

```bash
# 1. 프로젝트 디렉터리 생성
mkdir my-mcp-server
cd my-mcp-server

# 2. Python 가상환경 설정
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. FastMCP 설치
pip install fastmcp

# 4. 의존성 파일 생성
pip freeze > requirements.txt
```

### 2단계: FastMCP 서버 개발

`main.py` 파일 생성:

```python
"""
MCP 서버 설명
"""

from fastmcp import FastMCP
import random

# Create server
mcp = FastMCP("서버이름")

@mcp.tool
def my_function(param: str) -> dict:
    """함수 설명
    
    Args:
        param: 파라미터 설명
    
    Returns:
        dict: 반환값 설명
    """
    # 함수 로직
    return {"result": "값"}

if __name__ == "__main__":
    mcp.run()
```

### 3단계: GitHub 배포

```bash
# 1. Git 초기화
git init

# 2. .gitignore 파일 생성
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
EOF

# 3. 파일 추가 및 커밋
git add .
git commit -m "Initial commit: MCP 서버 초기 설정"

# 4. GitHub 레포지토리 생성
gh repo create my-mcp-server --public --description "MCP 서버 설명"

# 5. 원격 저장소 연결 및 푸시
git remote add origin https://github.com/사용자명/my-mcp-server.git
git push -u origin main
```

### 4단계: FastMCP Cloud 배포

1. **FastMCP Cloud 접속**
   - https://fastmcp.cloud 방문
   - GitHub 계정으로 로그인

2. **프로젝트 생성**
   - "Create a Project" 클릭
   - GitHub 레포지토리 선택

3. **프로젝트 설정**
   - **Server Name**: 원하는 서버 이름 (변경 불가)
   - **Entrypoint**: `main.py`
   - **Authentication**: 필요에 따라 설정
   - **Discoverable**: 공개 여부 설정

4. **배포 실행**
   - "Deploy Server" 클릭
   - 자동 빌드 및 배포 완료 대기

## 📝 실제 프로젝트 예시들

### 예시 1: Lotto Number Generator (최초 프로젝트)

#### 프로젝트 정보
- **GitHub 리포지토리**: `https://github.com/quanttraderkim/lotto-mcp-server`
- **Server Name**: `lotto-mcp-server`
- **Entry Point**: `main.py`
- **배포 URL**: `https://lotto-mcp-server.fastmcp.app/mcp`

#### 구현된 기능
1. **`generate_lotto_numbers`** - 로또 번호 조합 생성 (개수 지정 가능)
2. **`get_lucky_number`** - 행운의 로또 번호 추천 (메시지 포함)

#### 배포 설정 예시
```
Server Name: lotto-mcp-server
Entry Point: main.py
Repository: https://github.com/quanttraderkim/lotto-mcp-server
```

### 예시 2: Tasting Note Assistant

#### 프로젝트 정보
- **GitHub 리포지토리**: `https://github.com/quanttraderkim/tasting-note-mcp`
- **Server Name**: `tasting-note-mcp`
- **Entry Point**: `main.py`
- **배포 URL**: `https://tasting-note-mcp.fastmcp.app/mcp`

#### 구현된 기능
1. **`create_whisky_tasting_note_prompt`** - 위스키 테이스팅 노트 프롬프트 생성
2. **`create_wine_tasting_note_prompt`** - 와인 테이스팅 노트 프롬프트 생성

#### 배포 설정 예시
```
Server Name: tasting-note-mcp
Entry Point: main.py
Repository: https://github.com/quanttraderkim/tasting-note-mcp
```

### 예시 3: URL Shortener

#### 프로젝트 정보
- **GitHub 리포지토리**: `https://github.com/quanttraderkim/url-shortener-mcp`
- **Server Name**: `url-shortener-mcp`
- **Entry Point**: `main.py`
- **배포 URL**: `https://url-shortener-mcp.fastmcp.app/mcp`

#### 구현된 기능
1. **`shorten_url`** - 긴 URL을 짧은 TinyURL로 변환

#### 배포 설정 예시
```
Server Name: url-shortener-mcp
Entry Point: main.py
Repository: https://github.com/quanttraderkim/url-shortener-mcp
```

### 5단계: 업데이트 배포

```bash
# 1. 코드 수정 후 커밋
git add .
git commit -m "기능 업데이트: 설명"

# 2. GitHub에 푸시
git push origin main

# 3. FastMCP Cloud에서 자동 재배포
# (main 브랜치에 푸시하면 자동으로 재배포됨)
```

## 📋 배포 후 확인사항

### 배포된 서버 정보
- **서버 URL**: `https://서버명.fastmcp.app/mcp`
- **상태**: FastMCP Cloud 대시보드에서 확인
- **로그**: 서버 로그에서 실행 상태 확인

### MCP 클라이언트 연결 설정

**Claude Desktop 설정** (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "lotto-mcp-server": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://lotto-mcp-server.fastmcp.app/mcp"]
    },
    "tasting-note-mcp": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://tasting-note-mcp.fastmcp.app/mcp"]
    },
    "url-shortener-mcp": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://url-shortener-mcp.fastmcp.app/mcp"]
    }
  }
}
```

**Cursor 설정**:
```json
{
  "mcpServers": {
    "lotto-mcp-server": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://lotto-mcp-server.fastmcp.app/mcp"]
    },
    "tasting-note-mcp": {
      "command": "npx", 
      "args": ["@modelcontextprotocol/inspector", "https://tasting-note-mcp.fastmcp.app/mcp"]
    },
    "url-shortener-mcp": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://url-shortener-mcp.fastmcp.app/mcp"]
    }
  }
}
```

### 일반적인 서버 설정 템플릿
```json
{
  "mcpServers": {
    "서버이름": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://서버이름.fastmcp.app/mcp"]
    }
  }
}
```

## 🔧 개발 팁

### 로컬 테스트
```bash
# MCP Inspector로 로컬 테스트
fastmcp dev main.py
```

### 도구(Tool) 개발 가이드
- `@mcp.tool` 데코레이터 사용
- 타입 힌트 필수 (`param: str`, `-> dict`)
- 명확한 docstring 작성
- JSON 형태로 반환

### 에러 해결
- **빌드 실패**: `requirements.txt` 확인
- **연결 실패**: 서버 URL 확인
- **도구 인식 안됨**: 함수명과 docstring 확인

## 📚 참고 자료

- [FastMCP 공식 문서](https://gofastmcp.com/)
- [MCP 프로토콜](https://modelcontextprotocol.io/)
- [FastMCP Cloud](https://fastmcp.cloud)

---

**마지막 업데이트**: 2025년 9월 17일 (Lotto Generator, Tasting Note Assistant, URL Shortener 프로젝트 예시 추가)
**작성자**: AI Assistant
