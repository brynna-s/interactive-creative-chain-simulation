import streamlit as st

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Brain Gym — Circuit 4: Adaptive Challenge",
    page_icon="🔁",
    layout="wide"
)

# ==== CUSTOM THEME ====
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
st.title("🔁 Circuit 4 — Adaptive Challenge (AI Remix)")
st.caption("Iterate, refine, and collaborate with AI for sharper financial insights")

# ==== INTRO ====
st.markdown("""
**Goal:** Learn how refining and re-phrasing analytical prompts improves clarity and accuracy.  
In finance, wording defines scope — whether you’re asking for a **variance analysis**, a **market brief**, or a **client summary**.
""")

st.sidebar.title("💡 Learning Tie-In")
st.sidebar.markdown("""
> “Iteration is at the core of analytical reasoning.  
> Each revision helps align AI output with financial logic, compliance tone, and stakeholder expectations.”
""")
st.sidebar.progress(1.0)
st.sidebar.caption("Progress 4 of 4 circuits completed ✅")

# ==== INPUT AREAS ====
st.divider()
st.subheader("💬 Step 1 – Original Prompt")
prompt = st.text_area(
    "Enter your initial analytical prompt:",
    placeholder="Example: Summarize our company's Q2 financial performance.",
    height=120
)

st.divider()
st.subheader("📊 Step 2 – Simulated AI Output")
if prompt:
    st.info("Below is a **simulated AI response** — representing a typical, unrefined first attempt.")
    simulated_output = (
        f"Simulated Response:\n\nHere’s a general overview based on your prompt:\n"
        f"'{prompt}'\n\n"
        "The summary lists revenues and expenses but lacks context, key drivers, and actionable insights — ready for refinement."
    )
    st.text_area("", value=simulated_output, height=180, disabled=True)

st.divider()
st.subheader("✏️ Step 3 – Refine Your Prompt")
st.markdown("""
Now **re-frame** your request to make it more specific:  
include a time frame, benchmark, audience, or desired output format.
""")

refined_prompt = st.text_area(
    "Refined Prompt:",
    placeholder=(
        "Example: Act as a financial analyst. Summarize Q2 results for a client memo, "
        "highlighting revenue growth vs Q1, expense trends, and key risks in bullet points."
    ),
    height=120
)

if "refined_output" not in st.session_state:
    st.session_state.refined_output = ""

if st.button("🚀 Generate Improved Output"):
    if refined_prompt.strip():
        st.session_state.refined_output = (
            f"Improved Response:\n\nBased on your clearer prompt — '{refined_prompt}' — "
            "the AI now produces a concise client-ready summary focusing on variances, ratios, and narrative insight."
        )
        st.success("Prompt refined! See comparison below.")
    else:
        st.warning("Please enter your refined prompt first.")

# ==== DISPLAY BEFORE & AFTER ====
if st.session_state.refined_output:
    st.divider()
    st.subheader("⚖️ Step 4 – Compare Results")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Before (Original)**")
        st.text_area("", value=prompt, height=120, disabled=True)
    with col2:
        st.markdown("**After (Refined)**")
        st.text_area("", value=refined_prompt, height=120, disabled=True)

    st.markdown("### 🧠 Simulated AI Response (After)")
    st.text_area("", value=st.session_state.refined_output, height=180, disabled=True)

# ==== REFLECTION ====
st.divider()
st.subheader("🧭 Reflection Prompt")
reflection = st.text_area(
    "How did refining your prompt improve the financial analysis or communication? "
    "What did you learn about clarity, scope, and audience?",
    placeholder="Write your reflection here..."
)

if st.button("✅ Save Reflection"):
    st.session_state.reflection_4 = reflection
    st.success("Reflection saved!")

# ==== CONCLUSION & NAVIGATION ====
st.divider()
st.markdown("""
### 🎓 Circuit Complete!
You’ve now completed all four Brain Gym circuits for creative and analytical reasoning:
1️⃣ Divergent Thinking – Flexibility  
2️⃣ Semantic Linking – Association  
3️⃣ Structured Expression – Clarity  
4️⃣ Adaptive Challenge – Iteration  
""")

col1, col2 = st.columns(2)
with col1:
    if st.button("← Back to Circuit 3", use_container_width=True):
        st.switch_page("pages/04_Circuit_3_Structured.py")
with col2:
    if st.button("🏁 View Summary / Reflection Dashboard →", use_container_width=True, type="primary"):
        st.switch_page("pages/06_Reflection_Dashboard.py")

st.divider()
st.caption("Brain Gym | Circuit 4: Adaptive Challenge © Microsoft Garage × NYU Stern Capstone 2025")