import streamlit as st

st.set_page_config(
    page_title="The Creative Chain",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
def init_state():
    st.session_state.setdefault("phase", 1)
    st.session_state.setdefault("scene_idx", 0)
    st.session_state.setdefault("chat", [])
    st.session_state.setdefault("design", {
        "disruption": "",
        "chain": [],
        "reflection": ""
    })

init_state()

# Main landing page
st.title("🧬 The Creative Chain")
st.markdown("""
### An Interactive Journey Through Creative Disruption

Explore how technological disruption has historically changed creativity, 
then use AI to simulate your own creative ideation process.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📜 Phase 1")
    st.markdown("**Walkthrough of History**")
    st.markdown("Navigate through pivotal moments when technology disrupted creativity.")
    if st.button("Start Phase 1 →", key="nav_phase1", use_container_width=True):
        st.switch_page("pages/01_Phase_1_Walkthrough.py")

with col2:
    st.markdown("### 🤖 Phase 2")
    st.markdown("**Prompting as Process**")
    st.markdown("Learn to think creatively with AI through guided prompting exercises.")
    if st.button("Start Phase 2 →", key="nav_phase2", use_container_width=True):
        st.switch_page("pages/02_Phase_2_Prompting.py")

with col3:
    st.markdown("### 🎨 Phase 3")
    st.markdown("**Design Your Disruption**")
    st.markdown("Map how human creativity might evolve in response to new disruptions.")
    if st.button("Start Phase 3 →", key="nav_phase3", use_container_width=True):
        st.switch_page("pages/03_Phase_3_Design.py")

st.divider()

st.markdown("""
#### About This Project

**The Creative Chain** demonstrates how creativity evolves in response to technological disruption. 
Throughout history, each new technology initially seemed to threaten existing creative practices, 
but ultimately expanded human creative capacity in unexpected ways.

This interactive experience will guide you through:
- Historical examples of creative adaptation
- Hands-on AI prompting techniques
- Building your own theory of future creative evolution
""")

# Footer
st.markdown("---")
st.caption("🧬 The Creative Chain | A guided exploration of creativity and disruption")