import random

def get_destiny_place():
    database = {
        "신남": [
            ["성수동 팝업스토어", "에너지를 발산하기 딱 좋은 공간!", "팝업 스토어는 대기줄이 길 수 있으니 확인 필수!", "NewJeans - Hype Boy", "Avril Lavigne - Girlfriend"],
            ["홍대 버스킹 거리", "사람들의 열기 속에 섞여보세요.", "밤늦게 가면 더 활기차요!", "Britney Spears - Toxic", "도겸 - GO!"],
            ["전포 카페거리", "그림을 그리자!", "예쁜 소품샵도 같이 구경하세요.", "Chappell Roan - Pink Pony Club", "Lady Gaga - Abracadabra"] 
        ],
        "차분": [
            ["영도 절영해안산책로", "파도 소리를 들으며 생각을 정리해보세요.", "운동화 신고 걷는 걸 추천합니다.", "카더가든 - 밤새", "자우림 - 스물다섯, 스물하나"],
            ["북카페 문장", "책 냄새와 커피 향이 마음을 달래줄 거예요.", "조용한 대화는 매너!", "10CM - 이 밤을 빌려 말해요", "검정치마 - EVERYTHING"]
        ],
        "우울": [
            ["심야 영화관", "어둠 속에서 영화에 몰입하며 기분 전환을!", "가끔 혼자 영화를 보는 것도 좋아요.", "박효신 - 눈의 꽃"],
            ["코인 노래방", "크게 소리 지르며 감정을 쏟아내 보세요.", "목 아프지 않게 물 챙기기!", "데이식스 - 한 페이지가 될 수 있게", "Akeboshi - Wind", "Billie Eilish - BIRDS OF A FEATHER"]
        ]
    }

    print("🔮 당신의 데이터를 분석하여 운명의 장소를 찾습니다.")
    
    mood = input("지금 기분은 어떠신가요? (신남/차분/우울): ")
    weather = input("바깥 날씨는 어떤가요? (맑음/비/흐림): ")
    with_who = input("누구와 함께인가요? (혼자/친구/연인/부모님/친구들): ")

    if mood in database:
        place_info = random.choice(database[mood])
        
        name = place_info[0]
        reason = place_info[1]
        special_guide = place_info[2]  # 무조건 2번 위치는 '추가 멘트'로 고정!
        
        # 3번 위치부터 끝까지가 진짜 '노래 리스트'
        music_list = place_info[3:]
        lucky_music = random.choice(music_list)

        advice = f"📌 팁: {special_guide}" # 데이터에서 가져온 팁
        if weather == "비":
            advice += " ☔ 비가 오니 우산을 꼭 챙기세요!"
        if with_who == "혼자":
            advice += " 🎧 혼자만의 시간을 온전히 즐기기 좋은 곳입니다."

        print("\n" + "✨" * 20)
        print(f"📍 추천 장소: {name}")
        print(f"📝 선정 이유: {reason}")
        print(f"🎵 오늘의 운명곡: {lucky_music}")
        print(f"💡 가이드: {advice}")
        print("✨" * 20)
    else:
        print("\n데이터를 수집 중이에요!")

get_destiny_place()