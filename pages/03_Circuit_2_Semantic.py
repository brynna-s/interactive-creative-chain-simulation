import streamlit as st
import random

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Brain Gym — Circuit 2: Semantic Linking",
    page_icon="🔗",
    layout="wide"
)

# ==== THEME (matches Circuit 1) ====
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

/* Sidebar styling */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg,#0f1419,#080c12);
  border-right: 1px solid #1f2937;
}
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,[data-testid="stSidebar"] span{
  color:#e6edf3!important;
  font-family:'Rajdhani',sans-serif!important;
}
[data-testid="stSidebar"] .stProgress>div>div{
  background-color:#00d9ff!important;
}

/* Titles */
h1,h2,h3{
  font-family:'Orbitron',sans-serif!important;
  letter-spacing:1px;
  background:linear-gradient(135deg,#00d9ff,#d946ef);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}

/* Text */
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

/* Emoji tiles */
.emoji-grid{
  display:flex;
  justify-content:center;
  flex-wrap:wrap;
  gap:12px;
  margin:10px 0 20px 0;
}
.emoji-tile{
  background:linear-gradient(135deg,#111720,#1a2130);
  border:1px solid #293241;
  border-radius:12px;
  padding:12px 18px;
  font-size:40px;
  box-shadow:0 2px 6px rgba(0,217,255,.25);
  transition:all .15s ease;
}
.emoji-tile:hover{
  background:linear-gradient(135deg,#182030,#222b40);
  transform:translateY(-3px);
  box-shadow:0 4px 14px rgba(0,217,255,.3);
}
</style>
""", unsafe_allow_html=True)

# ==== PAGE HEADER ====
st.title("🔗 Circuit 2 — Semantic Linking (ThinkLink)")
st.caption("Connect unrelated concepts to build analogical reasoning skills")

st.markdown("""
**Goal:** Combine two random emojis into a single concept, phrase, or metaphor.  
This helps train your ability to find **connections** — the same skill behind crafting creative AI prompts that blend ideas.
""")

# ==== SIDEBAR ====
st.sidebar.title("💡 Learning Tie-In")
st.sidebar.markdown("""
> “In prompt engineering, combining unrelated concepts can yield **novel insights**.  
> This circuit strengthens analogical thinking — the engine of creative prompting.”
""")
st.sidebar.progress(0.50)
st.sidebar.caption("Progress 2 of 4 circuits completed")

# ==== EMOJI SET (no external library) ====
emoji_list = [
    "🌊","🔥","🪞","🌙","🧠","🎭","📡","⚙️","🌱","💡",
    "🧩","🚀","🎨","💻","⏳","📚","🕸️","🏙️","🎵","🔮",
    "🪐","💬","🌍","🏦","📈","🤖","💎","🧮","💼","🔗"
]

# ==== STATE ====
def new_pair():
    return random.sample(emoji_list, 2)
if "emoji_pair" not in st.session_state:
    st.session_state.emoji_pair = new_pair()

# ==== DISPLAY ====
st.divider()
st.subheader("🧠 Emoji Pair")
pair = st.session_state.emoji_pair
st.markdown(
    f"<div class='emoji-grid'><div class='emoji-tile'>{pair[0]}</div>"
    f"<div class='emoji-tile'>{pair[1]}</div></div>",
    unsafe_allow_html=True
)

if st.button("🔄 New Pair"):
    st.session_state.emoji_pair = new_pair()
    st.rerun()

# ==== INPUT ====
st.divider()
st.subheader("💭 Your Link or Phrase")
st.markdown("Example → 🌊 + 🕯️ = “flickering calm” or “light that moves like water.”")

user_link = st.text_input("What connects these two emojis for you?")

if "saved_links" not in st.session_state:
    st.session_state.saved_links = []

if st.button("💾 Save Link"):
    if user_link.strip():
        st.session_state.saved_links.append({"pair": pair, "link": user_link.strip()})
        st.success("Link saved! Generate a new pair to try again.")
    else:
        st.warning("Please enter a link or phrase first.")

if st.session_state.saved_links:
    st.markdown("### 🗃 Your Connections")
    for i, item in enumerate(st.session_state.saved_links, 1):
        st.markdown(f"**{i}.** {item['pair'][0]} {item['pair'][1]} → *{item['link']}*")

# ==== REFLECTION ====
st.divider()
st.subheader("🧭 Reflection Prompt")
reflection = st.text_area(
    "How did you find meaning between two unrelated symbols? What strategies helped you connect them?",
    placeholder="Write your reflection here..."
)
if st.button("✅ Save Reflection"):
    st.session_state.reflection_2 = reflection
    st.success("Reflection saved!")

# ==== NAVIGATION ====
st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button("← Back to Circuit 1", use_container_width=True):
        st.switch_page("pages/02_Circuit_1_Divergent.py")
with col2:
    if st.button("Continue to Circuit 3 →", use_container_width=True, type="primary"):
        st.switch_page("pages/04_Circuit_3_Structured.py")

st.divider()
st.caption("Brain Gym | Circuit 2: Semantic Linking © Microsoft Garage × NYU Stern Capstone 2025")