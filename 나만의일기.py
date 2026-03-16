import datetime

def write_diary():
    # 1. 오늘 날짜 가져오기
    now = datetime.datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    
    print(f"--- {today_date} 일기 쓰기 ---")
    
    # 2. 내용 입력받기
    content = input("오늘 하루는 어땠나요? 내용을 입력하세요:\n")
    
    # 3. 파일 저장 (들여쓰기 주의!)
    with open("my_diary.txt", "a", encoding="utf-8") as file:
        file.write(f"\n[날짜: {today_date}]\n")
        file.write(content + "\n")
        file.write("-" * 20 + "\n")
    
    print("\n✅ 일기가 성공적으로 저장되었습니다!")

# 4. 프로그램 실행 (이 줄이 있어야 실제로 작동합니다!)
write_diary()
