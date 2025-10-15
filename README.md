# 🧬 The Creative Chain

An interactive Streamlit application exploring how technological disruption has historically changed creativity—and how to think creatively with AI.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app/)

## 🎯 Overview

**The Creative Chain** is a three-phase interactive experience that:

1. **Phase 1: Walkthrough of History** — Navigate through pivotal moments when technology disrupted creativity (printing press → Renaissance, photography → Impressionism, etc.)
2. **Phase 2: Prompting as Process** — Learn to think creatively **with** AI through guided prompting exercises (ideate, structure, prototype, reflect)
3. **Phase 3: Design Your Disruption** — Map how human creativity might evolve in response to future disruptions

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd creative-chain
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open in browser**
   - The app should automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in your terminal

## 📁 Project Structure

```
creative-chain/
├── streamlit_app.py              # Main entry point / home page
├── pages/
│   ├── 01_Phase_1_Walkthrough.py # Interactive timeline
│   ├── 02_Phase_2_Prompting.py   # AI prompting exercises
│   └── 03_Phase_3_Design.py      # Design your disruption
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🔧 Configuration

### Adding LLM Integration (Phase 2)

Phase 2 currently uses placeholder responses. To integrate a real LLM:

1. Open `pages/02_Phase_2_Prompting.py`
2. Find the `call_llm()` function
3. Replace with your API integration (OpenAI, Anthropic, etc.)

Example with OpenAI:
```python
def call_llm(prompt: str) -> str:
    from openai import OpenAI
    client = OpenAI(api_key="your-api-key")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

### Customizing the Timeline (Phase 1)

Edit the `TIMELINE_ITEMS` list in `pages/01_Phase_1_Walkthrough.py` to add or modify historical periods.

## 🌐 Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set `streamlit_app.py` as the main file
5. Add any API keys in the Secrets section
6. Deploy!

## 📝 Features

- ✅ Interactive historical timeline with hover effects
- ✅ Guided AI prompting workflow
- ✅ Creative chain mapping tool
- ✅ Export functionality for summaries
- ✅ Session state management across phases
- ✅ Responsive design

## 🎨 Design Philosophy

The app uses constraints as a teaching tool—each historical period shows how creative workers adapted when technology removed a previous capability. This pattern helps users understand that AI isn't "replacing" creativity, but rather shifting what human creative value looks like.

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest new historical periods for Phase 1
- Improve prompting exercises in Phase 2
- Enhance the UI/UX

## 📄 License

[Add your license here]

## 🙏 Acknowledgments

Built with [Streamlit](https://streamlit.io) 🎈

---

**Questions?** Open an issue or reach out to [your contact info]