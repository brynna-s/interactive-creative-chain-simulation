import streamlit as st

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Brain Gym — Circuit 3: Structured Expression",
    page_icon="💡",
    layout="wide"
)

# ==== CUSTOM THEME (same as previous pages) ====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;600;700&display=swap');
.stApp {background: linear-gradient(180deg,#0a0e14 0%,#050810 100%);}
h1,h2,h3{font-family:'Orbitron',sans-serif!important;letter-spacing:1px;
background:linear-gradient(135deg,#00d9ff,#d946ef);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
p,div,span{font-family:'Rajdhani',sans-serif!important;color:#e6edf3!important;}
.stButton>button{background:linear-gradient(135deg,#0f1419,#1a1f2e);
border:1px solid #1f2937;color:#00d9ff!important;font-family:'Orbitron',sans-serif!important;
font-weight:600;letter-spacing:0.5px;border-radius:8px;transition:all .2s ease;}
.stButton>button:hover{border-color:#00d9ff;box-shadow:0 4px 20px rgba(0,217,255,.3);transform:translateY(-2px);}
.card{background:linear-gradient(135deg,#0f1419 0%,#1a1f2e 100%);
border:1px solid #1f2937;border-radius:16px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,.5);}
</style>
""", unsafe_allow_html=True)

# ==== TITLE ====
st.title("💡 Circuit 3 — Structured Expression (Prompt Playground)")
st.caption("Translate creative ideas into clear, actionable AI prompts")

# ==== INSTRUCTIONS ====
st.markdown("""
**Goal:** Practice turning unstructured creative ideas into precise, effective prompts.  
This circuit focuses on clarity, context, and structure — the building blocks of good prompt design.
""")

st.sidebar.title("💡 Learning Tie-In")
st.sidebar.markdown("""
> “Effective prompts clearly define **role, task, format, and context.**  
>  
> This circuit trains clarity and specificity — key traits for guiding AI systems productively.”
""")
st.sidebar.progress(0.75)
st.sidebar.caption("Progress 3 of 4 circuits completed")

# ==== INPUT AREAS ====
st.divider()
st.subheader("🧠 Step 1 – Your Creative Idea")
idea = st.text_area(
    "Describe your idea, concept, or question in free-form language:",
    placeholder="Example: I want to explore how music could represent data about city traffic...",
    height=150
)

st.divider()
st.subheader("⚙️ Step 2 – Structure It as a Prompt")

with st.expander("💬 Prompt Elements (Reference)", expanded=False):
    st.markdown("""
    **1. Role:** Who should the AI act as?  
    **2. Task:** What should it do?  
    **3. Format:** How should the response look?  
    **4. Constraints:** Any limits or tone requirements?  
    **5. Context/Examples:** Extra details that help.
    """)

role = st.text_input("Role (optional):", placeholder="e.g., data storyteller, product designer, teacher")
task = st.text_input("Task:", placeholder="e.g., explain, analyze, generate ideas for, design...")
format_ = st.text_input("Format:", placeholder="e.g., bullet points, dialogue, poem, table")
constraints = st.text_input("Constraints:", placeholder="e.g., under 100 words, formal tone, no jargon")
context = st.text_area("Context or Examples (optional):", placeholder="Any extra info or sample output", height=100)

# Construct final prompt
if st.button("🧩 Generate Structured Prompt"):
    full_prompt = f"Act as a {role or 'helpful expert'}.\nTask: {task}\nFormat: {format_}\nConstraints: {constraints}\nContext: {context}\n"
    st.markdown("### 🧱 Your Structured Prompt")
    st.code(full_prompt, language="markdown")
    st.session_state.structured_prompt = full_prompt

# ==== REFLECTION ====
st.divider()
st.subheader("🧠 Reflection Prompt")
reflection = st.text_area(
    "How did structuring your idea clarify what you actually wanted? What changed between your free-form idea and your final prompt?",
    placeholder="Write your reflection here..."
)

if st.button("✅ Save Reflection"):
    st.session_state.reflection_3 = reflection
    st.success("Reflection saved!")

# ==== NAVIGATION ====
st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button("← Back to Circuit 2", use_container_width=True):
        st.switch_page("pages/03_Circuit_2_Semantic.py")
with col2:
    if st.button("Continue to Circuit 4 →", use_container_width=True, type="primary"):
        st.switch_page("pages/05_Circuit_4_Adaptive.py")

st.divider()
st.caption("Brain Gym | Circuit 3: Structured Expression © Microsoft Garage × NYU Stern Capstone 2025")