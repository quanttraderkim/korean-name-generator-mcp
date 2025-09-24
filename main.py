"""
키워드 기반 한국 이름 생성 MCP 서버
"""

from fastmcp import FastMCP
import random
from typing import List, Dict, Any

# Create server
mcp = FastMCP("KoreanNameGenerator")

@mcp.tool
def generate_korean_name(keywords: List[str], style: str = "cute", count: int = 5) -> Dict[str, Any]:
    """키워드 기반으로 한국 이름을 생성합니다.
    
    Args:
        keywords: 이름에 포함할 키워드 리스트
        style: 이름 스타일 (cute, cool, elegant, funny, traditional)
        count: 생성할 이름 개수 (1-10)
    
    Returns:
        dict: 생성된 이름들과 설명
    """
    # 스타일별 이름 요소들
    name_elements = {
        "cute": {
            "male": ["봄", "별", "달", "꽃", "나무", "물", "바람", "구름", "비", "눈"],
            "female": ["희", "미", "예", "연", "주", "은", "금", "옥", "진", "란"]
        },
        "cool": {
            "male": ["대", "태", "준", "호", "석", "철", "영", "수", "원", "진"],
            "female": ["현", "지", "유", "경", "민", "정", "화", "원", "영", "혜"]
        },
        "elegant": {
            "male": ["지", "혜", "선", "정", "의", "용", "성", "민", "현", "인"],
            "female": ["숙", "자", "라", "리", "나", "다", "사", "아", "야", "윤"]
        },
        "funny": {
            "male": ["동", "우", "찬", "빈", "범", "택", "근", "배", "식", "규"],
            "female": ["솔", "별", "달", "슬", "늘", "온", "참", "샘", "림", "애"]
        },
        "traditional": {
            "male": ["왕", "신", "사", "공", "후", "군", "상", "장", "조", "석"],
            "female": ["백", "청", "홍", "금", "은", "황", "흑", "적", "록", "자"]
        }
    }
    
    # 성씨 리스트
    surnames = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권", "황", "안", "송", "전", "고"]
    
    # 키워드 매칭을 위한 의미사전
    keyword_meanings = {
        "봄": "생명력, 희망, 새로운 시작",
        "여름": "열정, 활력, 따뜻함",  
        "가을": "결실, 성숙, 풍요",
        "겨울": "순수, 깨끗함, 인내",
        "해": "밝음, 희망, 빛",
        "달": "아름다움, 신비, 평온",
        "별": "소원, 꿈, 빛남",
        "꽃": "아름다움, 사랑, 순수",
        "나무": "성장, 견고함, 생명력",
        "물": "순수함, 유연함, 생명",
        "바다": "넓은 마음, 포용력, 깊이",
        "산": "의지, 굳건함, 높은 뜻",
        "강": "흐름, 지속성, 역동성",
        "바람": "자유로움, 시원함, 변화",
        "구름": "자유로움, 몽환적, 순수",
        "비": "은혜, 축복, 새로움",
        "눈": "순결, 깨끗함, 아름다움",
        "귀여운": "사랑스러움, 순수함",
        "멋진": "훌륭함, 뛰어남",
        "예쁜": "아름다움, 우아함",
        "강한": "힘, 의지력",
        "똑똑한": "지혜, 총명함",
        "착한": "선함, 올바름"
    }
    
    # 생성할 이름 개수 제한
    count = max(1, min(count, 10))
    
    generated_names = []
    
    for i in range(count):
        # 성씨 선택
        surname = random.choice(surnames)
        
        # 키워드에 맞는 이름 요소 선택
        if keywords:
            # 키워드와 매칭되는 요소 찾기
            matching_elements = []
            for keyword in keywords:
                if keyword in keyword_meanings:
                    # 키워드 의미에 맞는 요소들 찾기
                    for gender_elements in name_elements[style].values():
                        for element in gender_elements:
                            if keyword in keyword_meanings[element] if element in keyword_meanings else False:
                                matching_elements.append(element)
            
            if matching_elements:
                name_element = random.choice(matching_elements)
            else:
                # 매칭되는 요소가 없으면 스타일에 맞는 요소 선택
                all_elements = name_elements[style]["male"] + name_elements[style]["female"]
                name_element = random.choice(all_elements)
        else:
            # 키워드가 없으면 스타일에 맞는 요소 선택
            all_elements = name_elements[style]["male"] + name_elements[style]["female"]
            name_element = random.choice(all_elements)
        
        # 이름 생성 (1-2글자)
        if random.choice([True, False]):
            # 1글자 이름
            full_name = surname + name_element
        else:
            # 2글자 이름
            all_elements = name_elements[style]["male"] + name_elements[style]["female"]
            second_element = random.choice(all_elements)
            full_name = surname + name_element + second_element
        
        # 이름 설명 생성
        keyword_desc = ", ".join(keywords) if keywords else "일반적인"
        name_desc = f"'{keyword_desc}' 키워드와 '{style}' 스타일로 생성된 이름"
        
        generated_names.append({
            "name": full_name,
            "description": name_desc,
            "style": style,
            "keywords": keywords
        })
    
    return {
        "generated_names": generated_names,
        "total_count": len(generated_names),
        "style": style,
        "keywords": keywords,
        "message": f"'{style}' 스타일로 {len(generated_names)}개의 이름을 생성했습니다."
    }

