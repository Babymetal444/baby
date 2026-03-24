import random

def get_destiny_place():
    database = {
        "신남": [
            ["성수동 팝업스토어", "에너지를 발산하기 딱 좋은 공간!", "NewJeans - Hype Boy", "Avril Lavigne - Girlfriend"],
            ["홍대 버스킹 거리", "사람들의 열기 속에 섞여보세요.", "Britney Spears - Toxic", "도겸 - GO!"],
            ["전포 카페거리", "그림을 그리자!", "Chappell Roan - Pink Pony Club", "Lady Gaga - Abracadabra"] 
        ],
        "차분": [
            ["영도 절영해안산책로", "파도 소리를 들으며 생각을 정리해보세요.", "카더가든 - 밤새", "자우림 - 스물다섯, 스물하나"],
            ["북카페 문장", "책 냄새와 커피 향이 마음을 달래줄 거예요.", "10CM - 이 밤을 빌려 말해요", "검정치마 - EVERYTHING"]
        ],
        "우울": [
            ["심야 영화관", "어둠 속에서 영화에 몰입하며 기분 전환을!", "영화 OST", "가끔 혼자 영화를 보는 것도 좋아요", "박효신 - 눈의 꽃"],
            ["코인 노래방", "크게 소리 지르며 감정을 쏟아내 보세요.", "데이식스 - 한 페이지가 될 수 있게", "Akeboshi - Wind", "Billie Eilish - BIRDS OF A FEATHER"]
        ]
    }

    print("🔮 당신의 데이터를 분석하여 운명의 장소를 찾습니다.")
    
    mood = input("지금 기분은 어떠신가요? (신남/차분/우울): ")
    weather = input("바깥 날씨는 어떤가요? (맑음/비/흐림): ")
    with_who = input("누구와 함께인가요? (혼자/친구/연인/부모님/친구들): ")

    if mood in database:
        place_info = random.choice(database[mood])
        
        # 수정된 부분: 인덱스(순서)를 사용해 안전하게 가져오기
        name = place_info[0]
        reason = place_info[1]
        
        # 추천 음악이 여러 개일 수 있으므로, 2번 인덱스부터 끝까지 다 가져오기
        all_music = place_info[2:] 
        music_display = ", ".join(all_music) # 여러 곡을 쉼표로 연결

        advice = ""
        if weather == "비":
            advice = "☔ 비가 오니 이동할 때 우산을 꼭 챙기세요!"
        if with_who == "혼자":
            advice += " 🎧 혼자만의 시간을 온전히 즐기기 좋은 곳입니다."

        print("\n" + "✨" * 20)
        print(f"📍 추천 장소: {name}")
        print(f"📝 선정 이유: {reason}")
        print(f"🎵 추천 배경음: {music_display}") # 모든 음악 리스트 출력
        print(f"💡 가이드: {advice}")
        print("✨" * 20)
    else:
        print("\n죄송합니다. 그 기분에 맞는 데이터는 아직 수집 중이에요!")

get_destiny_place()