print("안녕하세요! 파이썬 공부를 시작합니다.")
import random  # 남이 만든 '랜덤' 도구 가져오기

import random

secret_number = random.randint(1, 100)
attempts = 0

print("★ 숫자 맞추기 게임 (안전 모드) ★")

while True:
    try:
        # 괄호 안의 내용을 먼저 실행하고, 에러가 나면 except로 점프합니다.
        guess = int(input("1~100 사이 숫자를 입력하세요: "))
    except ValueError:
        print("❌ 숫자가 아닌 것 같아요. 다시 입력해 주세요!")
        continue # 다시 위로 올라가서 숫자를 물어봅니다.

    attempts += 1

    if guess < secret_number:
        print("UP ↑")
    elif guess > secret_number:
        print("DOWN ↓")
    else:
        print(f"🎉 정답! {attempts}번 만에 성공!")
        break