@mcp.tool  
def get_name_meaning(name: str) -> Dict[str, Any]:
    """한국 이름의 가능한 의미를 해석합니다.
    
    Args:
        name: 해석할 한국 이름
        
    Returns:
        dict: 이름의 의미 해석과 설명
    """
    # 한글 글자별 의미 사전 (대폭 확장)
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
        "나무": "성장, 견고함, 생명력",
        "물": "순수함, 유연함, 생명",
        "바다": "넓은 마음, 포용력, 깊이",
        "산": "의지, 굳건함, 높은 뜻",
        "강": "흐름, 지속성, 역동성",
        "바람": "자유로움, 시원함, 변화",
        "구름": "자유로움, 몽환적, 순수",
        "비": "은혜, 축복, 새로움",
        "눈": "순결, 깨끗함, 아름다움",
        
        # 덕목 관련
        "지": "지혜, 총명함, 슬기로움",
        "혜": "은혜, 자비로움, 지혜", 
        "선": "선함, 착함, 올바름",
        "정": "정직, 바름, 올곧음",
        "의": "의로움, 정의, 올바름",
        "용": "용기, 용맹함, 드래곤",
        "성": "성실함, 진실함, 별",
        "민": "민첩함, 영민함, 백성",
        "현": "현명함, 지혜로움, 어질다",
        "인": "어질다, 사람다움, 인자함",
        "효": "효도, 부모님 사랑",
        "충": "충성심, 진실함",
        "예": "예의, 공손함, 아름다움",
        "신": "믿음, 신뢰, 신실함",
        "겸": "겸손함, 겸양",
        "관": "관찰력, 넓은 시야",
        "경": "공경, 존경, 조심",
        "순": "순수함, 순진함, 따름",
        "온": "온화함, 따뜻함",
        "화": "화목, 평화, 꽃",
        "평": "평화, 평온함",
        "안": "평안함, 안전함",
        
        # 일반적 남성 이름 요소
        "대": "큰, 위대한, 크다",
        "태": "큰, 태양, 위대한",
        "준": "높은, 준수한, 기준",
        "호": "큰, 넓은, 호수",
        "석": "바위, 견고함, 돌",
        "철": "쇠, 의지, 견고함",
        "영": "영원함, 빛남, 영광",
        "수": "물, 맑음, 오래삶, 뛰어남",
        "원": "원만함, 둥글음, 근원",
        "진": "진실, 참된, 나아감",
        "건": "건강, 튼튼함, 세움",
        "강": "강함, 굳셈, 강물",
        "혁": "변화, 개혁, 가죽",
        "훈": "가르침, 훈련, 공훈",
        "환": "환한, 밝은, 즐거운",
        "완": "완전함, 마무리",
        "창": "창조, 창문, 창",
        "섭": "잡다, 대신하다, 섭정",
        "규": "규칙, 법도, 둥근",
        "식": "먹다, 심다, 알다",
        "근": "뿌리, 근본, 근면",
        "배": "배우다, 베풀다, 배",
        "동": "움직임, 동쪽, 어린이",
        "우": "비, 오른쪽, 도움",
        "찬": "칭찬, 찬양, 차가운",
        "빈": "빈틈없는, 손님",
        "범": "범위, 호랑이, 법",
        "택": "선택, 택하다",
        
        # 일반적 여성 이름 요소  
        "희": "희망, 기쁨, 밝음",
        "미": "아름다움, 미소",
        "예": "예쁨, 우아함, 예술",
        "연": "연꽃, 이어짐, 부드러움",
        "주": "구슬, 붉은색, 주인",
        "은": "은색, 고귀함, 은혜",
        "금": "금, 귀함, 소중함",
        "옥": "옥, 보석, 아름다움",
        "진": "진주, 진실, 귀함",
        "란": "난초, 우아함",
        "매": "매화, 아름다움",
        "국": "나라, 국화",
        "영": "꽃잎, 영원, 영특함",
        "숙": "숙녀, 어른스러움",
        "자": "자녀, 사랑, 자다",
        "라": "나팔, 소라",
        "리": "리듬, 이치",
        "나": "나, 자신",
        "다": "많다, 다양함",
        "사": "넷, 사랑",
        "아": "아름다움, 아기",
        "야": "밤, 들",
        "윤": "윤기, 윤택함",
        "서": "서쪽, 시원함, 책",
        "하": "하늘, 아래, 큰",
        "혜": "지혜, 은혜",
        "지": "지혜, 의지",
        "유": "흐름, 있음, 놀다",
        "경": "경치, 경험, 공경",
        "민": "민첩, 백성",
        "정": "정성, 바름",
        "화": "꽃, 화목",
        "원": "원만, 소원",
        "현": "현명함, 현실",
        "영": "영원, 영광",
        "혜": "은혜, 지혜",
        "진": "진실, 진주",
        "선": "선함, 착함",
        "미": "아름다움, 미소",
        "수": "물, 뛰어남",
        "은": "은혜, 은색",
        "애": "사랑, 애정",
        "림": "숲, 나무들",
        "빈": "빈틈없는, 완전한",
        "솔": "소나무, 솔직함",
        "별": "별, 특별함",
        "달": "달, 다다름",
        "슬": "슬기, 지혜",
        "늘": "항상, 늘",
        "온": "온전함, 따뜻함",
        "참": "참, 진실",
        "샘": "샘물, 근원",
        "봄": "봄, 생명력",
        "가을": "가을, 결실",
        "겨울": "겨울, 순수",
        "여름": "여름, 열정",
        
        # 색깔/외모 관련
        "백": "하얀색, 순수함",
        "청": "파란색, 맑음", 
        "홍": "빨간색, 열정",
        "금": "황금색, 귀함",
        "은": "은색, 고귀함",
        "황": "황금, 노란색",
        "흑": "검은색, 깊이",
        "적": "빨간색, 열정",
        "록": "녹색, 자연",
        "자": "자주색, 고귀함",
        
        # 직업/지위 관련
        "왕": "임금, 왕",
        "신": "신하, 믿음",
        "사": "선비, 사람",
        "공": "공적, 공평함",
        "후": "뒤, 후손",
        "군": "군자, 임금",
        "상": "위, 높음",
        "장": "기다림, 어른",
        
        # 시간 관련
        "조": "아침, 이른",
        "석": "저녁, 바위",
        "야": "밤, 들판",
        "춘": "봄",
        "하": "여름",
        "추": "가을", 
        "동": "겨울",
        
        # 방향 관련
        "동": "동쪽",
        "서": "서쪽", 
        "남": "남쪽",
        "북": "북쪽",
        "중": "가운데"
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
                # 사전에 없는 글자는 추측해서 의미 부여
                given_meanings.append(f"{char}: 고유한 의미를 담은 특별한 글자")
    else:
        family = ""
        given = name
        given_meanings = [f"{name}: 독특하고 특별한 이름"]
    
    # 전체 해석 생성
    if given_meanings:
        meaning_parts = [meaning.split(': ')[1] for meaning in given_meanings]
        interpretation = f"'{name}'은(는) " + ", ".join(meaning_parts) + "을(를) 의미하는 아름다운 이름입니다."
    else:
        interpretation = f"'{name}'은(는) 특별한 의미를 담은 아름다운 이름입니다."
    
    return {
        "name": name,
        "family_name": family,
        "given_name": given,
        "meanings": given_meanings,
        "interpretation": interpretation
    }

