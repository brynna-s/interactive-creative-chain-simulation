import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Creative Chain — Phase 1",
    page_icon="🧬",
    layout="wide",
)

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
        "tech_image": "https://source.unsplash.com/800x600/?printing-press,woodcut,typography,book",
        "art_image": "https://source.unsplash.com/800x600/?renaissance,leonardo,michelangelo,painting"
    },
    {
        "era": "1760s–1840s",
        "tech_title": "Industrial Revolution",
        "tech_blurb": "Mechanization, factories, steam power, and new urban life.",
        "art_title": "Romanticism",
        "art_blurb": "Reaction to mechanization; emotion and nature over rationalism.",
        "recalibration": "Artists reclaim feeling and individuality amid machine logic.",
        "tech_image": "https://source.unsplash.com/800x600/?industrial-revolution,factory,steam,loom",
        "art_image": "https://source.unsplash.com/800x600/?romanticism,landscape,storm,turner"
    },
    {
        "era": "1839–1900",
        "tech_title": "Photography",
        "tech_blurb": "Mechanical reproduction of images reshapes representation.",
        "art_title": "Impressionism & Post-Impressionism",
        "art_blurb": "Artists reimagine perception, color, and time.",
        "recalibration": "Art shifts from depiction to expression; creativity becomes interpretation.",
        "tech_image": "https://source.unsplash.com/800x600/?daguerreotype,early-photography,camera,plate",
        "art_image": "https://source.unsplash.com/800x600/?impressionism,monet,van-gogh,painting"
    },
    {
        "era": "1900–1930s",
        "tech_title": "Electricity, Mass Media, Telephone, Cinema",
        "tech_blurb": "Acceleration of communication and moving images.",
        "art_title": "Modernism / Cubism / Futurism",
        "art_blurb": "Fragmentation of perspective; fascination with speed and industry.",
        "recalibration": "Creativity explores abstraction and multiplicity of perception.",
        "tech_image": "https://source.unsplash.com/800x600/?cinema,telephone,radio,electricity",
        "art_image": "https://source.unsplash.com/800x600/?cubism,picasso,futurism,modernism"
    },
    {
        "era": "1940s–1960s",
        "tech_title": "Computing and Television",
        "tech_blurb": "Early digital systems and mass broadcast.",
        "art_title": "Pop Art & Conceptualism",
        "art_blurb": "Commentary on mass media and consumerism.",
        "recalibration": "Artists question originality and authorship itself.",
        "tech_image": "https://source.unsplash.com/800x600/?mainframe,early-computer,vacuum-tube,television",
        "art_image": "https://source.unsplash.com/800x600/?pop-art,warhol,conceptual-art"
    },
    {
        "era": "1980s–1990s",
        "tech_title": "Personal Computer & Internet",
        "tech_blurb": "Democratization of creation and distribution.",
        "art_title": "Digital Art, Net Art, Cyberpunk",
        "art_blurb": "Code, networks, and the virtual as medium.",
        "recalibration": "Creativity blends with computation; new digital subjectivity emerges.",
        "tech_image": "https://source.unsplash.com/800x600/?personal-computer,retro-computer,90s,crt",
        "art_image": "https://source.unsplash.com/800x600/?cyberpunk,net-art,digital-art"
    },
    {
        "era": "2000s–2010s",
        "tech_title": "Smartphone, Social Media, Algorithms",
        "tech_blurb": "Always-on creation and algorithmic curation.",
        "art_title": "Post-Internet Art & Remix Culture",
        "art_blurb": "Curation, meme-making, participatory art.",
        "recalibration": "Creativity becomes collective, iterative, and ephemeral.",
        "tech_image": "https://source.unsplash.com/800x600/?smartphone,social-media,algorithm",
        "art_image": "https://source.unsplash.com/800x600/?meme,remix,glitch-art"
    },
    {
        "era": "2020s–Present",
        "tech_title": "Generative AI, Automation, Synthetic Data",
        "tech_blurb": "Models generate text, image, audio, code on demand.",
        "art_title": "AI Art, Prompt-based Creativity",
        "art_blurb": "Synthetic imagination and human-in-the-loop authorship.",
        "recalibration": "Creativity shifts to curation, prompting, and ethical direction.",
        "tech_image": "https://source.unsplash.com/800x600/?ai,neural-network,generative,robot",
        "art_image": "https://source.unsplash.com/800x600/?ai-art,generative-art,prompt-art"
    },
]

