import streamlit as st
import time

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Wine Quality Judge 🍷",
    page_icon="🍷",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

/* ===== Wine Color Gradient Background ===== */
.stApp {
    background: linear-gradient(
        135deg,
        #3a0010,
        #5a0018,
        #2a000b
    );
    background-size: 300% 300%;
    animation: wineFlow 10s ease infinite;
    color: white;
}

@keyframes wineFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===== Title ===== */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #ffd6df;
    margin-bottom: 35px;
}

/* ===== Sidebar ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2a000b, #420012);
}

/* ===== Sidebar Header ===== */
section[data-testid="stSidebar"] h2 {
    color: white !important;
}

/* ===== Slider Track ===== */
.stSlider > div[data-baseweb="slider"] > div {
    height: 6px;
    border-radius: 10px;
    background: #7b1e4a !important;
}

/* ===== Slider Thumb ===== */
.stSlider [role="slider"] {
    background: white !important;
    border: 3px solid white;
    box-shadow: 0 0 12px rgba(255,255,255,0.9);
}

/* ===== Slider Labels ===== */
.stSlider label, .stSlider span {
    color: white !important;
    font-weight: bold;
}

/* ===== Output Card ===== */
.output-box {
    background: rgba(255,255,255,0.18);
    padding: 55px;
    border-radius: 28px;
    box-shadow: 0 0 45px rgba(255, 100, 150, 0.7);
    text-align: center;
    margin-top: 40px;
}

/* ===== Result ===== */
.result {
    font-size: 46px;
    font-weight: bold;
}

/* ===== Comment ===== */
.comment {
    font-size: 22px;
    margin-top: 12px;
    color: #ffe6ec;
}

/* ===== Thinking Animation ===== */
.thinking {
    text-align: center;
    font-size: 26px;
    animation: blink 1.5s infinite;
}

@keyframes blink {
    0% { opacity: 0.3; }
    50% { opacity: 1; }
    100% { opacity: 0.3; }
}

/* ===== Emoji Celebration ===== */
.celebrate {
    font-size: 42px;
    animation: pop 1.2s ease-in-out infinite;
}

@keyframes pop {
    0% { transform: scale(1); }
    50% { transform: scale(1.25); }
    100% { transform: scale(1); }
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("<div class='title'>🍷 Wine Quality Judge</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Chemical Properties Based Quality Evaluation</div>", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.header("🧪 Chemical Properties")

fixed_acidity = st.sidebar.slider("🍋 Fixed Acidity", 4.0, 15.0, 7.0)
volatile_acidity = st.sidebar.slider("🧂 Volatile Acidity", 0.1, 1.5, 0.5)
citric_acid = st.sidebar.slider("🍊 Citric Acid", 0.0, 1.0, 0.3)
residual_sugar = st.sidebar.slider("🍬 Residual Sugar", 0.5, 15.0, 2.5)
alcohol = st.sidebar.slider("🍾 Alcohol %", 8.0, 15.0, 10.5)

# ================= BUTTON =================
analyze = st.button("🔍 Analyze Wine Quality")

# ================= LOGIC =================
if analyze:
    st.markdown("<div class='thinking'>🧠 Analyzing wine sample...</div>", unsafe_allow_html=True)
    time.sleep(2)

    score = 0
    if fixed_acidity <= 7.5: score += 1
    if volatile_acidity < 0.7: score += 1
    if citric_acid > 0.2: score += 1
    if residual_sugar < 5: score += 1
    if alcohol >= 10: score += 2

    if score <= 2:
        quality = "❌ POOR"
        comment = "Poor balance and low sensory quality."
        emojis = "😞🍷"
    elif score <= 4:
        quality = "⚠️ AVERAGE"
        comment = "Acceptable wine but lacks refinement."
        emojis = "🙂🍷"
    elif score <= 5:
        quality = "✅ GOOD"
        comment = "Well-balanced and enjoyable wine."
        emojis = "🎉🍷✨"
    else:
        quality = "🌟 EXCELLENT"
        comment = "Outstanding premium-quality wine."
        emojis = "🥂🍾🌟🔥"

    st.markdown(f"""
    <div class="output-box">
        <div class="result">{quality}</div>
        <div class="comment">{comment}</div>
        <div class="celebrate">{emojis}</div>
        <p style="margin-top:25px;color:#ffb3c6;font-size:18px;">
        — Created by <b>Devika</b> 💖
        </p>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown(
    "<p style='text-align:center;margin-top:55px;color:#ffd6df;'>🍷 Streamlit Wine Quality Project | Designed by Devika ✨</p>",
    unsafe_allow_html=True
)
