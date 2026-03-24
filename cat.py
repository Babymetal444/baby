import random

def get_destiny_place():
    database = {
        "신남": [
            ["팝업스토어", "에너지를 발산하기 딱 좋은 공간!", "팝업 스토어는 대기줄이 길 수 있으니 확인 필수!", "NewJeans - Hype Boy", "Avril Lavigne - Girlfriend"],
            ["서면 ", "사람들의 열기 속에 섞여보세요.", "밤늦게 가면 더 활기차요!", "Britney Spears - Toxic", "도겸 - GO!"],
            ["전포 카페거리", "맛있는 디저트는 어때요 !", "예쁜 소품샵도 같이 구경하세요.", "Chappell Roan - Pink Pony Club", "Lady Gaga - Abracadabra"] 
        ],
        "차분": [
            ["집", "집에서 영화라도 볼까요?", "집 청소를 해봐요!!", "카더가든 - 밤새", "자우림 - 스물다섯, 스물하나"],
            ["북카페 문장", "책 냄새와 커피 향이 마음을 달래줄 거예요.", "조용한 대화는 매너!", "10CM - 이 밤을 빌려 말해요", "검정치마 - EVERYTHING"]
        ],
        "우울": [
            ["심야 영화관", "어둠 속에서 영화에 몰입하며 기분 전환을!", "가끔 혼자 영화를 보는 것도 좋아요.", "박효신 - 눈의 꽃", "이하이 - 한숨"],
            ["코인 노래방", "크게 소리 지르며 감정을 쏟아내 보세요.", "목 아프지 않게 물 챙기기!", "데이식스 - 한 페이지가 될 수 있게", "Billie Eilish - BIRDS OF A FEATHER"]
        ],
        "화남": [
            ["떡볶이 맛집", "강렬한 매운맛으로 스트레스를 날려버리세요!", "쿨피스 주문은 필수입니다.", "Marilyn Manson - The Fight Song", "Korn - A.D.I.D.A.S."],
            ["야구 연습장", "배트를 휘두르며 답답함을 타격해 보세요!", "장갑을 끼면 손이 덜 아파요.", "Limp Bizkit - Hot Dog", "Rob Zombie - Living Dead Girl"]
        ],
        "설렘": [
            ["해운대 달맞이길", "낭만적인 풍경과 함께 설레는 마음을 만끽하세요.", "일몰 시간대에 가면 분위기가 최고예요.", "백아 - 첫사랑", "Bruno Mars - Just the Way You Are"],
            ["테마파크 관람차", "높은 곳에서 내려다보는 풍경이 심장을 더 뛰게 할 거예요.", "사진 찍기 좋은 명당을 찾아보세요.", "Gym Class Heroes -Stereo Hearts", "Taylor Swift - Love Story"]
        ]
    }

    print("🔮 당신의 데이터를 분석하여 운명의 장소를 찾습니다.")
    
    # 선택지 안내에 새로운 감정 추가
    mood = input("지금 기분은 어떠신가요? (신남/차분/우울/화남/설렘): ")
    weather = input("바깥 날씨는 어떤가요? (맑음/비/흐림): ")
    with_who = input("누구와 함께인가요? (혼자/친구/연인/부모님/친구들): ")

    if mood in database:
        place_info = random.choice(database[mood])
        
        name = place_info[0]
        reason = place_info[1]
        special_guide = place_info[2]
        
        music_list = place_info[3:]
        lucky_music = random.choice(music_list)

        advice = f"📌 팁: {special_guide}"
        if weather == "비":
            advice += " ☔ 비가 오니 이동할 때 우산을 꼭 챙기세요!"
        if with_who == "혼자":
            advice += " 🎧 혼자만의 시간을 온전히 즐기기 좋은 곳입니다."

        print("\n" + "✨" * 25)
        print(f"📍 추천 장소: {name}")
        print(f"📝 선정 이유: {reason}")
        print(f"🎵 오늘의 운명곡: {lucky_music}")
        print(f"💡 가이드: {advice}")
        print("✨" * 25)
    else:
        print("\n아직 그 감정에 맞는 장소는 준비 중이에요. 조금만 기다려주세요!")

get_destiny_place()