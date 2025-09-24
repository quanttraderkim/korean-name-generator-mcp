from fastmcp import FastMCP
from typing import List, Optional
import random
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MCP 서버 생성
mcp = FastMCP("KoreanNameGenerator")

# 한국어 성씨 데이터
FAMILY_NAMES = [
    "김", "이", "박", "최", "정", "강", "조", "윤", "장", "임",
    "한", "오", "서", "신", "권", "황", "안", "송", "전", "홍",
    "문", "양", "손", "배", "백", "허", "유", "남", "심", "노",
    "하", "곽", "성", "차", "주", "우", "구", "라", "마", "목"
]

# 키워드별 이름 구성 요소
KEYWORD_ELEMENTS = {
    # 자연/계절 관련
    "봄": ["봄", "춘", "화", "꽃", "새", "영", "연", "희", "미"],
    "여름": ["하", "열", "정", "양", "빛", "태", "진", "우", "성"],
    "가을": ["추", "단", "풍", "월", "금", "은", "실", "옥", "수"],
    "겨울": ["설", "한", "빙", "백", "청", "냉", "순", "결", "명"],
    "바다": ["해", "파", "물", "청", "깊", "넓", "푸", "른", "맑"],
    "산": ["산", "봉", "높", "웅", "장", "석", "암", "견", "고"],
    "달": ["월", "은", "밝", "야", "신", "비", "몽", "환", "야"],
    "별": ["성", "빛", "밤", "야", "은", "반", "짝", "빛", "눈"],
    
    # 감정/성격 관련  
    "용감": ["용", "웅", "강", "건", "담", "의", "호", "진", "무"],
    "똑똑": ["지", "슬", "명", "현", "총", "민", "영", "리", "혜"],
    "귀여운": ["귀", "애", "사", "랑", "예", "쁜", "달", "콤", "미"],
    "재미": ["재", "흥", "웃", "유", "쾌", "활", "명", "랑", "기"],
    "차분": ["차", "온", "순", "정", "고", "요", "안", "평", "화"],
    "활발": ["활", "발", "동", "적", "빠", "른", "쾌", "활", "생"],
    
    # 색깔 관련
    "빨간": ["홍", "적", "붉", "단", "주", "화", "열", "정", "진"],
    "파란": ["청", "푸", "른", "하늘", "바다", "시", "원", "한", "냉"],
    "노란": ["황", "금", "노", "란", "밝", "은", "따", "뜻", "온"],
    "하얀": ["백", "흰", "순", "결", "깨", "끗", "맑", "은", "설"],
    "검은": ["흑", "검", "은", "깊", "은", "진", "한", "그", "림"],
    
    # 취미/관심사 관련
    "음악": ["음", "성", "화", "선", "율", "소", "리", "가", "창"],
    "그림": ["화", "그", "색", "붓", "선", "미", "술", "작", "품"],
    "책": ["서", "글", "문", "학", "지", "식", "독", "서", "현"],
    "운동": ["체", "력", "건강", "강", "인", "빠", "른", "민", "첩"],
    "요리": ["맛", "향", "달", "콤", "감", "칠", "요", "리", "사"],
    "게임": ["놀", "이", "재", "미", "승", "부", "경", "쟁", "도전"],
    
    # 동물 관련
    "고양이": ["냥", "야옹", "귀", "엽", "털", "복", "실", "미", "애"],
    "강아지": ["멍", "왈", "충", "성", "활", "발", "사", "랑", "우"],
    "토끼": ["토", "깡", "총", "귀", "엽", "순", "하얀", "폭", "신"],
    "곰": ["웅", "크", "강", "력", "포", "근", "든", "든", "한"],
    "새": ["새", "날", "개", "자", "유", "하늘", "높", "이", "비행"],
    
    # 직업/꿈 관련
    "의사": ["의", "학", "치", "료", "생", "명", "건강", "돌", "봄"],
    "선생님": ["교", "육", "가", "르", "침", "지", "도", "현", "명"],
    "요리사": ["요", "리", "맛", "향", "솜", "씨", "창", "조", "달"],
    "예술가": ["예", "술", "창", "조", "미", "감", "작", "품", "아름"],
    "과학자": ["과", "학", "연", "구", "발", "견", "실", "험", "지"],
}

