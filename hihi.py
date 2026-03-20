import datetime

def run_account_book():
    print("💰 나만의 미니 용돈 기입장 💰")
    
    # 1. 날짜와 내역 입력받기
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    item = input("내역을 입력하세요 (예: 편의점, 용돈): ")
    
    # 2. 금액 입력받기 (중요: input은 글자이므로 int로 숫자로 바꿔줘야 해요!)
    amount = int(input("금액을 입력하세요 (숫자만): "))
    
    # 3. 수입인지 지출인지 선택하기
    category = input("1.수입(+)  2.지출(-) : ")
    
    if category == "1":
        type_str = "수입"
        display_amount = f"+{amount}"
    else:
        type_str = "지출"
        display_amount = f"-{amount}"

    # 4. 파일에 저장하기
    with open("account.txt", "a", encoding="utf-8") as file:
        file.write(f"[{today}] {item} | {type_str} : {display_amount}원\n")
    
    print(f"\n✅ {item} 내역이 저장되었습니다! ({display_amount}원)")

# 실행
run_account_book()