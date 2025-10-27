import streamlit as st
import random

# ==== PAGE CONFIG ====
st.set_page_config(page_title="Brain Gym — Circuit 1: Divergent Thinking", page_icon="🧩", layout="wide")

# ==== CUSTOM STYLING FIXES ====
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

/* Fix sidebar colors & text */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg,#0f1419,#080c12);
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
[data-testid="stSidebar"]::before {
  content: '';
  display: block;
  height: 12px;
}

/* Titles */
h1,h2,h3 {
  font-family:'Orbitron',sans-serif!important;
  letter-spacing:1px;
  background:linear-gradient(135deg,#00d9ff,#d946ef);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}

/* Body text */
p,div,span {
  font-family:'Rajdhani',sans-serif!important;
  color:#e6edf3!important;
}

/* Buttons */
.stButton>button {
  background:linear-gradient(135deg,#0f1419,#1a1f2e);
  border:1px solid #1f2937;
  color:#00d9ff!important;
  font-family:'Orbitron',sans-serif!important;
  font-weight:600;
  letter-spacing:0.5px;
  border-radius:8px;
  transition:all .2s ease;
}
.stButton>button:hover {
  border-color:#00d9ff;
  box-shadow:0 4px 20px rgba(0,217,255,.3);
  transform:translateY(-2px);
}

/* Magnet tiles */
.magnet-grid {
  display:flex;
  flex-wrap:wrap;
  justify-content:center;
  gap:10px;
  margin:10px 0 30px 0;
}
.magnet {
  background:linear-gradient(135deg,#111720,#1a2130);
  border:1px solid #293241;
  border-radius:8px;
  padding:8px 14px;
  font-family:'Orbitron',sans-serif;
  font-size:16px;
  color:#00d9ff;
  text-transform:lowercase;
  box-shadow:0 2px 6px rgba(0,217,255,.2);
  transition:all .15s ease;
}
.magnet:hover {
  background:linear-gradient(135deg,#182030,#222b40);
  transform:translateY(-3px);
  box-shadow:0 4px 14px rgba(0,217,255,.3);
}
</style>
""", unsafe_allow_html=True)

# ==== PAGE CONTENT ====
st.title("🧩 Circuit 1 — Divergent Thinking (Magnet Mixer)")
st.caption("Build flexible phrasing and idea fluency")

st.markdown("""
**Goal:** Create as many creative or meaningful sentences as you can using the random word magnets below.  
Afterward, reflect on how **phrasing** influences tone and meaning — just like phrasing in a prompt changes AI output.
""")

# ==== SIDEBAR ====
st.sidebar.title("💡 Learning Tie-In")
st.sidebar.markdown("""
> “In prompt engineering, phrasing determines how the model interprets context.”  
>  
> Small wording shifts can transform outcomes — this circuit trains that awareness.
""")
st.sidebar.progress(0.25)
st.sidebar.caption("Progress 1 of 4 circuits completed")

# ==== UPDATED WORD BANK ====
word_bank = [
    # nouns / concepts
    "echo","neon","mirror","code","glass","dream","pulse","seed","storm","spark",
    "network","data","canvas","light","memory","machine","song","shadow","mind",
    # prepositions & connectors
    "in","on","under","over","with","through","beyond","within","to","for","of","and"
]

# Initialize shuffled words
if "shuffled_words" not in st.session_state:
    st.session_state.shuffled_words = random.sample(word_bank, 16)

# ==== MAGNET MIXER ====
st.divider()
st.subheader("🧲 Magnet Mixer")
st.markdown("Click **Shuffle Words** to refresh, then type your sentence using any of the words shown below.")

# Display word magnets
magnet_html = "<div class='magnet-grid'>" + "".join(
    [f"<div class='magnet'>{w}</div>" for w in st.session_state.shuffled_words]
) + "</div>"
st.markdown(magnet_html, unsafe_allow_html=True)

if st.button("🔄 Shuffle Words"):
    st.session_state.shuffled_words = random.sample(word_bank, 16)
    st.rerun()

# ==== SENTENCE INPUT ====
st.divider()
st.subheader("✍️ Your Sentence")
sentence = st.text_input("Compose a creative or meaningful sentence using at least 3 words from the list above:")

if "saved_sentences" not in st.session_state:
    st.session_state.saved_sentences = []

if st.button("💾 Save Sentence"):
    if sentence.strip():
        st.session_state.saved_sentences.append(sentence.strip())
        st.success("Sentence saved! Add another or scroll down to reflect.")
    else:
        st.warning("Please enter a sentence first.")

if st.session_state.saved_sentences:
    st.markdown("### 🗃 Your Sentences")
    for i, s in enumerate(st.session_state.saved_sentences, 1):
        st.markdown(f"**{i}.** {s}")

# ==== REFLECTION ====
st.divider()
st.subheader("🧠 Reflection Prompt")
reflection = st.text_area(
    "How did phrasing affect the meaning or tone of what you created?",
    placeholder="Write your reflection here..."
)

if st.button("✅ Save Reflection"):
    st.session_state.reflection = reflection
    st.success("Reflection saved!")

# ==== NAVIGATION ====
st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button("← Back to Welcome", use_container_width=True):
        st.switch_page("pages/01_BrainGym_Welcome.py")
with col2:
    if st.button("Continue to Circuit 2 →", use_container_width=True, type="primary"):
        st.switch_page("pages/03_Circuit_2_Semantic.py")

st.divider()
st.caption("Brain Gym | Circuit 1: Divergent Thinking © Microsoft Garage × NYU Stern Capstone 2025")