# Legend and layout spacer
left, mid, right = st.columns([1, 0.4, 1])
with left:
    st.markdown("**Technological Disruptions**")
with mid:
    st.markdown(" ")
with right:
    st.markdown("**Artistic Disruptions**")

# Build interactive HTML/CSS/JS timeline
DATA_JSON = json.dumps(TIMELINE_ITEMS)

html = f"""
<style>
:root {{
  --bg: #0f1116;
  --panel: #141824;
  --text: #e6eaf2;
  --muted: #9aa4b2;
  --accent-tech: #56b6c2;
  --accent-art: #c678dd;
  --spine: #2d3347;
  --bubble-hover: #ffffff22;
}}

* {{ box-sizing: border-box; }}

.timeline-wrapper {{
  width: 100%;
  margin: 0 auto;
  color: var(--text);
  background: linear-gradient(180deg, #0f1116 0%, #0f1116cc 100%);
  border-radius: 12px;
  padding: 12px 12px 0 12px;
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
  width: 3px;
  top: 0;
  bottom: 0;
  background: linear-gradient(var(--spine), #3a415c);
  border-radius: 2px;
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
  width: 14px;
  height: 14px;
  background: #6671a4;
  border: 3px solid #0f1116;
  border-radius: 50%;
  z-index: 2;
  box-shadow: 0 0 0 4px #6671a433;
}}
.era-label {{
  position: relative;
  top: 28px;
  font-size: 12px;
  color: var(--muted);
  text-align: center;
  white-space: nowrap;
}}

.bubble {{
  position: relative;
  height: 92px;
  padding: 0 8px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-radius: 12px;
  border: 1px solid #2a3148;
  background: #151a28;
  color: var(--text);
  cursor: pointer;
  transition: transform 120ms ease, background 120ms ease, border-color 120ms ease;
  text-align: left;
  width: 100%;
  outline: none;
}}
.bubble:hover, .bubble:focus-visible {{
  transform: translateY(-1px);
  background: #1a2032;
  border-color: #3a4566;
}}
.bubble .dot {{
  width: 14px;
  height: 14px;
  border-radius: 50%;
  flex-shrink: 0;
}}
.bubble.tech .dot {{ background: var(--accent-tech); box-shadow: 0 0 0 4px #56b6c233; }}
.bubble.art  .dot {{ background: var(--accent-art);  box-shadow: 0 0 0 4px #c678dd33; }}

.title {{ font-weight: 700; font-size: 14px; line-height: 1.2; }}
.subtitle {{ font-size: 12px; color: var(--muted); margin-top: 2px; }}

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
  background: #0b0f1a;
  border: 1px solid #2a3148;
  border-radius: 12px;
  overflow: hidden;
}}
.preview .image {{
  width: 100%;
  aspect-ratio: 16/9;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-bottom: 1px solid #2a3148;
}}
.preview .content {{ padding: 14px; }}
.preview h3 {{ margin: 0 0 4px 0; font-size: 16px; }}
.preview p  {{ margin: 4px 0; color: var(--muted); font-size: 13px; }}
.preview .tag {{ font-size: 11px; color: #aeb7c6; background: #1a2032; padding: 2px 6px; border-radius: 6px; border: 1px solid #2a3148; }}

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
      <div class="image" style="background-image:url('${image}')"></div>
      <div class="content">
        <div class="tag">${item.era} • ${role}</div>
        <h3>${title}</h3>
        <p>${blurb}</p>
        <p><strong>Core Human Recalibration:</strong> ${item.recalibration}</p>
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
    techBtn.setAttribute('aria-label', `${item.era} Technology: ${item.tech_title}`);
    techBtn.innerHTML = `<span class="dot"></span><div><div class="title">${item.tech_title}</div><div class="subtitle">${item.tech_blurb}</div></div>`;
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
    artBtn.setAttribute('aria-label', `${item.era} Art: ${item.art_title}`);
    artBtn.innerHTML = `<span class="dot"></span><div><div class="title">${item.art_title}</div><div class="subtitle">${item.art_blurb}</div></div>`;
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
