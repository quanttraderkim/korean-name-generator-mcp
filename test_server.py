#!/usr/bin/env python3
"""
MCP 서버 테스트 스크립트
"""

import json
import subprocess
import sys
from typing import Dict, Any

def test_mcp_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """MCP 도구를 테스트하는 함수"""
    
    # MCP 요청 구성
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    
    try:
        # MCP 서버 프로세스 시작
        process = subprocess.Popen(
            [sys.executable, "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 초기화 요청
        init_request = {
            "jsonrpc": "2.0",
            "id": 0,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }
        
        # 초기화 요청 전송
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # 초기화 응답 읽기
        init_response = process.stdout.readline()
        print(f"초기화 응답: {init_response.strip()}")
        
        # 도구 목록 요청
        tools_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list"
        }
        
        process.stdin.write(json.dumps(tools_request) + "\n")
        process.stdin.flush()
        
        tools_response = process.stdout.readline()
        print(f"도구 목록: {tools_response.strip()}")
        
        # 실제 도구 테스트
        process.stdin.write(json.dumps(request) + "\n")
        process.stdin.flush()
        
        response = process.stdout.readline()
        print(f"도구 응답: {response.strip()}")
        
        # 프로세스 종료
        process.stdin.close()
        process.terminate()
        process.wait()
        
        return json.loads(response) if response else {}
        
    except Exception as e:
        print(f"테스트 중 오류 발생: {e}")
        return {}

def main():
    """메인 테스트 함수"""
    print("=== Korean Name Generator MCP 서버 테스트 ===\n")
    
    # 테스트 케이스들
    test_cases = [
        {
            "name": "generate_korean_name",
            "args": {
                "keywords": ["봄", "귀여운"],
                "style": "cute",
                "count": 3
            }
        },
        {
            "name": "get_name_meaning", 
            "args": {
                "name": "김봄이"
            }
        },
        {
            "name": "suggest_name_keywords",
            "args": {}
        }
    ]
    
    for test_case in test_cases:
        print(f"테스트: {test_case['name']}")
        print(f"인수: {test_case['args']}")
        result = test_mcp_tool(test_case['name'], test_case['args'])
        print(f"결과: {json.dumps(result, ensure_ascii=False, indent=2)}")
        print("-" * 50)

if __name__ == "__main__":
    main()

