import streamlit as st
import random

# ─── 페이지 설정 ───────────────────────────────────────────
st.set_page_config(
    page_title="🔮 MBTI 포켓몬 매칭",
    page_icon="🎮",
    layout="centered",
)

# ─── CSS 스타일링 ──────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Galmuri11&family=Noto+Sans+KR:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}

/* 배경 */
.stApp {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 25%, #a8edea 50%, #fed6e3 75%, #d299c2 100%);
    background-size: 400% 400%;
    animation: gradientShift 8s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* 메인 카드 */
.main-card {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(20px);
    border-radius: 28px;
    padding: 2.5rem 2rem;
    box-shadow: 0 20px 60px rgba(0,0,0,0.12), 0 0 0 1px rgba(255,255,255,0.6);
    margin: 1rem 0;
    text-align: center;
}

/* 타이틀 */
.title-box {
    background: linear-gradient(135deg, #ff6b9d, #c44dff, #4facfe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2.8rem;
    font-weight: 900;
    line-height: 1.2;
    margin-bottom: 0.3rem;
}

.subtitle {
    color: #888;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}

/* MBTI 버튼 그리드 */
.mbti-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin: 1.5rem 0;
}

.mbti-btn {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 6px;
    font-size: 0.9rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.25s ease;
    font-family: 'Noto Sans KR', sans-serif;
    box-shadow: 0 4px 12px rgba(102,126,234,0.35);
}

.mbti-btn:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 20px rgba(102,126,234,0.5);
}

/* 결과 카드 */
.result-card {
    background: linear-gradient(135deg, #f8f9ff, #fff0f8);
    border-radius: 24px;
    padding: 2rem;
    margin: 1.5rem 0;
    border: 2px solid rgba(200, 150, 255, 0.3);
    text-align: center;
    animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes popIn {
    0% { transform: scale(0.8); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}

.pokemon-name {
    font-size: 2rem;
    font-weight: 900;
    background: linear-gradient(135deg, #ff6b9d, #c44dff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.pokemon-img {
    border-radius: 16px;
    background: radial-gradient(circle, rgba(255,255,255,0.9), rgba(240,230,255,0.5));
    padding: 16px;
    display: inline-block;
}

.mbti-badge {
    display: inline-block;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 6px 20px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 1rem;
    box-shadow: 0 4px 15px rgba(102,126,234,0.4);
}

.trait-chip {
    display: inline-block;
    background: linear-gradient(135deg, #ffecd2, #fcb69f);
    color: #c05000;
    padding: 4px 14px;
    border-radius: 50px;
    font-size: 0.82rem;
    font-weight: 600;
    margin: 3px;
}

.reason-box {
    background: rgba(255,255,255,0.7);
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    font-size: 0.95rem;
    color: #444;
    line-height: 1.8;
    text-align: left;
    border-left: 4px solid #c44dff;
}

.fun-fact {
    background: linear-gradient(135deg, rgba(255,107,157,0.1), rgba(196,77,255,0.1));
    border-radius: 14px;
    padding: 0.8rem 1rem;
    margin-top: 1rem;
    font-size: 0.88rem;
    color: #666;
}

.stSelectbox > div > div {
    background: rgba(255,255,255,0.9) !important;
    border-radius: 14px !important;
    border: 2px solid rgba(196,77,255,0.3) !important;
    font-size: 1rem !important;
}

/* 섹션 헤더 */
.section-label {
    font-size: 1rem;
    color: #666;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.divider {
    border: none;
    border-top: 2px dashed rgba(196,77,255,0.2);
    margin: 1.5rem 0;
}

/* 반짝이 효과 */
.sparkle {
    display: inline-block;
    animation: sparkle 1.5s infinite;
}
@keyframes sparkle {
    0%, 100% { transform: scale(1) rotate(0deg); }
    50% { transform: scale(1.3) rotate(15deg); }
}

.footer {
    color: #bbb;
    font-size: 0.78rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)


# ─── 데이터 ────────────────────────────────────────────────
MBTI_POKEMON = {
    "INTJ": {
        "pokemon": "미뇽", "english": "Dratini",
        "number": 147,
        "emoji": "🐉",
        "reason": "INTJ는 혼자서도 강하고 장기적인 비전을 가진 전략가예요. 미뇽은 겉보기엔 순해 보이지만 드래곤족의 잠재력을 품고 조용히 자신만의 길을 걷죠. 언젠가 드래곤에어, 망나뇽으로 진화할 거라는 걸 미뇽 자신도 알고 있답니다. ✨",
        "traits": ["🧠 전략가", "🎯 목표지향", "🔮 통찰력", "🐺 독립적"],
        "fun_fact": "💡 미뇽은 용기와 인내를 상징해요. INTJ처럼 조용하지만 엄청난 힘을 숨기고 있답니다!",
        "type_color": "#6C5CE7"
    },
    "INTP": {
        "pokemon": "폴리곤", "english": "Porygon",
        "number": 137,
        "emoji": "💾",
        "reason": "INTP는 세상을 논리와 시스템으로 이해하는 분석가예요. 폴리곤은 세계 최초의 컴퓨터 프로그램으로 만들어진 포켓몬! 끊임없이 데이터를 처리하고 새로운 가능성을 탐구하는 모습이 INTP와 쏙 닮았어요. 🖥️",
        "traits": ["🔬 분석적", "💡 창의적", "📚 지식탐구", "🌌 이론가"],
        "fun_fact": "🤖 폴리곤은 사이버 공간에서도 자유롭게 이동할 수 있어요. INTP처럼 어떤 개념의 세계도 탐험하죠!",
        "type_color": "#74B9FF"
    },
    "ENTJ": {
        "pokemon": "리자몽", "english": "Charizard",
        "number": 6,
        "emoji": "🔥",
        "reason": "ENTJ는 타고난 리더로 강한 의지와 카리스마가 넘쳐요. 리자몽은 포켓몬 세계에서 가장 상징적인 리더 포켓몬! 자신만의 룰로 살며, 진정한 강자만 인정하는 그 고집스러운 자존심이 ENTJ와 완벽히 일치해요. 🏆",
        "traits": ["👑 리더십", "🔥 열정", "⚡ 결단력", "💼 목표달성"],
        "fun_fact": "🦅 리자몽은 약한 상대와는 싸우지 않아요. ENTJ처럼 언제나 최고를 추구한답니다!",
        "type_color": "#FF7675"
    },
    "ENTP": {
        "pokemon": "게으킹", "english": "Snorlax",
        "number": 143,
        "emoji": "😴",
        "reason": "잠깐, 게으킹이라고 무시하면 안 돼요! ENTP는 즉흥적이고 재치있으며 아이디어가 샘솟죠. 게으킹은 겉으론 느긋해 보이지만 배우기 싫어하는 기술이 없는 만능 포켓몬! 그 여유로운 자신감과 폭발적인 잠재력이 ENTP 그 자체예요. 💥",
        "traits": ["⚡ 즉흥적", "🎭 재치있음", "🌀 아이디어뱅크", "😎 자신감"],
        "fun_fact": "🍖 게으킹의 위장은 3주 동안 먹지 않아도 버틸 수 있어요. ENTP처럼 에너지를 폭발적으로 쓰죠!",
        "type_color": "#FDCB6E"
    },
    "INFJ": {
        "pokemon": "뮤츠", "english": "Mewtwo",
        "number": 150,
        "emoji": "🔮",
        "reason": "INFJ는 깊은 통찰력과 강한 신념을 가진 이상주의자예요. 뮤츠는 세계 최강의 포켓몬이지만 그 힘을 함부로 쓰지 않고, 자신의 존재 의미와 사명을 끊임없이 탐구해요. 그 고독한 심층의 깊이가 INFJ와 닮았답니다. 🌌",
        "traits": ["🌟 통찰력", "💜 이상주의", "🔮 예지력", "🕊️ 사명감"],
        "fun_fact": "✨ 뮤츠는 인간의 말을 텔레파시로 이해해요. INFJ처럼 말하지 않아도 상대방의 감정을 느끼죠!",
        "type_color": "#A29BFE"
    },
    "INFP": {
        "pokemon": "이브이", "english": "Eevee",
        "number": 133,
        "emoji": "🦊",
        "reason": "INFP는 가능성이 무궁무진하고 감수성이 풍부한 몽상가예요. 이브이는 무려 8가지 진화 방향을 가진 유일한 포켓몬! 어떤 길을 선택하느냐에 따라 완전히 다른 존재가 되는 무한한 가능성이 INFP의 영혼과 꼭 닮았어요. 🌈",
        "traits": ["🌸 감수성", "🎨 창의력", "💭 몽상가", "🌈 가능성"],
        "fun_fact": "💫 이브이의 DNA는 불안정해서 환경에 따라 다르게 진화해요. INFP처럼 주변과의 감정적 연결이 성장을 결정하죠!",
        "type_color": "#FD79A8"
    },
    "ENFJ": {
        "pokemon": "피카츄", "english": "Pikachu",
        "number": 25,
        "emoji": "⚡",
        "reason": "ENFJ는 사람들에게 에너지와 영감을 주는 타고난 조력자예요. 피카츄는 전 세계 포켓몬의 얼굴이자 모두에게 사랑받는 존재! 밝은 에너지로 주변 모두를 행복하게 만드는 그 능력이 ENFJ와 완벽히 맞아요. ⚡💛",
        "traits": ["💛 따뜻함", "⚡ 에너지", "🤝 리더십", "❤️ 공감능력"],
        "fun_fact": "🌟 피카츄는 꼬리로 다른 피카츄에게 전기를 보내 인사해요. ENFJ처럼 언제나 연결을 중요시하죠!",
        "type_color": "#FFEAA7"
    },
    "ENFP": {
        "pokemon": "야도란", "english": "Slowbro",
        "number": 80,
        "emoji": "🌀",
        "reason": "ENFP는 열정적이고 자유로운 영혼의 소유자! 야도란은 늘 느긋하게 자기 페이스로 살지만 한번 영감이 떠오르면 천재적인 번뜩임을 보여줘요. 그 예측불가능한 매력과 독특한 시각이 ENFP 그 자체랍니다. 🌊",
        "traits": ["🌈 자유로움", "✨ 열정", "🎪 독창성", "💫 낙천적"],
        "fun_fact": "🐚 야도란의 꼬리를 무는 야돈 덕분에 야도란이 된대요. ENFP처럼 우연한 만남이 인생을 바꾸죠!",
        "type_color": "#81ECEC"
    },
    "ISTJ": {
        "pokemon": "잉어킹→갸라도스", "english": "Magikarp",
        "number": 129,
        "emoji": "🐟",
        "reason": "ISTJ는 묵묵히 자신의 역할을 다하며 신뢰를 쌓는 성실의 아이콘이에요. 잉어킹은 처음엔 아무것도 못 하지만, 포기하지 않고 레벨을 쌓아 결국 갸라도스라는 최강 포켓몬이 되죠. 그 꾸준함과 책임감이 ISTJ와 딱 맞아요! 💪",
        "traits": ["📋 성실함", "🏋️ 인내력", "🔒 신뢰성", "📏 원칙주의"],
        "fun_fact": "⚡ 갸라도스가 한번 날뛰기 시작하면 한 달은 멈추지 않는대요. ISTJ도 한번 결심하면 절대 안 멈추죠!",
        "type_color": "#0984E3"
    },
    "ISFJ": {
        "pokemon": "푸린", "english": "Jigglypuff",
        "number": 39,
        "emoji": "🎤",
        "reason": "ISFJ는 따뜻하고 헌신적이며 주변 사람을 보살피는 수호자예요. 푸린은 자신의 노래로 모두를 편안하게 잠들게 해주는 포켓몬! 때로는 화가 나도 결국 다시 노래를 부르는 그 헌신적인 사랑이 ISFJ와 닮았어요. 🌸",
        "traits": ["💗 헌신적", "🏠 보호본능", "🌺 따뜻함", "🤲 봉사정신"],
        "fun_fact": "😪 푸린의 노래는 수면 유도 효과가 있어요. ISFJ처럼 주변 사람들에게 안정감을 주는 존재죠!",
        "type_color": "#FF9FF3"
    },
    "ESTJ": {
        "pokemon": "거북왕", "english": "Blastoise",
        "number": 9,
        "emoji": "💧",
        "reason": "ESTJ는 규칙과 질서를 중요시하는 실용적인 관리자예요. 거북왕은 강력한 수압포와 단단한 껍질로 팀을 지키는 수비의 요새! 체계적이고 믿음직한 그 존재감이 ESTJ 리더십과 완벽히 일치해요. 🏛️",
        "traits": ["⚖️ 체계적", "🛡️ 책임감", "📊 실용적", "🏆 리더십"],
        "fun_fact": "💦 거북왕의 수압포는 빌딩도 뚫을 수 있어요. ESTJ처럼 한번 결정하면 어떤 장애물도 뚫어버리죠!",
        "type_color": "#0097A7"
    },
    "ESFJ": {
        "pokemon": "토게피", "english": "Togepi",
        "number": 175,
        "emoji": "🥚",
        "reason": "ESFJ는 사람들을 행복하게 만드는 것에 기쁨을 느끼는 배려의 천재예요. 토게피는 행복한 감정을 먹고 자라며 주변에 행복을 나눠주는 포켓몬! 그 순수한 선의와 따뜻함이 ESFJ와 꼭 닮았답니다. 🌟",
        "traits": ["❤️ 배려심", "🎉 사교적", "🌻 긍정적", "🤗 친화력"],
        "fun_fact": "✨ 토게피는 껍질 안에 행복을 저장한대요. ESFJ처럼 행복을 주변에 나눠주는 존재죠!",
        "type_color": "#FFBE76"
    },
    "ISTP": {
        "pokemon": "팬텀", "english": "Gengar",
        "number": 94,
        "emoji": "👻",
        "reason": "ISTP는 논리적이고 실용적이며 자기만의 방식으로 문제를 해결하는 장인이에요. 팬텀은 그림자 속에 숨어 자기만의 방식으로 행동하는 유령! 독립적이고 신비로운 존재감, 그리고 상황에 따라 순식간에 해결책을 찾는 모습이 ISTP와 닮았어요. 🌙",
        "traits": ["🔧 실용적", "🎯 집중력", "😏 독립적", "⚡ 순발력"],
        "fun_fact": "🌑 팬텀은 벽을 통과할 수 있어요. ISTP처럼 어떤 문제도 우회해서 해결하는 방법을 찾죠!",
        "type_color": "#6C5CE7"
    },
    "ISFP": {
        "pokemon": "뮤", "english": "Mew",
        "number": 151,
        "emoji": "✨",
        "reason": "ISFP는 온화하고 예술적이며 현재 순간을 즐기는 자유로운 영혼이에요. 뮤는 모든 포켓몬의 DNA를 가진 전설의 포켓몬이지만 항상 장난스럽고 순수해요. 자유롭게 세상을 탐험하며 모든 것과 조화를 이루는 그 감성이 ISFP와 딱 맞아요! 🌸",
        "traits": ["🎨 예술적", "🌸 온화함", "🦋 자유로움", "💫 감수성"],
        "fun_fact": "🔬 뮤는 모든 포켓몬 기술을 배울 수 있어요. ISFP처럼 어떤 예술적 표현도 가능한 무한한 잠재력을 가졌죠!",
        "type_color": "#FD79A8"
    },
    "ESTP": {
        "pokemon": "이상해씨→이상해꽃", "english": "Bulbasaur",
        "number": 1,
        "emoji": "🌱",
        "reason": "ESTP는 행동파 모험가로 위험을 즐기고 현실에 직접 부딪히는 스타일이에요! 이상해씨는 세 번의 진화를 거치며 점점 강해지는 포켓몬. 처음엔 수줍어 보이지만 실전에 강하고 전략적인 모습이 ESTP와 꼭 맞아요. 🌿💪",
        "traits": ["🚀 행동파", "😎 대담함", "🎲 위험감수", "💡 현실적"],
        "fun_fact": "☀️ 이상해꽃은 햇빛을 받으면 더 강해져요. ESTP처럼 실전 경험으로 쑥쑥 성장하죠!",
        "type_color": "#00B894"
    },
    "ESFP": {
        "pokemon": "파이리", "english": "Charmander",
        "number": 4,
        "emoji": "🔥",
        "reason": "ESFP는 삶을 파티처럼 즐기는 자유롭고 열정적인 엔터테이너예요! 파이리는 꼬리의 불꽃이 곧 생명력이에요. 언제나 불꽃처럼 뜨겁게 타오르며 주변을 밝히는 그 에너지가 ESFP의 매력과 완벽히 같아요. 🎉",
        "traits": ["🎉 즐거움", "❤️ 열정", "🎭 표현력", "🌟 사교적"],
        "fun_fact": "🔥 파이리의 꼬리 불꽃은 감정에 따라 크기가 변해요. ESFP처럼 감정이 풍부하고 솔직하죠!",
        "type_color": "#E17055"
    },
}

MBTI_TYPES = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

MBTI_GROUPS = {
    "🧠 분석가형 (NT)": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "💚 외교관형 (NF)": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "🛡️ 관리자형 (SJ)": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "🎯 탐험가형 (SP)": ["ISTP", "ISFP", "ESTP", "ESFP"],
}


# ─── UI 시작 ───────────────────────────────────────────────

# 헤더
st.markdown("""
<div class="main-card">
    <div class="title-box">🎮 MBTI 포켓몬 매칭</div>
    <div style="font-size: 1.5rem; margin: 0.3rem 0">✨ 나에게 어울리는 포켓몬은? ✨</div>
    <div class="subtitle">당신의 MBTI를 선택하면 딱 맞는 포켓몬을 찾아드려요!<br>🌟 총 16가지 포켓몬이 기다리고 있어요 🌟</div>
</div>
""", unsafe_allow_html=True)


# MBTI 선택
st.markdown("### 🔍 나의 MBTI를 선택해주세요!")

col1, col2 = st.columns([3, 1])

with col1:
    selected_mbti = st.selectbox(
        "MBTI 유형",
        options=["선택하세요 👇"] + MBTI_TYPES,
        label_visibility="collapsed"
    )

with col2:
    lucky = st.button("🎲 랜덤!", use_container_width=True)

if lucky:
    selected_mbti = random.choice(MBTI_TYPES)
    st.session_state["lucky_mbti"] = selected_mbti

# 랜덤 결과 처리
if "lucky_mbti" in st.session_state and lucky:
    selected_mbti = st.session_state["lucky_mbti"]


# MBTI 그룹 표시
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
st.markdown("#### 📋 MBTI 유형 한눈에 보기")

for group_name, types in MBTI_GROUPS.items():
    st.markdown(f"<div class='section-label'>{group_name}</div>", unsafe_allow_html=True)
    cols = st.columns(4)
    for i, mbti in enumerate(types):
        with cols[i]:
            is_selected = (selected_mbti == mbti)
            if is_selected:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #c44dff, #667eea);
                            color: white; border-radius: 12px; padding: 10px;
                            text-align: center; font-weight: 800; font-size: 1rem;
                            box-shadow: 0 6px 20px rgba(196,77,255,0.5);">
                    {MBTI_POKEMON[mbti]['emoji']} {mbti}
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.7); border-radius: 12px;
                            padding: 10px; text-align: center; font-weight: 600;
                            color: #666; border: 1.5px solid rgba(200,150,255,0.3);">
                    {mbti}
                </div>""", unsafe_allow_html=True)


# ─── 결과 표시 ─────────────────────────────────────────────
if selected_mbti in MBTI_POKEMON:
    data = MBTI_POKEMON[selected_mbti]
    pokemon_num = data["number"]
    
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("## 🎉 매칭 결과!")

    # 포켓몬 이미지 URL (공식 스프라이트)
    img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_num}.png"
    
    st.markdown(f"""
    <div class="result-card">
        <div class="mbti-badge">🧩 {selected_mbti}</div>
        <br>
        <div style="font-size: 1rem; color: #888; margin-bottom: 0.5rem">당신과 어울리는 포켓몬은...</div>
        <div class="pokemon-name">{data['emoji']} {data['pokemon']}</div>
        <div style="color: #aaa; font-size: 0.9rem; margin-bottom: 1rem">({data['english']} #{pokemon_num:03d})</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 이미지
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        st.image(img_url, width=260, caption=f"{data['emoji']} {data['pokemon']}")

    # 특성 태그
    st.markdown("<div style='text-align:center; margin: 1rem 0'>", unsafe_allow_html=True)
    traits_html = " ".join([f"<span class='trait-chip'>{t}</span>" for t in data["traits"]])
    st.markdown(f"<div style='text-align:center'>{traits_html}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 매칭 이유
    st.markdown(f"""
    <div class="reason-box">
        <strong>💬 왜 {data['pokemon']}일까요?</strong><br><br>
        {data['reason']}
    </div>
    """, unsafe_allow_html=True)

    # 재미있는 사실
    st.markdown(f"""
    <div class="fun-fact">
        {data['fun_fact']}
    </div>
    """, unsafe_allow_html=True)

    # 공유 메시지
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.6);
                border-radius: 18px; margin-top: 1rem;">
        <div style="font-size: 1.3rem; font-weight: 800; color: #555; margin-bottom: 0.5rem">
            🌟 결과를 친구에게 공유해보세요!
        </div>
        <div style="font-size: 1rem; color: #888; line-height: 1.8">
            "나는 <strong>{selected_mbti}</strong>이고<br>
            나의 포켓몬은 <strong>{data['emoji']} {data['pokemon']}</strong>이야!"
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_mbti == "선택하세요 👇":
    st.markdown("""
    <div style="text-align:center; padding: 2rem; color: #aaa; font-size: 1.1rem; margin-top: 1rem">
        ⬆️ 위에서 MBTI를 선택하거나<br>
        🎲 랜덤 버튼을 눌러보세요!
    </div>
    """, unsafe_allow_html=True)


# ─── 푸터 ──────────────────────────────────────────────────
st.markdown("""
<div class="footer" style="text-align:center; margin-top: 3rem; padding: 1rem">
    🎮 포켓몬 이미지 출처: PokéAPI Official Artwork<br>
    만들어진 곳: Claude AI 🤖 | 모든 포켓몬은 Nintendo / Game Freak 소유
</div>
""", unsafe_allow_html=True)
