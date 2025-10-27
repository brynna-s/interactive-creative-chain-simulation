import streamlit as st
import random

# ==== PAGE CONFIG ====
st.set_page_config(page_title="Brain Gym — Circuit 1: Divergent Thinking", page_icon="🧩", layout="wide")

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
st.title("🧩 Circuit 1 — Divergent Thinking (Magnet Mixer)")
st.caption("Build flexible phrasing and idea fluency")

# ==== INSTRUCTIONS ====
st.markdown("""
**Goal:** Create as many creative or meaningful sentences as you can using the random word magnets below.  
Afterward, reflect on how **phrasing** influences tone and meaning — just like phrasing in a prompt changes an AI’s output.
""")

st.sidebar.title("💡 Learning Tie-In")
st.sidebar.markdown("""
> “In prompt engineering, **phrasing determines how the model interprets context.**  
>  
> Small wording changes can transform outputs — this circuit trains that awareness.”
""")
st.sidebar.progress(0.25)
st.sidebar.caption("Progress 1 of 4 circuits completed")

# ==== RANDOM WORD BANK ====
word_bank = [
    "echo","neon","whisper","data","sky","dream","pulse","mirror","machine","canvas","memory",
    "storm","algorithm","song","glass","light","map","code","shadow","seed","network","spark","mind"
]
if "shuffled_words" not in st.session_state:
    st.session_state.shuffled_words = random.sample(word_bank, 12)

st.divider()
st.subheader("🧲 Magnet Mixer")
st.markdown("Click **Shuffle Words** to refresh, then type your sentence using any of the words shown.")

cols = st.columns(6)
for i, word in enumerate(st.session_state.shuffled_words):
    with cols[i % 6]:
        st.markdown(f"<div style='text-align:center;color:#00d9ff;font-family:Orbitron;'>{word}</div>", unsafe_allow_html=True)

if st.button("🔄 Shuffle Words"):
    st.session_state.shuffled_words = random.sample(word_bank, 12)
    st.rerun()

# ==== USER INPUT ====
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
st.caption("Brain Gym | Circuit 1: Divergent Thinking © Microsoft Garage x NYU Stern Capstone 2025")