@mcp.tool
def generate_korean_name(
    keywords: List[str],
    gender: Optional[str] = "any",
    style: Optional[str] = "cute",
    count: Optional[int] = 3
) -> dict:
    """
    키워드를 기반으로 재미있는 한국 이름을 생성합니다.
    
    Args:
        keywords: 이름에 반영할 키워드들 (예: ["봄", "귀여운", "고양이"])
        gender: 성별 ("male", "female", "any")
        style: 이름 스타일 ("cute", "cool", "elegant", "funny", "traditional")
        count: 생성할 이름 개수 (1-10)
        
    Returns:
        dict: 생성된 이름들과 의미 설명
    """
    logger.info(f"키워드 기반 이름 생성 요청: {keywords}, 스타일: {style}, 개수: {count}")
    if count > 10:
        count = 10
    elif count < 1:
        count = 1
        
    generated_names = []
    
    for _ in range(count):
        # 성씨 선택
        family_name = random.choice(FAMILY_NAMES)
        
        # 키워드에서 이름 요소 추출
        name_elements = []
        for keyword in keywords:
            if keyword in KEYWORD_ELEMENTS:
                name_elements.extend(KEYWORD_ELEMENTS[keyword])
        
        # 키워드 매칭이 없으면 기본 요소 사용
        if not name_elements:
            default_elements = ["예", "쁜", "착", "한", "밝", "은", "좋", "아", "사랑"]
            name_elements = default_elements
        
        # 스타일에 따른 이름 구성
        if style == "cute":
            cute_endings = ["이", "아", "야", "애", "희", "미", "리", "지", "은", "콩", "별", "달"]
            given_name = random.choice(name_elements) + random.choice(cute_endings)
        elif style == "cool":
            cool_endings = ["준", "민", "진", "현", "성", "혁", "철", "강", "용", "호"]
            given_name = random.choice(name_elements) + random.choice(cool_endings)
        elif style == "elegant":
            elegant_endings = ["화", "연", "영", "정", "수", "윤", "서", "하", "율", "원"]
            given_name = random.choice(name_elements) + random.choice(elegant_endings)
        elif style == "funny":
            funny_elements = ["뽀", "삐", "꿀", "콩", "떡", "빵", "쪼", "망", "깜", "똘"]
            funny_endings = ["이", "찡", "롱", "둥", "뚱", "맹", "꾸", "또", "순", "돌"]
            given_name = random.choice(funny_elements) + random.choice(funny_endings)
        else:  # traditional
            traditional_endings = ["자", "숙", "순", "옥", "인", "경", "희", "란", "미", "선"]
            given_name = random.choice(name_elements) + random.choice(traditional_endings)
        
        full_name = family_name + given_name
        
        # 이름 의미 생성
        meaning = f"'{keywords}'의 특성을 담은 {style} 스타일의 이름"
        
        generated_names.append({
            "name": full_name,
            "meaning": meaning,
            "family_name": family_name,
            "given_name": given_name
        })
    
    return {
        "names": generated_names,
        "keywords_used": keywords,
        "style": style,
        "total_count": count
    }

@mcp.tool  
def get_name_meaning(name: str) -> dict:
    """
    한국 이름의 가능한 의미를 해석합니다.
    
    Args:
        name: 해석할 한국 이름
        
    Returns:
        dict: 이름의 의미 해석과 설명
    """
    # 한글 글자별 의미 사전 (간단한 예시)
    meanings = {
        # 자연 관련
        "봄": "생명력, 희망, 새로운 시작",
        "여름": "열정, 활력, 따뜻함",  
        "가을": "결실, 성숙, 풍요",
        "겨울": "순수, 깨끗함, 인내",
        "해": "밝음, 희망, 빛",
        "달": "아름다움, 신비, 평온",
        "별": "소원, 꿈, 빛남",
        "꽃": "아름다움, 사랑, 순수",
        
        # 덕목 관련
        "지": "지혜, 총명함",
        "혜": "은혜, 자비로움", 
        "선": "선함, 착함",
        "정": "정직, 바름",
        "의": "의로움, 정의",
        "용": "용기, 용맹함",
        "성": "성실함, 진실함",
        "민": "민첩함, 영민함",
        
        # 색깔/외모 관련
        "백": "하얀색, 순수함",
        "청": "파란색, 맑음", 
        "홍": "빨간색, 열정",
        "금": "황금색, 귀함",
        "은": "은색, 고귀함",
        "미": "아름다움",
        "예": "예쁨, 우아함",
        
        # 일반적 긍정 요소
        "희": "희망, 기쁨",
        "복": "복, 행운", 
        "영": "영원함, 빛남",
        "수": "물, 맑음, 오래삶",
        "원": "원만함, 둥글음"
    }
    
    # 이름에서 성과 이름 분리
    if len(name) >= 2:
        family = name[0]
        given = name[1:]
        
        # 각 글자의 의미 찾기
        given_meanings = []
        for char in given:
            if char in meanings:
                given_meanings.append(f"{char}: {meanings[char]}")
            else:
                given_meanings.append(f"{char}: 특별한 의미를 담은 글자")
    else:
        family = ""
        given = name
        given_meanings = [f"{name}: 독특하고 특별한 이름"]
    
    interpretation = f"'{name}'은(는) " + ", ".join([meaning.split(': ')[1] for meaning in given_meanings]) + "을(를) 의미하는 아름다운 이름입니다."
    
    return {
        "name": name,
        "family_name": family,
        "given_name": given,
        "meanings": given_meanings,
        "interpretation": interpretation
    }

@mcp.tool
def suggest_name_keywords() -> dict:
    """
    이름 생성에 사용할 수 있는 키워드들을 카테고리별로 제안합니다.
    
    Returns:
        dict: 카테고리별 키워드 목록
    """
    return {
        "categories": {
            "자연/계절": ["봄", "여름", "가을", "겨울", "바다", "산", "달", "별"],
            "감정/성격": ["용감", "똑똑", "귀여운", "재미", "차분", "활발"],
            "색깔": ["빨간", "파란", "노란", "하얀", "검은"],
            "취미/관심사": ["음악", "그림", "책", "운동", "요리", "게임"],
            "동물": ["고양이", "강아지", "토끼", "곰", "새"],
            "직업/꿈": ["의사", "선생님", "요리사", "예술가", "과학자"]
        },
        "styles": ["cute", "cool", "elegant", "funny", "traditional"],
        "usage_tip": "여러 카테고리의 키워드를 조합하면 더 독특한 이름을 만들 수 있습니다!"
    }

if __name__ == "__main__":
    mcp.run()
