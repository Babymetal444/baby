import random

def play_game():
    options = ["가위", "바위", "보"]
    print("🎮 가위바위보 게임을 시작합니다!")
    
    while True:
        computer = random.choice(options)
        user = input("\n가위, 바위, 보 중 하나를 입력하세요 (그만하려면 '종료'): ")
        
        if user == "종료":
            print("게임을 종료합니다. 다음에 또 봐요!")
            break
            
        if user not in options:
            print("⚠️ 잘못된 입력입니다. 다시 입력해 주세요.")
            continue
            
        print(f"컴퓨터: {computer} VS 당신: {user}")
        
        if user == computer:
            print("🤝 비겼습니다!")
        elif (user == "가위" and computer == "보") or \
             (user == "바위" and computer == "가위") or \
             (user == "보" and computer == "바위"):
            print("🎉 당신이 이겼습니다!")
        else:
            print("💀 컴퓨터가 이겼습니다!")

play_game()