@mcp.tool
def suggest_name_keywords() -> Dict[str, Any]:
    """이름 생성에 사용할 수 있는 키워드들을 제안합니다.
    
    Returns:
        dict: 카테고리별 키워드 목록
    """
    keywords = {
        "자연": ["봄", "여름", "가을", "겨울", "해", "달", "별", "꽃", "나무", "물", "바다", "산", "강", "바람", "구름", "비", "눈"],
        "성격": ["귀여운", "멋진", "예쁜", "강한", "똑똑한", "착한", "용감한", "친절한", "밝은", "따뜻한"],
        "색깔": ["빨간", "파란", "노란", "초록", "보라", "하얀", "검은", "금색", "은색"],
        "감정": ["기쁜", "행복한", "사랑스러운", "평화로운", "희망적인", "즐거운"],
        "직업": ["의사", "선생님", "화가", "음악가", "작가", "과학자", "운동선수"],
        "동물": ["호랑이", "사자", "독수리", "돌고래", "나비", "토끼", "강아지", "고양이"]
    }
    
    return {
        "keyword_categories": keywords,
        "total_keywords": sum(len(words) for words in keywords.values()),
        "message": "이름 생성에 사용할 수 있는 키워드들을 카테고리별로 정리했습니다."
    }

if __name__ == "__main__":
    mcp.run()