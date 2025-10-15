import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Creative Chain — Phase 1",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark tech theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;600;700&display=swap');
    
    /* Main app background */
    .stApp {
        background: linear-gradient(180deg, #0a0e14 0%, #050810 100%);
    }
    
    /* Headers */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 1px;
        background: linear-gradient(135deg, #00d9ff, #d946ef);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Body text */
    p, div, span {
        font-family: 'Rajdhani', sans-serif !important;
        color: #e6edf3 !important;
    }
    
    /* Caption */
    .stCaption {
        color: #8b949e !important;
        font-size: 14px !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0f1419, #1a1f2e);
        border: 1px solid #1f2937;
        color: #00d9ff !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 600;
        letter-spacing: 0.5px;
        border-radius: 8px;
        transition: all 200ms ease;
    }
    
    .stButton > button:hover {
        border-color: #00d9ff;
        box-shadow: 0 4px 20px rgba(0, 217, 255, 0.3);
        transform: translateY(-2px);
    }
    
    /* Column labels */
    .stMarkdown {
        color: #e6edf3 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("The Creative Chain — Phase 1: Walkthrough of History")
st.caption("Hover over the timeline bubbles to reveal visuals and blurbs. Left = Technology, Right = Art.")

# Define timeline data
TIMELINE_ITEMS = [
    {
        "era": "1450s–1500s",
        "tech_title": "Printing Press (Gutenberg)",
        "tech_blurb": "Democratized knowledge, accelerated literacy and replication.",
        "art_title": "Renaissance Humanism",
        "art_blurb": "Shift from religious symbolism to human-centered realism; invention of perspective.",
        "recalibration": "Humans rediscover individual intellect and authorship in a reproducible world.",
        "tech_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Printing_press_1811.jpg/800px-Printing_press_1811.jpg",
        "art_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/800px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"
    },
    {
        "era": "1760s–1840s",
        "tech_title": "Industrial Revolution",
        "tech_blurb": "Mechanization, factories, steam power, and new urban life.",
        "art_title": "Romanticism",
        "art_blurb": "Reaction to mechanization; emotion and nature over rationalism.",
        "recalibration": "Artists reclaim feeling and individuality amid machine logic.",
        "tech_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Powerloom_weaving_in_1835.jpg/800px-Powerloom_weaving_in_1835.jpg",
        "art_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg/800px-Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg"
    },
    {
        "era": "1839–1900",
        "tech_title": "Photography",
        "tech_blurb": "Mechanical reproduction of images reshapes representation.",
        "art_title": "Impressionism & Post-Impressionism",
        "art_blurb": "Artists reimagine perception, color, and time.",
        "recalibration": "Art shifts from depiction to expression; creativity becomes interpretation.",
        "tech_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Daguerreotype_camera_1839.jpg/800px-Daguerreotype_camera_1839.jpg",
        "art_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Claude_Monet%2C_Impression%2C_soleil_levant.jpg/800px-Claude_Monet%2C_Impression%2C_soleil_levant.jpg"
    },
    {
        "era": "1900–1930s",
        "tech_title": "Electricity, Mass Media, Telephone, Cinema",
        "tech_blurb": "Acceleration of communication and moving images.",
        "art_title": "Modernism / Cubism / Futurism",
        "art_blurb": "Fragmentation of perspective; fascination with speed and industry.",
        "recalibration": "Creativity explores abstraction and multiplicity of perception.",
        "tech_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Thomas_Edison2.jpg/800px-Thomas_Edison2.jpg",
        "art_image": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Les_Demoiselles_d%27Avignon.jpg/800px-Les_Demoiselles_d%27Avignon.jpg"
    },
    {
        "era": "1940s–1960s",
        "tech_title": "Computing and Television",
        "tech_blurb": "Early digital systems and mass broadcast.",
        "art_title": "Pop Art & Conceptualism",
        "art_blurb": "Commentary on mass media and consumerism.",
        "recalibration": "Artists question originality and authorship itself.",
        "tech_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Eniac.jpg/800px-Eniac.jpg",
        "art_image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/24/Warhol-Campbell_Soup-1-screenprint-1968.jpg/800px-Warhol-Campbell_Soup-1-screenprint-1968.jpg"
    },
    {
        "era": "1980s–1990s",
        "tech_title": "Personal Computer & Internet",
        "tech_blurb": "Democratization of creation and distribution.",
        "art_title": "Digital Art, Net Art, Cyberpunk",
        "art_blurb": "Code, networks, and the virtual as medium.",
        "recalibration": "Creativity blends with computation; new digital subjectivity emerges.",
        "tech_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/IBM_PC_5150.jpg/800px-IBM_PC_5150.jpg",
        "art_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Blade_Runner_spinner_flyby.jpg/800px-Blade_Runner_spinner_flyby.jpg"
    },
    {
        "era": "2000s–2010s",
        "tech_title": "Smartphone, Social Media, Algorithms",
        "tech_blurb": "Always-on creation and algorithmic curation.",
        "art_title": "Post-Internet Art & Remix Culture",
        "art_blurb": "Curation, meme-making, participatory art.",
        "recalibration": "Creativity becomes collective, iterative, and ephemeral.",
        "tech_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/IPhone_7_Plus_%28rear%29.png/800px-IPhone_7_Plus_%28rear%29.png",
        "art_image": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Trollface_non-free.png/800px-Trollface_non-free.png"
    },
    {
        "era": "2020s–Present",
        "tech_title": "Generative AI, Automation, Synthetic Data",
        "tech_blurb": "Models generate text, image, audio, code on demand.",
        "art_title": "AI Art, Prompt-based Creativity",
        "art_blurb": "Synthetic imagination and human-in-the-loop authorship.",
        "recalibration": "Creativity shifts to curation, prompting, and ethical direction.",
        "tech_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/800px-ChatGPT_logo.svg.png",
        "art_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Artificial_intelligence_prompt_engineering.png/800px-Artificial_intelligence_prompt_engineering.png"
    },
]

# Legend and layout spacer
left, mid, right = st.columns([1, 0.4, 1])
with left:
    st.markdown("**<span style='color: #00d9ff; font-family: Orbitron, sans-serif; letter-spacing: 1px;'>⚡ TECHNOLOGICAL DISRUPTIONS</span>**", unsafe_allow_html=True)
with mid:
    st.markdown(" ")
with right:
    st.markdown("**<span style='color: #d946ef; font-family: Orbitron, sans-serif; letter-spacing: 1px;'>✨ ARTISTIC DISRUPTIONS</span>**", unsafe_allow_html=True)

# Build interactive HTML/CSS/JS timeline
DATA_JSON = json.dumps(TIMELINE_ITEMS)

html = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');

:root {{
  --bg: #0a0e14;
  --panel: #0f1419;
  --text: #e6edf3;
  --muted: #8b949e;
  --accent-tech: #00d9ff;
  --accent-art: #d946ef;
  --spine: #1f2937;
  --bubble-hover: #ffffff15;
  --glow-tech: rgba(0, 217, 255, 0.3);
  --glow-art: rgba(217, 70, 239, 0.3);
}}

* {{ 
  box-sizing: border-box; 
  font-family: 'Rajdhani', sans-serif;
}}

.timeline-wrapper {{
  width: 100%;
  margin: 0 auto;
  color: var(--text);
  background: linear-gradient(180deg, #0a0e14 0%, #050810 100%);
  border-radius: 16px;
  padding: 24px 16px;
  border: 1px solid #1f2937;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
}}

.timeline-grid {{
  display: grid;
  grid-template-columns: 1fr 68px 1fr;
  gap: 16px 12px;
  align-items: center;
}}

.spine {{
  position: relative;
  width: 68px;
  margin: 0 auto;
  height: 100%;
}}
.spine::before {{
  content: "";
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 2px;
  top: 0;
  bottom: 0;
  background: linear-gradient(180deg, var(--accent-tech), var(--accent-art));
  border-radius: 2px;
  box-shadow: 0 0 10px var(--glow-tech), 0 0 20px var(--glow-art);
}}

.row {{
  display: contents;
}}

.era-cell {{
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 92px;
}}

.spine-dot {{
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 16px;
  height: 16px;
  background: linear-gradient(135deg, var(--accent-tech), var(--accent-art));
  border: 2px solid #0a0e14;
  border-radius: 50%;
  z-index: 2;
  box-shadow: 0 0 12px var(--glow-tech), 0 0 24px var(--glow-art);
  animation: pulse 2s ease-in-out infinite;
}}

@keyframes pulse {{
  0%, 100% {{ box-shadow: 0 0 12px var(--glow-tech), 0 0 24px var(--glow-art); }}
  50% {{ box-shadow: 0 0 20px var(--glow-tech), 0 0 40px var(--glow-art); }}
}}

.era-label {{
  position: relative;
  top: 32px;
  font-size: 13px;
  font-weight: 600;
  font-family: 'Orbitron', sans-serif;
  color: var(--accent-tech);
  text-align: center;
  white-space: nowrap;
  letter-spacing: 1px;
  text-shadow: 0 0 8px var(--glow-tech);
}}

.bubble {{
  position: relative;
  height: 92px;
  padding: 0 12px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-radius: 12px;
  border: 1px solid #1f2937;
  background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
  color: var(--text);
  cursor: pointer;
  transition: all 200ms ease;
  text-align: left;
  width: 100%;
  outline: none;
  font-family: 'Rajdhani', sans-serif;
}}
.bubble:hover, .bubble:focus-visible {{
  transform: translateY(-2px);
  background: linear-gradient(135deg, #1a1f2e 0%, #252b3d 100%);
  border-color: currentColor;
}}
.bubble.tech:hover, .bubble.tech:focus-visible {{
  border-color: var(--accent-tech);
  box-shadow: 0 4px 20px var(--glow-tech), 0 0 40px var(--glow-tech);
}}
.bubble.art:hover, .bubble.art:focus-visible {{
  border-color: var(--accent-art);
  box-shadow: 0 4px 20px var(--glow-art), 0 0 40px var(--glow-art);
}}
.bubble .dot {{
  width: 12px;
  height: 12px;
  border-radius: 50%;
  flex-shrink: 0;
}}
.bubble.tech .dot {{ 
  background: var(--accent-tech); 
  box-shadow: 0 0 8px var(--glow-tech);
}}
.bubble.art .dot {{ 
  background: var(--accent-art);
  box-shadow: 0 0 8px var(--glow-art);
}}

.title {{ 
  font-weight: 700; 
  font-size: 15px; 
  line-height: 1.2; 
  font-family: 'Orbitron', sans-serif;
  letter-spacing: 0.5px;
}}
.subtitle {{ 
  font-size: 13px; 
  color: var(--muted); 
  margin-top: 3px; 
  font-weight: 400;
}}

/* Tooltip */
.bubble[data-tooltip]::after {{
  content: attr(data-tooltip);
  position: absolute;
  pointer-events: none;
  left: 12px;
  right: 12px;
  bottom: 100%;
  transform: translateY(-8px);
  background: #0b0f1a;
  border: 1px solid #2a3148;
  border-radius: 8px;
  padding: 8px 10px;
  color: var(--muted);
  opacity: 0;
  transition: opacity 120ms ease;
  white-space: normal;
  font-size: 12px;
}}
.bubble:hover::after, .bubble:focus-visible::after {{ opacity: 1; }}

/* Preview panel */
.preview {{
  position: sticky;
  top: 12px;
  margin-top: 16px;
  background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
  border: 1px solid #1f2937;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
}}
.preview .image {{
  width: 100%;
  aspect-ratio: 16/9;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-bottom: 1px solid #1f2937;
  position: relative;
}}
.preview .image::after {{
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(10, 14, 20, 0.8) 100%);
}}
.preview .content {{ padding: 16px; }}
.preview h3 {{ 
  margin: 0 0 6px 0; 
  font-size: 18px; 
  font-family: 'Orbitron', sans-serif;
  font-weight: 700;
  letter-spacing: 0.5px;
  background: linear-gradient(135deg, var(--accent-tech), var(--accent-art));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}}
.preview p {{ 
  margin: 6px 0; 
  color: var(--muted); 
  font-size: 14px; 
  line-height: 1.6;
}}
.preview .tag {{ 
  font-size: 11px; 
  color: var(--accent-tech); 
  background: rgba(0, 217, 255, 0.1); 
  padding: 4px 8px; 
  border-radius: 6px; 
  border: 1px solid rgba(0, 217, 255, 0.3);
  font-family: 'Orbitron', sans-serif;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}}

/* Responsive */
@media (max-width: 900px) {{
  .timeline-grid {{ grid-template-columns: 1fr; }}
  .spine {{ display: none; }}
  .era-cell {{ height: auto; min-height: 0; }}
  .era-label {{ position: static; margin-bottom: 12px; }}
  .bubble {{ height: auto; min-height: 72px; }}
}}
</style>

<div class="timeline-wrapper">
  <div class="timeline-grid" id="timeline-grid">
    <!-- Rows are injected by JS -->
    <div class="spine" aria-hidden="true"></div>
  </div>

  <div class="preview" id="preview">
    <div class="image" style="background-image:url('https://source.unsplash.com/1200x675/?history,art,technology');"></div>
    <div class="content">
      <h3>Explore the Creative Chain</h3>
      <p>Hover bubbles to see visuals and blurbs. Click to pin.</p>
      <p class="tag">Hint: Left = Technology, Right = Art</p>
    </div>
  </div>
</div>

<script>
(function() {{
  const DATA = {DATA_JSON};

  const grid = document.getElementById('timeline-grid');
  const spine = grid.querySelector('.spine');
  const preview = document.getElementById('preview');

  function setPreview(kind, item) {{
    const title = kind === 'tech' ? item.tech_title : item.art_title;
    const blurb = kind === 'tech' ? item.tech_blurb : item.art_blurb;
    const image = kind === 'tech' ? item.tech_image : item.art_image;
    const role  = kind === 'tech' ? 'Technological Disruption' : 'Artistic Disruption';

    preview.innerHTML = `
      <div class="image" style="background-image:url('${{image}}')"></div>
      <div class="content">
        <div class="tag">${{item.era}} • ${{role}}</div>
        <h3>${{title}}</h3>
        <p>${{blurb}}</p>
        <p><strong>Core Human Recalibration:</strong> ${{item.recalibration}}</p>
      </div>
    `;
  }}

  function createRow(item, idx) {{
    const rowStart = document.createElement('div');
    rowStart.className = 'row';

    // Left bubble (Tech)
    const leftCell = document.createElement('div');
    const techBtn = document.createElement('button');
    techBtn.className = 'bubble tech';
    techBtn.setAttribute('data-tooltip', item.tech_blurb);
    techBtn.setAttribute('aria-label', `${{item.era}} Technology: ${{item.tech_title}}`);
    techBtn.innerHTML = `<span class="dot"></span><div><div class="title">${{item.tech_title}}</div><div class="subtitle">${{item.tech_blurb}}</div></div>`;
    leftCell.appendChild(techBtn);

    // Era cell (spine + label)
    const eraCell = document.createElement('div');
    eraCell.className = 'era-cell';
    const spineDot = document.createElement('div');
    spineDot.className = 'spine-dot';
    const eraLabel = document.createElement('div');
    eraLabel.className = 'era-label';
    eraLabel.textContent = item.era;
    eraCell.appendChild(spineDot);
    eraCell.appendChild(eraLabel);

    // Right bubble (Art)
    const rightCell = document.createElement('div');
    const artBtn = document.createElement('button');
    artBtn.className = 'bubble art';
    artBtn.setAttribute('data-tooltip', item.art_blurb);
    artBtn.setAttribute('aria-label', `${{item.era}} Art: ${{item.art_title}}`);
    artBtn.innerHTML = `<span class="dot"></span><div><div class="title">${{item.art_title}}</div><div class="subtitle">${{item.art_blurb}}</div></div>`;
    rightCell.appendChild(artBtn);

    grid.insertBefore(leftCell, spine);
    grid.insertBefore(eraCell, spine);
    grid.insertBefore(rightCell, spine);

    const showTech = () => setPreview('tech', item);
    const showArt  = () => setPreview('art', item);

    techBtn.addEventListener('mouseenter', showTech);
    techBtn.addEventListener('focus', showTech);
    techBtn.addEventListener('click', showTech);

    artBtn.addEventListener('mouseenter', showArt);
    artBtn.addEventListener('focus', showArt);
    artBtn.addEventListener('click', showArt);
  }}

  DATA.forEach(createRow);
}})();
</script>
"""

components.html(html, height=1400, scrolling=True)

# Navigation section
st.divider()

st.markdown("""
### 🎯 Key Takeaway

Notice the pattern: Each technological disruption initially seems to threaten creative work, 
but humans adapt by focusing on what machines *can't* do—judgment, meaning-making, and value-based choices.

**Ready to explore how to think creatively with AI?**
""")

col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("streamlit_app.py")
with col2:
    if st.button("Continue to Phase 2 →", use_container_width=True, type="primary"):
        st.switch_page("pages/02_Phase_2_Prompting.py")

st.divider()
st.caption("🧬 The Creative Chain | Phase 1: Walkthrough of History")