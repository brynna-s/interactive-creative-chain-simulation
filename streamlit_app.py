import streamlit as st

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Brain Gym — Interactive Skill Circuits",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==== INITIALIZE SESSION STATE ====
def init_state():
    st.session_state.setdefault("current_circuit", 0)
    st.session_state.setdefault("reflections", {})
    st.session_state.setdefault("progress", 0.0)

init_state()

# ==== MAIN LANDING PAGE ====
st.title("🧠 Brain Gym — Interactive Skill Circuits")
st.markdown("""
### A Guided Pathway from Creativity to Prompt-Engineering Mastery

**Brain Gym** transforms creative reasoning into practical AI literacy.  
Each circuit strengthens a different “creativity muscle” — helping you think, structure, and iterate like an effective prompt engineer.
""")

st.divider()

# ==== CIRCUIT CARDS ====
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧩 Circuit 1")
    st.markdown("**Divergent Thinking (Magnet Mixer)**")
    st.markdown("Build phrasing agility by creating sentences from randomized words.")
    if st.button("Start Circuit 1 →", key="nav_circuit1", use_container_width=True):
        st.switch_page("pages/02_Circuit_1_Divergent.py")

    st.markdown("### 💡 Circuit 3")
    st.markdown("**Structured Expression (Prompt Playground)**")
    st.markdown("Translate abstract ideas into clear, actionable prompts.")
    if st.button("Start Circuit 3 →", key="nav_circuit3", use_container_width=True):
        st.switch_page("pages/04_Circuit_3_Structured.py")

with col2:
    st.markdown("### 🔗 Circuit 2")
    st.markdown("**Semantic Linking (ThinkLink)**")
    st.markdown("Connect unrelated concepts to train analogical reasoning.")
    if st.button("Start Circuit 2 →", key="nav_circuit2", use_container_width=True):
        st.switch_page("pages/03_Circuit_2_Semantic.py")

    st.markdown("### 🔁 Circuit 4")
    st.markdown("**Adaptive Challenge (AI Remix)**")
    st.markdown("Refine and iterate on AI prompts to improve analytical clarity.")
    if st.button("Start Circuit 4 →", key="nav_circuit4", use_container_width=True):
        st.switch_page("pages/05_Circuit_4_Adaptive.py")

st.divider()

# ==== OVERVIEW SECTION ====
st.markdown("""
#### 💼 Why Brain Gym?

As organizations adopt AI tools, creativity and structured reasoning become critical workplace skills.  
Brain Gym offers a **hands-on, lightweight framework** to build those abilities — blending creative exploration with prompt-engineering discipline.

Each circuit focuses on a specific cognitive skill:

| Circuit | Focus Skill | AI Prompting Tie-In |
|:--|:--|:--|
| 🧩 Divergent Thinking | Flexible phrasing | How wording shifts AI tone and meaning |
| 🔗 Semantic Linking | Analogical reasoning | Building concept bridges in prompts |
| 💡 Structured Expression | Clarity and context | Turning abstract ideas into precise instructions |
| 🔁 Adaptive Challenge | Iterative refinement | Improving results through re-prompting and feedback |

""")

# ==== NAVIGATION TO DASHBOARD ====
st.divider()
st.subheader("📊 Reflection & Progress")
st.markdown("""
Track your growth, revisit reflections, and view your overall completion progress.
""")

if st.button("View Reflection Dashboard →", use_container_width=True):
    st.switch_page("pages/06_Reflection_Dashboard.py")

# ==== FOOTER ====
st.divider()
st.caption("🧠 Brain Gym | Microsoft Garage × NYU Stern Consulting Capstone 2025  |  A Creative-to-Prompt Learning Toolkit")