import streamlit as st
import random

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(page_title="Brain Gym — Circuit 1: Divergent Thinking", page_icon="🧩", layout="wide")

# =============================
# THEME & TOP-STRIP FIX
# =============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;600;700&display=swap');

:root{
  --bg1:#0a0e14; --bg2:#050810; --panel:#0f1419; --panel2:#1a1f2e;
  --line:#1f2937; --text:#e6edf3; --muted:#8b949e;
  --c1:#00d9ff; --c2:#d946ef;
  --noun:#00d9ff; --verb:#22c55e; --mod:#facc15; --conn:#fb7185;
}

/* remove top white strip & header */
[data-testid="stAppViewContainer"]{ background-color: transparent !important; padding-top:0 !important; margin-top:0 !important; }
[data-testid="stHeader"]{ background: transparent !important; height:0 !important; visibility:hidden; }

.stApp{ background: linear-gradient(180deg,var(--bg1) 0%,var(--bg2) 100%); }
h1,h2,h3{ font-family:'Orbitron',sans-serif!important; letter-spacing:1px;
  background:linear-gradient(135deg,var(--c1),var(--c2)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
p,div,span{ font-family:'Rajdhani',sans-serif!important; color:var(--text)!important; }
.stDivider{ opacity:.5; }

/* sidebar */
[data-testid="stSidebar"]{ background:linear-gradient(180deg,#0f1419,#080c12); border-right:1px solid var(--line); }
[data-testid="stSidebar"] *{ color:var(--text)!important; font-family:'Rajdhani',sans-serif!important; }
[data-testid="stSidebar"] .stProgress > div > div{ background-color: var(--c1) !important; }

/* buttons */
.stButton>button{
  background:linear-gradient(135deg,var(--panel),var(--panel2));
  border:1px solid var(--line); color:var(--c1)!important;
  font-family:'Orbitron',sans-serif!important; font-weight:600; letter-spacing:.5px; border-radius:10px;
  transition:all .15s ease; }
.stButton>button:hover{ border-color:var(--c1); box-shadow:0 4px 20px rgba(0,217,255,.25); transform:translateY(-2px); }

/* cards */
.card{ background:linear-gradient(135deg,var(--panel),var(--panel2)); border:1px solid var(--line);
  border-radius:16px; padding:22px; box-shadow:0 8px 32px rgba(0,0,0,.45); }

/* magnet grid */
.magnet-grid{ display:flex; flex-wrap:wrap; gap:10px; }
.magnet{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; border-radius:10px; border:1px solid var(--line);
  background:linear-gradient(135deg,#111720,#1a2130);
  color:var(--text); font-family:'Orbitron',sans-serif; text-transform:lowercase; font-size:16px;
  box-shadow:0 2px 6px rgba(0,0,0,.25); user-select:none; cursor:pointer; transition:all .12s ease;
}
.magnet:hover{ transform:translateY(-2px); box-shadow:0 6px 16px rgba(0,217,255,.18); }
.magnet.noun{ color:var(--noun); }
.magnet.verb{ color:var(--verb); }
.magnet.mod{ color:var(--mod); }
.magnet.conn{ color:var(--conn); }

/* sentence canvas chips */
.chips{ display:flex; flex-wrap:wrap; gap:8px; }
.chip{
  padding:6px 12px; border-radius:999px; border:1px solid var(--line);
  background:linear-gradient(135deg,#101620,#1b2230); font-family:'Rajdhani',sans-serif; font-size:15px; color:var(--text);
}
.hint{ color:var(--muted); font-size:14px; }
.badge{ font-size:11px; padding:2px 8px; border-radius:999px; border:1px solid var(--line); opacity:.9; }
.badge.noun{ color:var(--noun); } .badge.verb{ color:var(--verb); } .badge.mod{ color:var(--mod); } .badge.conn{ color:var(--conn); }
</style>
""", unsafe_allow_html=True)

# =============================
# STATE
# =============================
if "stage" not in st.session_state: st.session_state.stage = 0  # 0=Onboarding, 1=Build, 2=Compare
if "word_bank" not in st.session_state: st.session_state.word_bank = {}
if "deck" not in st.session_state: st.session_state.deck = []
if "sentence_tokens" not in st.session_state: st.session_state.sentence_tokens = []

# =============================
# WORD BANK (by category)
# =============================
NOUNS = ["echo","neon","mirror","data","canvas","light","memory","machine","song","shadow","network","signal","pattern","model","prompt","context"]
VERBS = ["maps","shapes","guides","mirrors","amplifies","filters","links","reveals","builds","iterates","generates","adapts","tests","clarifies","structures"]
MODS  = ["precise","concise","playful","analytical","ethical","safe","clear","focused","novel","human","adaptive","synthetic","useful","reliable","contextual"]
CONNS = ["in","on","with","for","of","to","through","beyond","within","and","under","over"]

def shuffle_deck():
    # pick a balanced set (e.g., 6 nouns, 4 verbs, 4 mods, 6 conns) -> 20 total
    deck = random.sample(NOUNS, 6) + random.sample(VERBS, 4) + random.sample(MODS, 4) + random.sample(CONNS, 6)
    random.shuffle(deck)
    st.session_state.deck = deck

if not st.session_state.deck:
    shuffle_deck()

# Helper: categorize a word
def category_of(w):
    if w in NOUNS: return "noun"
    if w in VERBS: return "verb"
    if w in MODS:  return "mod"
    return "conn"

# =============================
# SIDEBAR
# =============================
st.sidebar.title("💡 Learning Tie-In")
st.sidebar.write("> “Every word you choose is a **token** that steers model interpretation.”")
st.sidebar.write("In this circuit, you’ll **build** a sentence from magnets, then later **compare** it to an AI’s sentence made from the same words.")
st.sidebar.progress(0.25)
st.sidebar.caption("Progress 1 of 4 circuits")

# =============================
# STAGE 0 — ONBOARDING
# =============================
if st.session_state.stage == 0:
    st.title("🧩 Circuit 1 — Divergent Thinking (Magnet Mixer)")
    st.caption("Stage 0 — Onboarding")
    st.markdown("""
<div class="card">
  <h3 style="margin:0 0 8px 0;">What you’ll do</h3>
  <p>• Click magnetic words to build a sentence on the canvas.<br>
     • You’re assembling a mini-prompt: <em>order and choice matter</em>.<br>
     • Next, you’ll see how an AI uses the **exact same words** to compose a sentence.</p>
  <p class="hint">Goal: feel how small wording changes shift meaning — the heart of prompt engineering.</p>
</div>
""", unsafe_allow_html=True)

    colA, colB = st.columns([1,1])
    with colA:
        if st.button("🚀 Start Building"):
            st.session_state.stage = 1
            st.rerun()
    with colB:
        if st.button("← Back to Welcome"):
            st.switch_page("pages/01_BrainGym_Welcome.py")

# =============================
# STAGE 1 — WORD SELECTION / BUILDER
# =============================
if st.session_state.stage == 1:
    st.title("🧩 Circuit 1 — Divergent Thinking (Magnet Mixer)")
    st.caption("Stage 1 — Build your sentence from magnets")

    # Controls row
    c1, c2, c3, c4 = st.columns([1,1,1,3])
    with c1:
        if st.button("🔄 Shuffle Words"):
            shuffle_deck(); st.rerun()
    with c2:
        if st.button("🧹 Clear Sentence"):
            st.session_state.sentence_tokens = []; st.rerun()
    with c3:
        if st.button("↩️ Undo Last"):
            if st.session_state.sentence_tokens:
                st.session_state.sentence_tokens.pop(); st.rerun()
    with c4:
        pass

    st.divider()

    # Magnets section — grouped by category
    st.subheader("🧲 Word Magnets")

    # Render magnets as clickable buttons in a grid
    def render_magnet(word, idx):
        cat = category_of(word)
        # Use form to keep buttons on the same line groups stable
        if st.button(word, key=f"mag_{idx}", help=f"{cat}", use_container_width=False):
            st.session_state.sentence_tokens.append(word)

    # Show legend
    st.markdown("""
<span class="badge noun">noun</span> <span class="badge verb">verb</span>
<span class="badge mod">modifier</span> <span class="badge conn">connector</span>
""", unsafe_allow_html=True)

    # Custom HTML grid for color + hover while still using buttons
    # We’ll render styled divs for looks, but actual click is Streamlit buttons below.
    styled = "".join([f"<span class='magnet {category_of(w)}'>{w}</span>" for w in st.session_state.deck])
    # --- Clickable Magnet Buttons ---
    st.markdown("<div class='magnet-grid'>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, word in enumerate(st.session_state.deck):
        cat = category_of(word)
        with cols[i % 5]:
            if st.button(word, key=f"mag_{i}", use_container_width=True):
                st.session_state.sentence_tokens.append(word)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Filler word input ---
    st.markdown("### ✏️ Add Your Own Word")
    new_word = st.text_input(
        "Type a connector or filler (e.g., 'towards', 'around', 'via')",
        key="custom_word"
    )
    if st.button("Add Word ➕"):
        if new_word.strip():
            st.session_state.sentence_tokens.append(new_word.strip())
            st.toast(f"Added '{new_word.strip()}' to your sentence!")
            st.rerun()

    st.divider()


    # Sentence canvas
    st.subheader("📝 Your Sentence Canvas")
    if st.session_state.sentence_tokens:
        st.markdown(
            "<div class='chips'>" +
            "".join([f"<span class='chip'>{tok}</span>" for tok in st.session_state.sentence_tokens]) +
            "</div>", unsafe_allow_html=True
        )
        st.markdown(
            f"<p class='hint'>Preview: “{' '.join(st.session_state.sentence_tokens)}”</p>",
            unsafe_allow_html=True
        )
    else:
        st.markdown("<p class='hint'>Click magnets above to start building your sentence…</p>", unsafe_allow_html=True)

    st.divider()

    # Proceed to Stage 2 (Compare) — will be implemented next
    min_words = 3
    ready = len(st.session_state.sentence_tokens) >= min_words
    cL, cR = st.columns([1,3])
    with cL:
        if st.button("Continue → Compare with AI", disabled=not ready, type="primary"):
            st.session_state.stage = 2  # We'll implement Stage 2 next
            st.rerun()
    with cR:
        if not ready:
            st.caption(f"Add at least {min_words} words to continue.")

    st.divider()
    st.caption("Brain Gym | Circuit 1 — Stage 1 © Microsoft Garage × NYU Stern Capstone 2025")
# =============================
# STAGE 2 — HUMAN vs AI COMPARISON
# =============================
elif st.session_state.stage == 2:
    st.title("🧩 Circuit 1 — Divergent Thinking (Magnet Mixer)")
    st.caption("Stage 2 — Compare Your Sentence to AI’s")

    user_sentence = " ".join(st.session_state.sentence_tokens)

    # --- Simulated AI generation ---
    # lightweight rearrange to feel "model-like"
    words = st.session_state.deck.copy()
    random.shuffle(words)
    ai_sentence = " ".join(words[: random.randint(6, 10)]).capitalize() + "."


    st.markdown("### 🤖 Human vs AI Output Comparison")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🧠 Your Sentence**")
        st.markdown(f"> {user_sentence}")
    with col2:
        st.markdown("**⚙️ AI-Generated Sentence**")
        st.markdown(f"> {ai_sentence}")

    st.divider()

    # --- Micro-lesson feedback block ---
    st.subheader("🧭 Quick Compare & Learn")

    colT, colF, colC = st.columns(3)
    tone = colT.radio("Tone", ["– Select –","Calm","Energetic","Formal","Playful"], index=0)
    focus = colF.radio("Focus", ["– Select –","Abstract","Concrete"], index=0)
    clarity = colC.radio("Clarity", ["– Select –","Ambiguous","Specific"], index=0)

    # --- Micro-lesson output ---
    st.divider()
    feedback = []
    if tone != "– Select –":
        feedback.append("🎵 Small wording changes shift tone — models amplify adjectives & verbs.")
    if focus != "– Select –":
        feedback.append("🔍 Abstract words invite creativity; concrete ones anchor facts — balance them in prompts.")
    if clarity != "– Select –":
        feedback.append("💡 Precision guides models — extra context reduces ambiguity.")
    if feedback:
        st.markdown("### 💬 Micro-Lessons")
        for tip in feedback:
            st.markdown(f"- {tip}")

    # --- Iteration control ---
    st.divider()
    st.subheader("🔄 Tweak and Iterate")
    st.markdown("""
Try adjusting your sentence: swap a word, add a connector, or change the order.  
Then regenerate to see how the AI interprets it differently.
""")

    c1, c2 = st.columns([1,1])
    with c1:
        if st.button("↩️ Return to Builder"):
            st.session_state.stage = 1
            st.rerun()
    with c2:
        if st.button("Continue to Circuit 2 →", type="primary"):
            st.switch_page("pages/03_Circuit_2_Semantic.py")

    st.divider()
    st.caption("Brain Gym | Circuit 1 — Stage 2 © Microsoft Garage × NYU Stern Capstone 2025")
# =============================
# STAGE 3 — ITERATION LAB
# =============================
elif st.session_state.stage == 3:
    st.title("🧩 Circuit 1 — Divergent Thinking (Magnet Mixer)")
    st.caption("Stage 3 — Prompt Refinement Lab")

    # Retrieve last sentences
    base_sentence = " ".join(st.session_state.sentence_tokens)
    if "last_ai_sentence" in st.session_state:
        ai_prev = st.session_state.last_ai_sentence
    else:
        ai_prev = ""

    st.markdown("""
### 🔄 Refine and Regenerate
You’ve seen how the same words can produce different meanings.  
Now, **edit or expand** your sentence to steer the AI closer to your intent.
""")

    st.markdown(f"**Your previous sentence:**  \n> {base_sentence}")

    refined = st.text_input("✏️ Edit or rephrase your sentence:", value=base_sentence)

    # Simulate AI improvement
    if "iter_output" not in st.session_state:
        st.session_state.iter_output = ""

    if st.button("🚀 Regenerate AI Sentence"):
        tokens = refined.split()
        random.shuffle(tokens)
        ai_new = " ".join(tokens).capitalize() + "."
        st.session_state.iter_output = ai_new
        st.session_state.last_ai_sentence = ai_new
        st.success("New AI output generated!")

    if st.session_state.iter_output:
        st.divider()
        st.markdown("### 🧠 Comparison")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Your Edited Sentence**")
            st.markdown(f"> {refined}")
        with col2:
            st.markdown("**AI Regenerated Sentence**")
            st.markdown(f"> {st.session_state.iter_output}")

        # Mini-feedback tips
        st.markdown("""
💬 *Notice how even one added connector or adjective shifts tone and focus.*  
Iterating and testing phrasing is what turns language play into professional prompt engineering.
""")

    st.divider()
    st.subheader("✅ Wrap-Up Options")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("↩️ Back to Comparison"):
            st.session_state.stage = 2
            st.experimental_rerun()
    with c2:
        if st.button("🧩 Restart Circuit 1"):
            st.session_state.sentence_tokens = []
            st.session_state.iter_output = ""
            st.session_state.stage = 1
            st.experimental_rerun()
    with c3:
        if st.button("Continue to Circuit 2 →", type="primary"):
            st.switch_page("pages/03_Circuit_2_Semantic.py")

    st.divider()
    st.caption("Brain Gym | Circuit 1 — Stage 3 © Microsoft Garage × NYU Stern Capstone 2025")
