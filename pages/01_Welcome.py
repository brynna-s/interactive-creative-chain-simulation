import streamlit as st
import streamlit.components.v1 as components

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Brain Gym — Welcome",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==== GLOBAL STYLE FIX (matches Circuit 1) ====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;600;700&display=swap');
/* Remove default white top strip / background */
[data-testid="stAppViewContainer"] {
  background-color: transparent !important;
  padding-top: 0 !important;
  margin-top: 0 !important;
}
[data-testid="stHeader"] {
  background: transparent !important;
  height: 0 !important;
  visibility: hidden;
}

.stApp {
  background: linear-gradient(180deg, #0a0e14 0%, #050810 100%);
}

/* Sidebar styling */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0f1419, #080c12);
  border-right: 1px solid #1f2937;
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
  color: #e6edf3 !important;
  font-family: 'Rajdhani', sans-serif !important;
}
[data-testid="stSidebar"] .stProgress > div > div {
  background-color: #00d9ff !important;
}

/* Headers */
h1, h2, h3 {
  font-family: 'Orbitron', sans-serif !important;
  letter-spacing: 1px;
  background: linear-gradient(135deg, #00d9ff, #d946ef);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Text */
p, div, span {
  font-family: 'Rajdhani', sans-serif !important;
  color: #e6edf3 !important;
}

/* Buttons */
.stButton > button {
  background: linear-gradient(135deg, #0f1419, #1a1f2e);
  border: 1px solid #1f2937;
  color: #00d9ff !important;
  font-family: 'Orbitron', sans-serif !important;
  font-weight: 600;
  letter-spacing: 0.5px;
  border-radius: 8px;
  transition: all 0.2s ease;
}
.stButton > button:hover {
  border-color: #00d9ff;
  box-shadow: 0 4px 20px rgba(0, 217, 255, 0.3);
  transform: translateY(-2px);
}

/* Cards / roadmap tiles */
.card {
  background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
  border: 1px solid #1f2937;
  border-radius: 16px;
  padding: 16px 22px;
  margin-bottom: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
  transition: all 0.2s ease;
}
.card:hover {
  border-color: #00d9ff;
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 217, 255, 0.3);
}
</style>
""", unsafe_allow_html=True)

# ==== HEADER ====
st.title("🧠 Brain Gym — Interactive Skill Circuits")
st.caption("Train your creative reasoning as a structured pathway to prompt-engineering mastery.")

st.divider()

# ==== INTRO ====
st.subheader("Welcome to Brain Gym")
st.markdown("""
**Brain Gym** is a creative training toolkit designed to strengthen the reasoning muscles behind effective AI collaboration.  
Each activity is an **interactive skill circuit** — not a game — guiding you from open-ended creativity toward structured, responsible prompting.

By completing these circuits, you’ll learn how **phrasing, analogy, structure, and iteration** shape the way AI systems respond —  
turning creative reasoning into **prompt-engineering mastery**.
""")

st.divider()

# ==== ROADMAP ====
st.subheader("🏋️ The Skill Circuit Roadmap")

st.markdown("""
<div class='card'>
  <h4 style='font-family:Orbitron;background:linear-gradient(135deg,#00d9ff,#d946ef);
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;'>
      🧩 Circuit 1 — Divergent Thinking</h4>
  <p>Build idea fluency and phrasing agility → discover how language shapes AI meaning.</p>
</div>
<div class='card'>
  <h4 style='font-family:Orbitron;background:linear-gradient(135deg,#00d9ff,#d946ef);
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;'>
      🔗 Circuit 2 — Semantic Linking</h4>
  <p>Connect unrelated concepts → strengthen analogical reasoning for richer prompts.</p>
</div>
<div class='card'>
  <h4 style='font-family:Orbitron;background:linear-gradient(135deg,#00d9ff,#d946ef);
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;'>
      💡 Circuit 3 — Structured Expression</h4>
  <p>Translate creative ideas into clear, contextual, and actionable AI instructions.</p>
</div>
<div class='card'>
  <h4 style='font-family:Orbitron;background:linear-gradient(135deg,#00d9ff,#d946ef);
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;'>
      🔁 Circuit 4 — Adaptive Challenge</h4>
  <p>Iterate and refine prompts → improve analytical clarity and ethical alignment.</p>
</div>
""", unsafe_allow_html=True)

# ==== BUTTONS ====
st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Start Training →", use_container_width=True, type="primary"):
        st.switch_page("pages/02_Circuit_1_Divergent.py")
with col2:
    if st.button("📊 View Reflection Dashboard", use_container_width=True):
        st.switch_page("pages/06_Reflection_Dashboard.py")

# ==== FOOTER ====
st.divider()
st.caption("🧠 Brain Gym | Microsoft Garage × NYU Stern Capstone 2025 | Creative-to-Prompt Learning Toolkit")
