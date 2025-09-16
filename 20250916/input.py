# -*- coding: utf-8 -*-

import os
import time

def clear_screen():
    """화면을 지우는 함수"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_gugudan(dan):
    """구구단을 출력하는 함수"""
    print(f"\n{'='*30}")
    print(f"          [{dan}단]")
    print(f"{'='*30}")
    
    for i in range(1, 10):
        result = dan * i
        print(f"    {dan} × {i} = {result}")
    
    print(f"{'='*30}")

def main():
    """메인 함수"""
    while True:
        try:
            clear_screen()  # 화면 지우기
            
            print("🔢 구구단 프로그램")
            print("-" * 20)
            print("2부터 9까지의 숫자를 입력하세요.")
            print("프로그램을 종료하려면 'q' 또는 '종료'를 입력하세요.")
            print()
            
            # 사용자 입력 받기
            user_input = input("구구단 수를 입력하세요: ").strip()
            
            # 종료 조건 확인
            if user_input.lower() in ['q', 'quit', 'exit', '종료']:
                clear_screen()
                print("구구단 프로그램을 종료합니다. 안녕히 가세요! 👋")
                break
            
            # 숫자 변환 시도
            dan = int(user_input)
            
            # 범위 확인
            if not (2 <= dan <= 9):
                print("\n❌ 2부터 9까지의 숫자만 입력 가능합니다.")
                input("Enter 키를 눌러 계속...")
                continue
            
            # 화면 지우고 구구단 출력
            clear_screen()
            print_gugudan(dan)
            
            # 결과를 보여주고 잠시 정지
            print("\n결과를 확인하세요...")
            print("계속하려면 Enter 키를 누르세요.")
            input()  # 사용자가 Enter를 누를 때까지 대기
            
        except ValueError:
            print(f"\n❌ '{user_input}'는 올바른 숫자가 아닙니다.")
            print("2부터 9까지의 숫자를 입력해주세요.")
            input("Enter 키를 눌러 계속...")
        
        except KeyboardInterrupt:
            print("\n\n프로그램이 중단되었습니다.")
            break

# 프로그램 실행
if __name__ == "__main__":
    main()