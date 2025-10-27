# 🧠 Brain Gym — Interactive Skill Circuits

An interactive Streamlit toolkit developed in collaboration with **Microsoft Garage × NYU Stern**, designed to strengthen creative reasoning and prompt-engineering mastery.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app/)

---

## 🎯 Overview

**Brain Gym** transforms creative reasoning into practical AI literacy.  
Each “circuit” trains a distinct creativity muscle — helping users think flexibly, form analogies, structure instructions, and iterate effectively when collaborating with AI.

### 💡 Circuits Overview
1. **🧩 Circuit 1: Divergent Thinking (Magnet Mixer)**  
   Build phrasing agility and idea fluency by composing creative sentences from randomized word magnets.
2. **🔗 Circuit 2: Semantic Linking (ThinkLink)**  
   Connect unrelated emojis to strengthen analogical reasoning — the basis for creative prompting.
3. **💡 Circuit 3: Structured Expression (Prompt Playground)**  
   Translate abstract ideas into structured, actionable AI prompts.
4. **🔁 Circuit 4: Adaptive Challenge (AI Remix)**  
   Refine and iterate on prompts to improve analytical clarity and collaboration.

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9 or higher  
- pip package manager  

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd brain-gym

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py


### 📁 Project Structure

```
brain-gym/
├── streamlit_app.py                # Project overview / main hub
├── pages/
│   ├── 01_BrainGym_Welcome.py      # Welcome + introduction
│   ├── 02_Circuit_1_Divergent.py   # Circuit 1: Magnet Mixer
│   ├── 03_Circuit_2_Semantic.py    # Circuit 2: ThinkLink
│   ├── 04_Circuit_3_Structured.py  # Circuit 3: Prompt Playground
│   ├── 05_Circuit_4_Adaptive.py    # Circuit 4: AI Remix
│   └── 06_Reflection_Dashboard.py  # Reflection summary + completion
├── styles/
│   └── global.css                  # Shared theme / style sheet
├── requirements.txt                # Python dependencies
└── README.md
```


### Learning Outcomes

Brain Gym teaches the core reasoning processes behind prompt engineering:
1. ✳️ Divergent Thinking → Wording and phrasing awareness
2. 🔗 Analogy Formation → Connecting concepts for richer prompts
3. 💡 Structured Expression → Clarity and context control
4. 🔁 Iteration → Refining AI responses through feedback

### 🖼 Design Philosophy
Brain Gym views creativity as a trainable system.
Just as physical circuits strengthen different muscles, these “skill circuits” build distinct reasoning abilities essential for effective, ethical AI collaboration.

## 🧑‍💻 Contributing

✅ We welcome contributions and collaboration!
- Suggest new exercises or circuit types
- Improve UI/UX or educational flow
- Report bugs or issues

## 🎨 Design Philosophy

The app uses constraints as a teaching tool—each historical period shows how creative workers adapted when technology removed a previous capability. This pattern helps users understand that AI isn't "replacing" creativity, but rather shifting what human creative value looks like.

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest new historical periods for Phase 1
- Improve prompting exercises in Phase 2
- Enhance the UI/UX

## 🙏 Acknowledgments

Built with ❤️ using Streamlit
Developed by the NYU Stern Consulting Capstone Team, in partnership with Microsoft Garage.
---

**Questions?** Open an issue or reach out to brynna-s