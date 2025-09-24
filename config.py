"""
MCP 서버 설정 파일
"""

import os
from typing import Optional

class Config:
    """MCP 서버 설정 클래스"""
    
    # 서버 기본 정보
    SERVER_NAME: str = "KoreanNameGenerator"
    SERVER_VERSION: str = "1.0.0"
    SERVER_DESCRIPTION: str = "키워드 기반 한국 이름 생성 MCP 서버"
    
    # 로깅 설정
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # 서버 포트 (필요시)
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # 이름 생성 설정
    MAX_NAME_COUNT: int = 10
    MIN_NAME_COUNT: int = 1
    
    # 기본 스타일 옵션
    DEFAULT_STYLE: str = "cute"
    AVAILABLE_STYLES: list = ["cute", "cool", "elegant", "funny", "traditional"]
    
    # 기본 성별 옵션
    DEFAULT_GENDER: str = "any"
    AVAILABLE_GENDERS: list = ["male", "female", "any"]

