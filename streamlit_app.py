import streamlit as st

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Brain Gym — Project Overview",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==== THEME (dark, unified with circuits) ====
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
  background: linear-gradient(180deg,#0a0e14 0%,#050810 100%);
}

/* Sidebar */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg,#0f1419,#080c12);
  border-right: 1px solid #1f2937;
}
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,[data-testid="stSidebar"] span{
  color:#e6edf3!important;
  font-family:'Rajdhani',sans-serif!important;
}

/* Headings */
h1,h2,h3{
  font-family:'Orbitron',sans-serif!important;
  letter-spacing:1px;
  background:linear-gradient(135deg,#00d9ff,#d946ef);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}

/* Body text */
p,div,span{
  font-family:'Rajdhani',sans-serif!important;
  color:#e6edf3!important;
}

/* Buttons */
.stButton>button{
  background:linear-gradient(135deg,#0f1419,#1a1f2e);
  border:1px solid #1f2937;
  color:#00d9ff!important;
  font-family:'Orbitron',sans-serif!important;
  font-weight:600;
  letter-spacing:0.5px;
  border-radius:8px;
  transition:all .2s ease;
}
.stButton>button:hover{
  border-color:#00d9ff;
  box-shadow:0 4px 20px rgba(0,217,255,.3);
  transform:translateY(-2px);
}

/* Cards */
.card{
  background:linear-gradient(135deg,#0f1419 0%,#1a1f2e 100%);
  border:1px solid #1f2937;
  border-radius:16px;
  padding:24px;
  box-shadow:0 8px 32px rgba(0,0,0,.5);
  transition:all .25s ease;
}
.card:hover{
  border-color:#00d9ff;
  box-shadow:0 6px 20px rgba(0,217,255,.3);
}
</style>
""", unsafe_allow_html=True)

# ==== HEADER ====
st.title("📘 Brain Gym — Project Overview")
st.caption("A Microsoft Garage × NYU Stern Consulting Capstone Project")

st.markdown("""
### 🎯 Project Objective
**Brain Gym** is an interactive skill-building toolkit that transforms creativity training into practical **AI-literacy development**.  
Through four guided “circuits,” users strengthen different cognitive muscles — **flexibility, association, structure, and iteration** — mirroring the reasoning processes behind effective prompt engineering.

The project aligns with **Microsoft’s Responsible AI** principles by teaching users to:
- Understand how phrasing shapes AI outputs  
- Build structured, transparent communication with generative tools  
- Practice safe, creative collaboration between humans + AI
""")

# ==== HOW TO USE ====
st.divider()
st.subheader("🧭 How to Use Brain Gym")
st.markdown("""
1. Start with the **Welcome** page for orientation.  
2. Complete Circuits 1 → 4 sequentially — each circuit builds a different skill.  
3. Save your reflections after each circuit.  
4. Review all reflections and progress in the **Reflection Dashboard** at the end.
""")

# ==== ROADMAP ====
st.divider()
st.subheader("🏋️ Skill Circuits")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
      <h4 style='font-family:Orbitron;background:linear-gradient(135deg,#00d9ff,#d946ef);
          -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;'>🧩 Circuit 1 — Divergent Thinking</h4>
      <p>Build phrasing agility by creating sentences from randomized words.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Circuit 1 →", use_container_width=True):
        st.switch_page("pages/02_Circuit_1_Divergent.py")

    st.markdown("""
    <div class='card'>
      <h4 style='font-family:Orbitron;background:linear-gradient(135deg,#00d9ff,#d946ef);
          -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;'>💡 Circuit 3 — Structured Expression</h4>
      <p>Translate abstract ideas into clear, actionable AI prompts.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Circuit 3 →", use_container_width=True):
        st.switch_page("pages/04_Circuit_3_Structured.py")

with col2:
    st.markdown("""
    <div class='card'>
      <h4 style='font-family:Orbitron;background:linear-gradient(135deg,#00d9ff,#d946ef);
          -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;'>🔗 Circuit 2 — Semantic Linking</h4>
      <p>Connect unrelated concepts to train analogical reasoning and creative association.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Circuit 2 →", use_container_width=True):
        st.switch_page("pages/03_Circuit_2_Semantic.py")

    st.markdown("""
    <div class='card'>
      <h4 style='font-family:Orbitron;background:linear-gradient(135deg,#00d9ff,#d946ef);
          -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;'>🔁 Circuit 4 — Adaptive Challenge</h4>
      <p>Refine and iterate on AI prompts to improve analytical clarity and collaboration.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Circuit 4 →", use_container_width=True):
        st.switch_page("pages/05_Circuit_4_Adaptive.py")

# ==== FOOTER ====
st.divider()
st.caption("🧠 Brain Gym | Microsoft Garage × NYU Stern Capstone 2025 | A Creative-to-Prompt Learning Toolkit")
