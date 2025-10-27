import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Brain Gym — Welcome",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== Custom CSS: Dark Futuristic Theme =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;600;700&display=swap');

.stApp {
    background: linear-gradient(180deg, #0a0e14 0%, #050810 100%);
}
h1, h2, h3 {
    font-family: 'Orbitron', sans-serif !important;
    letter-spacing: 1px;
    background: linear-gradient(135deg, #00d9ff, #d946ef);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
p, div, span {
    font-family: 'Rajdhani', sans-serif !important;
    color: #e6edf3 !important;
}
.stButton > button {
    background: linear-gradient(135deg, #0f1419, #1a1f2e);
    border: 1px solid #1f2937;
    color: #00d9ff !important;
    font-family: 'Orbitron', sans-serif !important;
    font-weight: 600;
    letter-spacing: 0.5px;
    border-radius: 8px;
    transition: all 200ms ease;
}
.stButton > button:hover {
    border-color: #00d9ff;
    box-shadow: 0 4px 20px rgba(0, 217, 255, 0.3);
    transform: translateY(-2px);
}
.card {
    background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
    border: 1px solid #1f2937;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    transition: all 0.25s ease;
}
.card:hover {
    border-color: #00d9ff;
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# ===== Header =====
st.title("🧠 Brain Gym — Interactive Skill Circuits")
st.caption("Train your creative reasoning as a structured pathway to prompt-engineering mastery.")

st.divider()

# ===== Intro Section =====
st.subheader("Welcome to Brain Gym")
st.markdown("""
Brain Gym is a **creative training toolkit** designed to strengthen the reasoning muscles behind effective AI collaboration.
Each activity is an **interactive skill circuit** — not a game — guiding you from open-ended creativity toward structured, responsible prompting.
""")

st.markdown("""
By completing these circuits, you’ll learn how **phrasing, analogy, structure, and iteration** shape the way AI systems respond — 
turning creative reasoning into **prompt-engineering mastery.**
""")

st.divider()

# ===== Roadmap Visualization =====
st.subheader("🏋️ The Skill Circuit Roadmap")

components.html("""
<style>
.roadmap {
  display: flex;
  flex-direction: column;
  gap: 18px;
  max-width: 700px;
  margin: 0 auto;
}
.stage {
  background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
  border: 1px solid #1f2937;
  border-radius: 12px;
  padding: 18px 22px;
  color: #e6edf3;
  font-family: 'Rajdhani', sans-serif;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.5);
}
.stage:hover {
  border-color: #00d9ff;
  box-shadow: 0 4px 20px rgba(0, 217, 255, 0.3);
  transform: translateY(-2px);
}
.stage h4 {
  margin: 0;
  font-family: 'Orbitron', sans-serif;
  background: linear-gradient(135deg, #00d9ff, #d946ef);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.stage p {
  margin: 6px 0 0 0;
  font-size: 14px;
  color: #8b949e;
}
</style>

<div class="roadmap">
  <div class="stage">
    <h4>🧩 Circuit 1 — Divergent Thinking</h4>
    <p>Build idea fluency and phrasing agility → discover how language shapes AI meaning.</p>
  </div>
  <div class="stage">
    <h4>🔗 Circuit 2 — Semantic Linking</h4>
    <p>Connect unrelated concepts → strengthen analogical reasoning for richer prompts.</p>
  </div>
  <div class="stage">
    <h4>💡 Circuit 3 — Structured Expression</h4>
    <p>Translate creative ideas into clear, actionable prompts with defined roles and goals.</p>
  </div>
  <div class="stage">
    <h4>🔁 Circuit 4 — Adaptive Challenge</h4>
    <p>Iterate and refine → learn to collaborate responsibly and improve AI outputs.</p>
  </div>
</div>
""", height=500)

st.divider()

# ===== Microsoft Alignment Section =====
st.subheader("🔍 Why It Matters")
st.markdown("""
Brain Gym serves as **Microsoft’s lightweight on-ramp to Responsible AI** — teaching users how to prompt, iterate, and collaborate with AI **safely, creatively, and inclusively.**

It’s designed for **creative-computing and design-thinking learners**, but can easily expand into **corporate upskilling** via **Teams** or **Viva Learning** integrations.
""")

st.divider()

# ===== Navigation Buttons =====
col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 Return to Dashboard", use_container_width=True):
        st.switch_page("streamlit_app.py")
with col2:
    if st.button("Continue to Circuit 1 →", use_container_width=True, type="primary"):
        st.switch_page("pages/02_Circuit_1_Divergent.py")

st.divider()
st.caption("Brain Gym | Welcome & Orientation  © Microsoft Garage x NYU Stern Capstone 2025")