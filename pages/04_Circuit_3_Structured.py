import streamlit as st

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Brain Gym — Circuit 3: Structured Expression",
    page_icon="💡",
    layout="wide"
)

# ==== THEME (matches Circuits 1 & 2) ====
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
[data-testid="stSidebar"] .stProgress>div>div{background-color:#00d9ff!important;}

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

/* Card blocks */
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

# ==== PAGE HEADER ====
st.title("💡 Circuit 3 — Structured Expression (Prompt Playground)")
st.caption("Translate creative ideas into clear, actionable AI prompts")

st.markdown("""
**Goal:** Practice turning unstructured creative ideas into precise, effective prompts.  
This circuit focuses on **clarity**, **context**, and **structure** — the building blocks of good prompt design.
""")
st.markdown("""
**Need inspiration?**  
Try one of these starter ideas to get going:
- *“How might an AI assistant summarize Q2 performance trends for a client update?”*  
- *“How could an AI help designers generate product names inspired by natural patterns?”*
""")


# ==== SIDEBAR ====
st.sidebar.title("💡 Learning Tie-In")
st.sidebar.markdown("""
> “Effective prompts clearly define **role, task, format, and context.**  
>  
> This circuit trains clarity and specificity — key traits for guiding AI systems productively.”
""")
st.sidebar.progress(0.75)
st.sidebar.caption("Progress 3 of 4 circuits completed")

# ==== STEP 1 ====
st.divider()
st.subheader("🧠 Step 1 – Your Creative Idea")
st.write("Describe your idea, concept, or question in free-form language:")

idea = st.text_area(
    "Example: I want to explore how music could represent data about city traffic...",
    placeholder="Type your free-form idea here...",
    height=120
)

# ==== STEP 2 ====
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

role = st.text_input("Role (optional):", placeholder="e.g., financial analyst, UX designer, historian")
task = st.text_input("Task:", placeholder="e.g., analyze trends, summarize, generate ideas...")
format_ = st.text_input("Format:", placeholder="e.g., bullet points, memo, paragraph, table")
constraints = st.text_input("Constraints:", placeholder="e.g., under 150 words, professional tone, data-driven")
context = st.text_area("Context or Examples (optional):", placeholder="Any extra info or example output", height=100)

# ==== OUTPUT ====
if st.button("🧩 Generate Structured Prompt"):
    full_prompt = (
        f"Act as a {role or 'helpful expert'}.\n"
        f"Task: {task}\n"
        f"Format: {format_}\n"
        f"Constraints: {constraints}\n"
        f"Context: {context}"
    )
    st.markdown("### 🧱 Your Structured Prompt")
    st.code(full_prompt, language="markdown")
    st.session_state.structured_prompt = full_prompt

# ==== REFLECTION ====
st.divider()
st.subheader("🧭 Reflection Prompt")
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