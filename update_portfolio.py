# update_portfolio.py
import re

with open('app/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update body and html CSS: allow smooth vertical scrolling
old_body_css = """html, body { height: 100%; }

body {
  font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: var(--red-orange);
  overflow: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}"""

new_body_css = """html {
  height: 100%;
  scroll-behavior: smooth;
  background: #000000;
}

body {
  font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #000000;
  overflow-x: hidden;
  overflow-y: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  scroll-behavior: smooth;
}"""

if old_body_css in content:
    content = content.replace(old_body_css, new_body_css)
else:
    print("WARNING: old_body_css not matched verbatim, performing regex replace")
    content = re.sub(
        r'html,\s*body\s*\{[^}]*height:\s*100%[^}]*\}\s*body\s*\{[^}]*overflow:\s*hidden;[^}]*\}',
        new_body_css,
        content
    )

# 2. Make .page height exactly 100dvh
old_page_css = """  height: 100dvh;
  width: 100%;
  overflow: hidden;"""
new_page_css = """  min-height: 100dvh;
  height: 100dvh;
  width: 100%;
  overflow: hidden;"""
content = content.replace(old_page_css, new_page_css)

# Add custom CSS for About Section and Project Stacking Cards
custom_sections_css = """
/* ============================================================
   SECTION 2: ABOUT ME SECTION (Pure Black & Vibrant Red-Orange)
   ============================================================ */

.about-section {
  position: relative;
  min-height: 100vh;
  width: 100%;
  background: #000000;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6rem 1.5rem 7rem;
  overflow: hidden;
  cursor: pointer; /* Click anywhere indicator */
}

.about-ambient-glow {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 65vw;
  height: 60vh;
  background: radial-gradient(circle, rgba(255, 77, 0, 0.16) 0%, rgba(255, 77, 0, 0.04) 45%, transparent 70%);
  pointer-events: none;
  filter: blur(40px);
}

.about-bg-grid {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255, 255, 255, 0.07) 1.2px, transparent 1.2px);
  background-size: 36px 36px;
  opacity: 0.6;
  pointer-events: none;
}

.about-container {
  position: relative;
  z-index: 2;
  max-width: 900px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 2.2rem;
}

.about-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.45rem 1.25rem;
  background: rgba(255, 77, 0, 0.12);
  border: 1px solid rgba(255, 77, 0, 0.45);
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: #FF4D00;
  text-transform: uppercase;
}

.badge-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #FF4D00;
  box-shadow: 0 0 10px #FF4D00;
  animation: pulse-dot 2s infinite ease-in-out;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.8); }
}

.about-heading {
  font-family: "Dela Gothic One", sans-serif;
  font-size: clamp(3.2rem, 9.5vw, 7.5rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 0.95;
  text-transform: uppercase;
  background: linear-gradient(180deg, #ffffff 15%, #FF4D00 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0;
  filter: drop-shadow(0 4px 20px rgba(255, 77, 0, 0.25));
}

.about-card {
  position: relative;
  background: rgba(18, 19, 24, 0.82);
  border: 1.5px solid rgba(255, 255, 255, 0.14);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 36px;
  padding: 2.75rem 2.5rem;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 77, 0, 0.1);
  transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
  cursor: default;
}

.about-card:hover {
  border-color: rgba(255, 77, 0, 0.45);
  box-shadow: 0 35px 90px rgba(0, 0, 0, 0.9), 0 0 40px rgba(255, 77, 0, 0.18);
}

.about-text {
  font-size: clamp(1.1rem, 2vw, 1.45rem);
  line-height: 1.7;
  font-weight: 500;
  color: #eaecef;
  letter-spacing: -0.01em;
  margin-bottom: 2rem;
  text-wrap: pretty;
}

.about-meta-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem 2.5rem;
  padding-top: 1.8rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.meta-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  text-align: left;
}

.meta-label {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: #FF4D00;
  text-transform: uppercase;
}

.meta-val {
  font-size: 0.95rem;
  font-weight: 600;
  color: #ffffff;
}

.about-actions {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.5rem;
  margin-top: 0.5rem;
}

.explore-projects-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.85rem;
  padding: 1.15rem 2.8rem;
  background: linear-gradient(135deg, #FF4D00 0%, #e03f00 100%);
  color: #ffffff;
  border: 2px solid rgba(255, 255, 255, 0.35);
  border-radius: 9999px;
  font-family: "Dela Gothic One", sans-serif;
  font-size: clamp(0.95rem, 1.4vw, 1.15rem);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 12px 35px rgba(255, 77, 0, 0.42), 0 0 20px rgba(255, 77, 0, 0.3) inset;
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.25s ease, filter 0.25s ease;
}

.explore-projects-btn:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 18px 45px rgba(255, 77, 0, 0.6), 0 0 28px rgba(255, 77, 0, 0.45) inset;
  filter: brightness(1.1);
}

.click-anywhere-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.6rem 1.4rem;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: rgba(255, 255, 255, 0.7);
  text-transform: uppercase;
  cursor: pointer;
  animation: bounce-subtle 2.5s infinite ease-in-out;
  transition: all 0.25s ease;
}

.click-anywhere-pill:hover {
  background: rgba(255, 77, 0, 0.18);
  border-color: #FF4D00;
  color: #ffffff;
}

@keyframes bounce-subtle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(6px); }
}

/* ============================================================
   SECTION 3: PROJECT STACKING CARDS (Red-Orange, Black & White)
   ============================================================ */

.projects-section {
  position: relative;
  min-height: 100vh;
  width: 100%;
  background: #0C0C0C;
  color: #ffffff;
  padding: 6.5rem 1.5rem 8rem;
  overflow: clip;
}

.projects-ambient-glow {
  position: absolute;
  top: 10%;
  left: 50%;
  transform: translateX(-50%);
  width: 80vw;
  height: 50vh;
  background: radial-gradient(ellipse at center, rgba(255, 77, 0, 0.14) 0%, transparent 65%);
  pointer-events: none;
  filter: blur(50px);
}

.projects-header-wrap {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 900px;
  margin: 0 auto 5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.projects-eyebrow {
  display: inline-block;
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.22em;
  color: #FF4D00;
  text-transform: uppercase;
}

.projects-massive-title {
  font-family: "Dela Gothic One", sans-serif;
  font-size: clamp(3.8rem, 12.5vw, 9.5rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 0.92;
  text-transform: uppercase;
  background: linear-gradient(180deg, #ffffff 20%, #7d8594 70%, #2f3440 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0;
  filter: drop-shadow(0 6px 30px rgba(0, 0, 0, 0.7));
}

.projects-subtitle {
  font-size: clamp(0.95rem, 1.6vw, 1.3rem);
  font-weight: 500;
  color: rgba(255, 255, 255, 0.65);
  letter-spacing: 0.02em;
  max-width: 600px;
  margin-top: 0.5rem;
}

/* Stacking Cards Container */
.cards-stack-container {
  display: flex;
  flex-direction: column;
  gap: 3.5rem;
  max-width: 1140px;
  margin: 0 auto;
  position: relative;
  padding-bottom: 5rem;
}

/* Sticky Stacking Card */
.stack-card {
  position: -webkit-sticky;
  position: sticky;
  top: calc(90px + var(--card-idx) * 9px);
  z-index: calc(10 + var(--card-idx));
  background: #14151a;
  border: 2px solid rgba(255, 255, 255, 0.18);
  border-radius: 46px;
  padding: 2.25rem 2.5rem;
  box-shadow: 0 25px 65px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 77, 0, 0.12);
  transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.3s ease, box-shadow 0.3s ease;
  margin-bottom: 2rem;
  overflow: hidden;
}

.stack-card:hover {
  border-color: #FF4D00;
  box-shadow: 0 30px 75px rgba(0, 0, 0, 0.9), 0 0 35px rgba(255, 77, 0, 0.25);
}

.card-inner {
  display: flex;
  flex-direction: column;
  gap: 1.8rem;
}

.card-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.card-num-col {
  display: flex;
  align-items: center;
  gap: 1.4rem;
}

.card-num {
  font-family: "Dela Gothic One", sans-serif;
  font-size: clamp(2.8rem, 6vw, 4.5rem);
  font-weight: 900;
  line-height: 0.9;
  color: #FF4D00;
  letter-spacing: -0.05em;
  text-shadow: 0 0 25px rgba(255, 77, 0, 0.35);
}

.card-title-col {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.card-cat-badge {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.2em;
  color: #FF4D00;
  text-transform: uppercase;
}

.card-title {
  font-family: "Syne", "Plus Jakarta Sans", sans-serif;
  font-size: clamp(1.2rem, 2.4vw, 2.1rem);
  font-weight: 800;
  color: #ffffff;
  letter-spacing: -0.02em;
  line-height: 1.15;
  margin: 0;
  text-transform: uppercase;
}

.card-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.65rem 1.4rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1.5px solid rgba(255, 255, 255, 0.22);
  border-radius: 9999px;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #ffffff;
  text-transform: uppercase;
  margin-left: auto;
  transition: all 0.25s ease;
}

.stack-card:hover .card-status-pill {
  border-color: #FF4D00;
  background: rgba(255, 77, 0, 0.15);
  color: #ffffff;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #FF4D00;
  box-shadow: 0 0 8px #FF4D00;
}

.card-slot-wrap {
  width: 100%;
}

.card-slot-frame {
  position: relative;
  background: linear-gradient(135deg, rgba(255, 77, 0, 0.04) 0%, rgba(20, 21, 26, 0.6) 100%);
  border: 1.5px dashed rgba(255, 77, 0, 0.35);
  border-radius: 30px;
  padding: 2.5rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  flex-wrap: wrap;
  transition: border-color 0.3s ease, background 0.3s ease;
}

.stack-card:hover .card-slot-frame {
  border-color: rgba(255, 77, 0, 0.65);
  background: linear-gradient(135deg, rgba(255, 77, 0, 0.08) 0%, rgba(20, 21, 26, 0.8) 100%);
}

.slot-left-group {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.slot-icon {
  width: 48px;
  height: 48px;
  border-radius: 16px;
  background: rgba(255, 77, 0, 0.16);
  border: 1px solid rgba(255, 77, 0, 0.4);
  color: #FF4D00;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  flex-shrink: 0;
}

.slot-content {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.slot-title {
  font-size: clamp(0.95rem, 1.4vw, 1.15rem);
  font-weight: 800;
  letter-spacing: 0.1em;
  color: #ffffff;
  text-transform: uppercase;
  margin: 0;
}

.slot-desc {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.55);
  margin: 0;
}

.slot-badge-pill {
  padding: 0.45rem 1.1rem;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 9999px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: rgba(255, 255, 255, 0.7);
  text-transform: uppercase;
}

/* Projects Footer */
.projects-footer {
  max-width: 1140px;
  margin: 4rem auto 0;
  padding-top: 3rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.footer-tagline {
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: rgba(255, 255, 255, 0.45);
  text-transform: uppercase;
  margin: 0;
}

.back-to-top-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.75rem 1.6rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1.5px solid rgba(255, 255, 255, 0.2);
  border-radius: 9999px;
  font-family: "Dela Gothic One", sans-serif;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  color: #ffffff;
  text-transform: uppercase;
  text-decoration: none;
  transition: all 0.25s ease;
}

.back-to-top-btn:hover {
  background: #FF4D00;
  border-color: #FF4D00;
  box-shadow: 0 0 25px rgba(255, 77, 0, 0.5);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .about-card { padding: 2rem 1.5rem; }
  .stack-card { padding: 1.75rem 1.5rem; border-radius: 36px; }
  .card-top-row { flex-direction: column; align-items: flex-start; }
  .card-status-pill { margin-left: 0; }
  .card-slot-frame { padding: 1.75rem 1.25rem; }
  .projects-footer { flex-direction: column; text-align: center; }
}
"""

# Insert custom_sections_css into styles before </style>
content = content.replace("</style>", custom_sections_css + "\n</style>")

# 3. Build the 15 project cards
slides = [
  ('01', 'ACADEMIC MILESTONES', 'Stars & Recognitions Collected', 'HONORS & BADGES'),
  ('02', 'LAB ENGAGEMENT', 'Interactive Laboratory Sessions', 'HANDS-ON EXPERIMENTS'),
  ('03', 'CLASSROOM PARTICIPATION', 'Interactive Sessions in Class', 'THEORY & ENGAGEMENT'),
  ('04', 'CONTINUOUS LEARNING', 'Knowledge Acquired Through Homework', 'DEEP EXPLORATION'),
  ('05', 'MENTORSHIP & COLLABORATION', 'Personal Interaction & Faculty Guidance', '1-ON-1 SESSIONS'),
  ('06', 'TECHNICAL WRITING', 'Medium Engineering Blog Publication', 'RESEARCH ARTICLES'),
  ('07', 'CODE REPOSITORY', 'Project Demonstration (GitHub)', 'OPEN SOURCE REPO'),
  ('08', 'SYSTEM DOCUMENTATION', 'Comprehensive Project Write-Up', 'TECHNICAL REPORT'),
  ('09', 'PRODUCTION RELEASE', 'Deployed Application & Presentation (PPTX)', 'LIVE APP & SLIDES'),
  ('10', 'VISUAL WALKTHROUGH', 'High-Definition Project Demo Video', 'VIDEO WALKTHROUGH'),
  ('11', 'ADVANCED RESEARCH', 'Case Study: FAISS Vector Similarity Engine', 'AI & VECTOR SEARCH'),
  ('12', 'UNFORGETTABLE EXPERIENCES', 'The Chaotic Classroom Episode I Was Involved In', 'CLASSROOM MEMORIES'),
  ('13', 'REFLECTIONS & DIALOGUE', 'Memorable Personal Faculty Interaction', 'REFLECTIVE DIALOGUE'),
  ('14', 'PERSPECTIVES & CURIOSITY', 'Things I Wonder About My Faculty', 'FACULTY PERSPECTIVES'),
  ('15', 'MULTIMODAL MEDIA', 'Project Audio Recording & Commentary', 'AUDIO PRODUCTION')
]

cards_stack_html = []
for idx, (num, cat, title, badge) in enumerate(slides):
    card = f'''      <!-- Slide {num} -->
      <article class="stack-card" style="--card-idx: {idx};">
        <div class="card-inner">
          <div class="card-top-row">
            <div class="card-num-col">
              <span class="card-num">{num}</span>
              <div class="card-title-col">
                <span class="card-cat-badge">{cat}</span>
                <h3 class="card-title">{title}</h3>
              </div>
            </div>
            <div class="card-status-pill">
              <span class="status-dot"></span>
              <span>SLIDE {num}</span>
            </div>
          </div>
          <div class="card-slot-wrap">
            <div class="card-slot-frame">
              <div class="slot-left-group">
                <div class="slot-icon">✦</div>
                <div class="slot-content">
                  <h4 class="slot-title">SLIDE {num} READY</h4>
                  <p class="slot-desc">Awaiting detailed context and media attachment for this slide.</p>
                </div>
              </div>
              <div class="slot-badge-pill">{badge}</div>
            </div>
          </div>
        </div>
      </article>'''
    cards_stack_html.append(card)

cards_full_html = "\n\n".join(cards_stack_html)

# 4. Construct Section 2 and Section 3 HTML
sections_html = f'''
<!-- ============================================================
     SECTION 2: ABOUT ME SECTION (Pure Black & Red-Orange Glow)
     ============================================================ -->
<section id="about-section" class="about-section" aria-label="About Me">
  <div class="about-bg-grid"></div>
  <div class="about-ambient-glow"></div>

  <div class="about-container">
    <div class="about-badge">
      <span class="badge-dot"></span>
      <span>ABOUT ME</span>
    </div>

    <h2 class="about-heading">ABOUT ME</h2>

    <div class="about-card" id="aboutCard">
      <p class="about-text">
        I am a Computer Science Engineering student with a strong interest in programming, technology, and problem-solving. I enjoy exploring Python and developing practical applications that turn ideas into meaningful solutions. I am continuously learning new technologies and improving my technical skills through hands-on projects and practical experiences.
      </p>

      <div class="about-meta-row">
        <div class="meta-item">
          <span class="meta-label">DISCIPLINE</span>
          <span class="meta-val">Computer Science & Engineering</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">SPECIALIZATION</span>
          <span class="meta-val">Advanced Python & AI Systems</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">PORTFOLIO</span>
          <span class="meta-val">CSI3007 Digital Assignments</span>
        </div>
      </div>
    </div>

    <div class="about-actions">
      <button type="button" class="explore-projects-btn" id="exploreProjectBtn" aria-label="Explore Projects">
        <span>LET&apos;S EXPLORE</span>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
          <line x1="5" y1="12" x2="19" y2="12"></line>
          <polyline points="12 5 19 12 12 19"></polyline>
        </svg>
      </button>
    </div>

    <div class="click-anywhere-pill" id="clickAnywhereBtn" title="Click anywhere on this screen to go to Projects">
      <span class="badge-dot" style="width:5px; height:5px;"></span>
      <span>CLICK ANYWHERE TO EXPLORE</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <line x1="12" y1="5" x2="12" y2="19"></line>
        <polyline points="19 12 12 19 5 12"></polyline>
      </svg>
    </div>
  </div>
</section>

<!-- ============================================================
     SECTION 3: PROJECT STACKING CARDS SECTION
     ============================================================ -->
<section id="projects-section" class="projects-section" aria-label="Projects Archive">
  <div class="projects-ambient-glow"></div>

  <div class="projects-header-wrap">
    <span class="projects-eyebrow">PORTFOLIO ARCHIVE</span>
    <h2 class="projects-massive-title">PROJECT</h2>
    <p class="projects-subtitle">15 Key Milestones, Laboratory Systems & Academic Experiences</p>
  </div>

  <div class="cards-stack-container">
{cards_full_html}
  </div>

  <footer class="projects-footer">
    <p class="footer-tagline">VIKNESH G &mdash; ADVANCED PYTHON PROGRAMMING PORTFOLIO</p>
    <a href="#hero-section" class="back-to-top-btn" id="backToTopBtn" aria-label="Back to Top">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
        <line x1="12" y1="19" x2="12" y2="5"></line>
        <polyline points="5 12 12 5 19 12"></polyline>
      </svg>
      <span>BACK TO TOP</span>
    </a>
  </footer>
</section>
'''

# Replace closing of hero section
# Find the exact hero section closing
hero_closing = '</section>'
first_closing_pos = content.find(hero_closing)
if first_closing_pos != -1:
    content = content[:first_closing_pos + len(hero_closing)] + "\n" + sections_html + "\n" + content[first_closing_pos + len(hero_closing):]
    print("Successfully inserted Section 2 and Section 3 after hero section!")
else:
    print("ERROR: could not find hero section closing tag")

# 5. Update JavaScript event handlers for explorerBtn and new buttons
old_explorer_js = """  /* ---- EXPLORER button interaction ---- */
  var explorerBtn = document.getElementById('explorerBtn');
  if (explorerBtn) {
    explorerBtn.addEventListener('click', function () {
      setDrawer(true);
    });
  }"""

new_navigation_js = """  /* ---- Navigation Event Handlers ---- */
  var explorerBtn = document.getElementById('explorerBtn');
  if (explorerBtn) {
    explorerBtn.addEventListener('click', function (e) {
      e.preventDefault();
      var aboutSec = document.getElementById('about-section');
      if (aboutSec) {
        aboutSec.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  var exploreProjectBtn = document.getElementById('exploreProjectBtn');
  if (exploreProjectBtn) {
    exploreProjectBtn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var projSec = document.getElementById('projects-section');
      if (projSec) {
        projSec.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  var clickAnywhereBtn = document.getElementById('clickAnywhereBtn');
  if (clickAnywhereBtn) {
    clickAnywhereBtn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var projSec = document.getElementById('projects-section');
      if (projSec) {
        projSec.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  var aboutSec = document.getElementById('about-section');
  if (aboutSec) {
    aboutSec.addEventListener('click', function (e) {
      // If click was on background or card (not a button)
      if (!e.target.closest('button, a')) {
        var projSec = document.getElementById('projects-section');
        if (projSec) {
          projSec.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  }

  var backToTopBtn = document.getElementById('backToTopBtn');
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }"""

if old_explorer_js in content:
    content = content.replace(old_explorer_js, new_navigation_js)
    print("Replaced old explorer JS with smooth scroll navigation!")
else:
    print("WARNING: old_explorer_js not found verbatim, appending handlers before closing script")
    content = content.replace("})();", new_navigation_js + "\n})();")

# Add id="hero-section" to .page if not present
if 'id="hero-section"' not in content:
    content = content.replace('class="page"', 'class="page" id="hero-section"')

# Write updated file to app/index.html and marcus-bennet-pull-light.html
with open('app/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated app/index.html successfully!")

with open('marcus-bennet-pull-light.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated marcus-bennet-pull-light.html successfully!")

