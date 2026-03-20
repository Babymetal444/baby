def analyze_emotion():
    print("🤖 AI 감정 분석기를 시작합니다 (종료하려면 'exit' 입력)")
    
    # 1. 긍정/부정 단어 사전 (우리가 직접 정해주는 거예요!)
    good_words = ["행복", "기쁨", "좋아", "최고", "성공", "감사", "사랑"]
    bad_words = ["슬픔", "화나", "짜증", "실패", "우울", "나빠", "힘들어"]

    while True:
        sentence = input("\n분석할 문장을 입력하세요: ")
        
        if sentence == "exit":
            break
            
        # 2. 점수 계산하기
        score = 0
        for word in good_words:
            if word in sentence:
                score += 1
        for word in bad_words:
            if word in sentence:
                score -= 1
        
        # 3. 결과 보여주기 (트렌디한 이모지 활용!)
        print("-" * 30)
        if score > 0:
            print(f"✨ 결과: 이 문장은 '긍정적({score}점)'이네요! 기분 좋은 하루인가요? 😊")
        elif score < 0:
            print(f"☁️ 결과: 이 문장은 '부정적({score}점)'이군요. 토닥토닥, 힘내세요. ☕")
        else:
            print("😐 결과: 아주 평온하거나 중립적인 문장이네요.")
        print("-" * 30)

analyze_emotion()