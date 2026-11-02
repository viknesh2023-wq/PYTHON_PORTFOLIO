# refine_portfolio.py
import re

with open('app/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. OVERHAUL ABOUT ME SECTION:
# Left-aligned, top-left corner, pure white heading, plain pure white text,
# NO box/card, NO metadata, NO explore button,
# bottom-middle non-bold "TOUCH TO REDIRECT FOR THE NEXT ONE ↓"
# ---------------------------------------------------------------------------

old_about_section = re.search(r'<section id="about-section".*?</section>', content, re.DOTALL)
if old_about_section:
    old_about_html = old_about_section.group(0)
    print("Found old about section, length:", len(old_about_html))
else:
    print("ERROR: could not find old about section")

new_about_html = """<section id="about-section" class="about-section" aria-label="About Me">
  <div class="about-bg-grid"></div>

  <!-- Top-left content block (completely plain, no card, pure white text) -->
  <div class="about-top-content">
    <h2 class="about-heading-white">ABOUT ME</h2>
    <p class="about-text-white">
      I am a Computer Science Engineering student with a strong interest in programming, technology, and problem-solving. I enjoy exploring Python and developing practical applications that turn ideas into meaningful solutions. I am continuously learning new technologies and improving my technical skills through hands-on projects and practical experiences.
    </p>
  </div>

  <!-- Bottom-middle subtle non-bold prompt -->
  <div class="about-bottom-prompt" id="aboutTouchPrompt">
    <span>TOUCH TO REDIRECT FOR THE NEXT ONE</span>
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <line x1="12" y1="5" x2="12" y2="19"></line>
      <polyline points="19 12 12 19 5 12"></polyline>
    </svg>
  </div>
</section>"""

content = content.replace(old_about_html, new_about_html)

# ---------------------------------------------------------------------------
# 2. OVERHAUL PROJECT SECTION:
# Remove "15 milestone", reduce size of all text, make titles pure white,
# reduce boldness and color intensity
# ---------------------------------------------------------------------------

old_proj_header = re.search(r'<div class="projects-header-wrap">.*?</div>', content, re.DOTALL)
if old_proj_header:
    old_proj_header_html = old_proj_header.group(0)
    new_proj_header_html = """<div class="projects-header-wrap">
    <span class="projects-eyebrow">PORTFOLIO ARCHIVE</span>
    <h2 class="projects-massive-title">PROJECT</h2>
  </div>"""
    content = content.replace(old_proj_header_html, new_proj_header_html)
    print("Replaced project header (removed 15 milestone subtitle)!")

# Re-generate cards with reduced text sizes, pure white titles, lighter weight, and subtle styling
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

old_cards_container = re.search(r'<div class="cards-stack-container">.*?</div>\s*<footer', content, re.DOTALL)
if old_cards_container:
    content = content[:old_cards_container.start()] + '<div class="cards-stack-container">\n' + cards_full_html + '\n  </div>\n\n  <footer' + content[old_cards_container.end():]
    print("Replaced cards container with refined slides!")

# ---------------------------------------------------------------------------
# 3. UPDATE CSS FOR ABOUT SECTION & PROJECT SECTION:
# - About section: top-left aligned, pure white heading, plain pure white text,
#   no card box, bottom-middle subtle prompt.
# - Project section: reduced sizes, pure white titles, lighter weights, reduced intensity.
# - Light/Dark toggle support:
#   Light ON: vibrant orange background on hero, white typography.
#   Light OFF: dark/black background, orange accents, white text.
# ---------------------------------------------------------------------------

new_refined_css = """
/* ============================================================
   SECTION 2: ABOUT ME SECTION (Pure Black, Top-Left Plain White)
   ============================================================ */

.about-section {
  position: relative;
  min-height: 100vh;
  width: 100%;
  background: #000000;
  color: #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  padding: 6.5rem 2rem 3.5rem;
  overflow: hidden;
  cursor: pointer; /* Click anywhere redirects to project */
}

@media (min-width: 640px) {
  .about-section {
    padding: 7.5rem 4.5rem 4rem;
  }
}

@media (min-width: 1024px) {
  .about-section {
    padding: 8.5rem 6.5rem 4.5rem;
  }
}

.about-bg-grid {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255, 255, 255, 0.05) 1.2px, transparent 1.2px);
  background-size: 38px 38px;
  opacity: 0.45;
  pointer-events: none;
}

.about-top-content {
  position: relative;
  z-index: 2;
  max-width: 1020px;
  width: 100%;
  text-align: left;
}

/* Heading: Complete White in TOKA format, at top-left */
.about-heading-white {
  font-family: "Dela Gothic One", sans-serif;
  font-size: clamp(2.8rem, 6.5vw, 5.2rem);
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1;
  text-transform: uppercase;
  color: #ffffff; /* PURE COMPLETE WHITE */
  margin: 0 0 2rem 0;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
}

/* Paragraph: Complete Plain White text beneath heading, NO card box */
.about-text-white {
  font-family: "Plus Jakarta Sans", sans-serif;
  font-size: clamp(1.1rem, 1.8vw, 1.4rem);
  line-height: 1.75;
  font-weight: 400; /* Normal readable format */
  color: #ffffff; /* PURE COMPLETE WHITE */
  letter-spacing: -0.01em;
  margin: 0;
  text-wrap: pretty;
  max-width: 900px;
}

/* Bottom-middle: Non-bold touch to redirect prompt */
.about-bottom-prompt {
  position: relative;
  z-index: 2;
  align-self: center;
  margin: 4rem auto 0;
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  font-family: "Plus Jakarta Sans", sans-serif;
  font-weight: 300; /* VERY NON-BOLD */
  font-size: 0.78rem;
  letter-spacing: 0.24em;
  color: rgba(255, 255, 255, 0.65);
  text-transform: uppercase;
  cursor: pointer;
  animation: bounce-subtle 2.5s infinite ease-in-out;
  transition: color 0.25s ease;
  user-select: none;
}

.about-bottom-prompt:hover {
  color: #ffffff;
}

@keyframes bounce-subtle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(6px); }
}

/* ============================================================
   SECTION 3: PROJECT SECTION (Refined Sizes, Reduced Intensity)
   ============================================================ */

.projects-section {
  position: relative;
  min-height: 100vh;
  width: 100%;
  background: #0C0C0C;
  color: #ffffff;
  padding: 5.5rem 1.5rem 7rem;
  overflow: clip;
}

.projects-header-wrap {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 900px;
  margin: 0 auto 3.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.projects-eyebrow {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: #FF4D00;
  text-transform: uppercase;
}

.projects-massive-title {
  font-family: "Dela Gothic One", sans-serif;
  font-size: clamp(2.8rem, 7.5vw, 5.5rem); /* Reduced size */
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1;
  text-transform: uppercase;
  color: #ffffff; /* PURE WHITE */
  margin: 0;
}

/* Stacking Cards Container */
.cards-stack-container {
  display: flex;
  flex-direction: column;
  gap: 2.5rem; /* Reduced gap */
  max-width: 1040px; /* Refined max-width */
  margin: 0 auto;
  position: relative;
  padding-bottom: 4rem;
}

/* Sticky Stacking Card: Reduced padding, subtle border */
.stack-card {
  position: -webkit-sticky;
  position: sticky;
  top: calc(85px + var(--card-idx) * 8px);
  z-index: calc(10 + var(--card-idx));
  background: #14151a;
  border: 1px solid rgba(255, 255, 255, 0.14); /* Reduced intensity border */
  border-radius: 32px; /* Sleeker radius */
  padding: 1.6rem 2rem; /* Reduced size */
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.75);
  transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
  margin-bottom: 1.5rem;
  overflow: hidden;
}

.stack-card:hover {
  border-color: rgba(255, 77, 0, 0.6);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85), 0 0 25px rgba(255, 77, 0, 0.18);
}

.card-inner {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.card-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.2rem;
  flex-wrap: wrap;
}

.card-num-col {
  display: flex;
  align-items: center;
  gap: 1.1rem;
}

/* Reduced size of number */
.card-num {
  font-family: "Dela Gothic One", sans-serif;
  font-size: clamp(1.8rem, 3.2vw, 2.5rem); /* Reduced size */
  font-weight: 800;
  line-height: 1;
  color: #ffffff; /* PURE WHITE NUMBER */
  letter-spacing: -0.04em;
}

.card-title-col {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.card-cat-badge {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #FF4D00; /* Subtle orange badge */
  text-transform: uppercase;
}

/* Reduced size and weight of Title: Pure White */
.card-title {
  font-family: "Plus Jakarta Sans", "Syne", sans-serif;
  font-size: clamp(0.95rem, 1.4vw, 1.25rem); /* Reduced size */
  font-weight: 600; /* NOT OVERLY BOLD */
  color: #ffffff; /* PURE COMPLETE WHITE */
  letter-spacing: 0.01em;
  line-height: 1.25;
  margin: 0;
  text-transform: uppercase;
}

.card-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.45rem 1rem;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 9999px;
  font-size: 0.7rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  color: rgba(255, 255, 255, 0.7);
  text-transform: uppercase;
  margin-left: auto;
  transition: all 0.2s ease;
}

.stack-card:hover .card-status-pill {
  border-color: #FF4D00;
  color: #ffffff;
}

.status-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #FF4D00;
}

/* Card Slot Frame: Compact & subtle */
.card-slot-wrap {
  width: 100%;
}

.card-slot-frame {
  position: relative;
  background: rgba(255, 255, 255, 0.02);
  border: 1px dashed rgba(255, 255, 255, 0.15); /* Subtle white dashed border */
  border-radius: 20px;
  padding: 1.35rem 1.6rem; /* Compact height */
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  transition: border-color 0.25s ease, background 0.25s ease;
}

.stack-card:hover .card-slot-frame {
  border-color: rgba(255, 77, 0, 0.4);
  background: rgba(255, 77, 0, 0.03);
}

.slot-left-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.slot-icon {
  width: 36px;
  height: 36px;
  border-radius: 12px;
  background: rgba(255, 77, 0, 0.12);
  border: 1px solid rgba(255, 77, 0, 0.3);
  color: #FF4D00;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.slot-content {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.slot-title {
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: #ffffff; /* PURE WHITE */
  text-transform: uppercase;
  margin: 0;
}

.slot-desc {
  font-size: 0.78rem;
  color: rgba(255, 255, 255, 0.5);
  margin: 0;
}

.slot-badge-pill {
  padding: 0.35rem 0.9rem;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 9999px;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  color: rgba(255, 255, 255, 0.6);
  text-transform: uppercase;
}

/* Projects Footer */
.projects-footer {
  max-width: 1040px;
  margin: 3.5rem auto 0;
  padding-top: 2.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.footer-tagline {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  color: rgba(255, 255, 255, 0.4);
  text-transform: uppercase;
  margin: 0;
}

.back-to-top-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 1.4rem;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 9999px;
  font-family: "Dela Gothic One", sans-serif;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  color: #ffffff;
  text-transform: uppercase;
  text-decoration: none;
  transition: all 0.2s ease;
}

.back-to-top-btn:hover {
  background: #FF4D00;
  border-color: #FF4D00;
  box-shadow: 0 0 20px rgba(255, 77, 0, 0.45);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .stack-card { padding: 1.4rem 1.25rem; border-radius: 26px; }
  .card-top-row { flex-direction: column; align-items: flex-start; }
  .card-status-pill { margin-left: 0; }
  .card-slot-frame { padding: 1.15rem 1rem; }
  .projects-footer { flex-direction: column; text-align: center; }
}
"""

# Replace custom sections css in content
start_marker = "/* ============================================================\n   SECTION 2: ABOUT ME SECTION"
end_marker = "</style>"
idx_start = content.find(start_marker)
if idx_start != -1:
    idx_end = content.find(end_marker, idx_start)
    content = content[:idx_start] + new_refined_css + "\n" + content[idx_end:]
    print("Replaced custom sections CSS!")
else:
    print("WARNING: start_marker not found, appending CSS")
    content = content.replace("</style>", new_refined_css + "\n</style>")

# ---------------------------------------------------------------------------
# 4. FIX LAMP PHYSICS & TOGGLE (CLICK / J-CURVE ANIMATION / RELIABLE TOGGLE)
# ---------------------------------------------------------------------------

old_lamp_js_pattern = re.search(r'/\* ---- Light Toggle State ---- \*/.*?(?=/\* ---- Live Local Time Clock ---- \*/)', content, re.DOTALL)
if not old_lamp_js_pattern:
    old_lamp_js_pattern = re.search(r'/\* ---- Light Switch State ---- \*/.*?(?=/\* ---- Live Local Time Clock ---- \*/)', content, re.DOTALL)
if not old_lamp_js_pattern:
    old_lamp_js_pattern = re.search(r'function toggleLight\(\).*?(?=\/\* ---- mobile drawer ---- \*\/)', content, re.DOTALL)

print("Found lamp JS pattern:", bool(old_lamp_js_pattern))

new_lamp_js = """  /* ============================================================
     LAMP TOGGLE & SNAKE PHYSICS WITH J-CURVE CLICK ANIMATION
     Single click or pull on lamp/cord triggers smooth 'J' curl
     and toggles light state ON and OFF reliably!
     ============================================================ */

  var heroPage = document.getElementById('hero-section') || document.querySelector('.page');
  var isLightOn = true;

  function toggleLight() {
    isLightOn = !isLightOn;
    if (heroPage) {
      heroPage.classList.toggle('light-off', !isLightOn);
    }
    document.body.classList.toggle('light-off', !isLightOn);
  }

  var bulbEl = document.getElementById('plBulb');
  var lampWrapper = document.getElementById('lampWrapper');

  /* ---- Multi-joint Snake Rope Simulation ---- */
  var canvas = document.getElementById('snakeCanvas');
  var ctx = canvas.getContext('2d');
  var w = canvas.width = 140;
  var h = canvas.height = 380;

  var numNodes = 14;
  var segLen = 20; // 280px total length
  var rootX = 70;
  var rootY = 10;
  var nodes = [];
  for (var i = 0; i < numNodes; i++) {
    nodes.push({
      x: rootX,
      y: rootY + i * segLen,
      vx: 0,
      vy: 0
    });
  }

  var isDragging = false;
  var hasHover = false;
  var mouseX = rootX;
  var mouseY = rootY;
  var whipEnergy = 0;
  var time = 0;
  var startPointerX = 0;
  var startPointerY = 0;

  // Trigger J-shaped pull curve when clicked
  function triggerJPull() {
    toggleLight();
    // Create an elegant J-shaped pull curve: lower segments displace down and hook horizontally
    for (var k = 1; k < numNodes; k++) {
      var ratio = k / (numNodes - 1);
      // Hook to the left then pull down like the curved tail of letter 'J'
      var jCurveX = -Math.sin(ratio * Math.PI) * 26 * ratio;
      var jPullY = Math.pow(ratio, 1.4) * 44;
      nodes[k].vx += jCurveX;
      nodes[k].vy += jPullY;
    }
    whipEnergy = 16;
  }

  // Pointer helpers
  function getCanvasCoords(e) {
    var rect = canvas.getBoundingClientRect();
    var clientX = e.clientX;
    var clientY = e.clientY;
    if (e.touches && e.touches[0]) {
      clientX = e.touches[0].clientX;
      clientY = e.touches[0].clientY;
    }
    return {
      x: (clientX - rect.left) * (w / rect.width),
      y: (clientY - rect.top) * (h / rect.height),
      rawX: clientX,
      rawY: clientY
    };
  }

  // Canvas interaction listeners
  canvas.addEventListener('pointerenter', function () { hasHover = true; });
  canvas.addEventListener('pointerleave', function () { if (!isDragging) hasHover = false; });

  canvas.addEventListener('pointerdown', function (e) {
    e.preventDefault();
    isDragging = true;
    hasHover = true;
    var c = getCanvasCoords(e);
    mouseX = c.x;
    mouseY = c.y;
    startPointerX = c.rawX;
    startPointerY = c.rawY;
    canvas.setPointerCapture(e.pointerId);
  });

  canvas.addEventListener('pointermove', function (e) {
    if (isDragging || hasHover) {
      var c = getCanvasCoords(e);
      mouseX = c.x;
      mouseY = c.y;
    }
  });

  canvas.addEventListener('pointerup', function (e) {
    if (isDragging) {
      isDragging = false;
      hasHover = false;
      try { canvas.releasePointerCapture(e.pointerId); } catch (err) {}
      
      var c = getCanvasCoords(e);
      var moveDist = Math.hypot(c.rawX - startPointerX, c.rawY - startPointerY);
      
      // If user tapped/clicked or dragged slightly (< 12px) -> trigger clean J-pull toggle!
      if (moveDist < 12) {
        triggerJPull();
      } else {
        // If dragged significantly downwards (> 18px)
        var tip = nodes[numNodes - 1];
        var restTipY = rootY + (numNodes - 1) * segLen;
        if (tip.y - restTipY > 18) {
          toggleLight();
          whipEnergy = 14;
        }
      }
    }
  });

  canvas.addEventListener('pointercancel', function (e) {
    isDragging = false;
    hasHover = false;
  });

  // Bulb element click directly triggers J-pull toggle
  if (bulbEl) {
    bulbEl.addEventListener('click', function (e) {
      e.stopPropagation();
      triggerJPull();
    });
  }

  // Physics animation loop
  function updateSnakePhysics() {
    time += 0.035;
    if (whipEnergy > 0.1) whipEnergy *= 0.90;
    else whipEnergy = 0;

    // Fixed root at fixture
    nodes[0].x = rootX;
    nodes[0].y = rootY;
    nodes[0].vx = 0;
    nodes[0].vy = 0;

    // Apply forces
    for (var i = 1; i < numNodes; i++) {
      var n = nodes[i];

      // Gravity pull downwards
      n.vy += 0.24;

      // Restoring spring pull back to center line
      n.vx += (rootX - n.x) * 0.09;

      // Whip wave pulse ripple down cord if just toggled
      if (whipEnergy > 0) {
        var whipWave = Math.sin(time * 10 - i * 0.7) * whipEnergy * (i / numNodes);
        n.vx += whipWave * 0.08;
      }

      // Gentle snake bending when hovered without dragging
      if (hasHover && !isDragging) {
        var dx = n.x - mouseX;
        var dy = n.y - mouseY;
        var dist = Math.hypot(dx, dy);
        var influenceRadius = 40;
        if (dist < influenceRadius && dist > 0.1) {
          var repulse = (1 - dist / influenceRadius) * 1.6;
          n.vx += (dx / dist) * repulse + Math.sin(time * 3 + i * 0.4) * 0.4;
          n.vy += (dy / dist) * (repulse * 0.12);
        }
      }

      // Handle drag tracking
      if (isDragging) {
        var dragWeight = i / (numNodes - 1);
        if (i === numNodes - 1) {
          n.vx += (mouseX - n.x) * 0.45;
          n.vy += (mouseY - n.y) * 0.45;
        } else if (i > numNodes - 5) {
          n.vx += (mouseX - n.x) * 0.16 * dragWeight;
          n.vy += (mouseY - n.y) * 0.16 * dragWeight;
        }
      }

      // Natural air damping
      n.vx *= 0.88;
      n.vy *= 0.88;

      n.x += n.vx;
      n.y += n.vy;
    }

    // Multi-pass distance constraint solver (keeps snake cord unbroken)
    for (var iter = 0; iter < 4; iter++) {
      for (var j = 0; j < numNodes - 1; j++) {
        var p1 = nodes[j];
        var p2 = nodes[j + 1];
        var cdx = p2.x - p1.x;
        var cdy = p2.y - p1.y;
        var curDist = Math.hypot(cdx, cdy);
        if (curDist > 0.001) {
          var diff = (curDist - segLen) / curDist;
          var offsetX = cdx * 0.5 * diff;
          var offsetY = cdy * 0.5 * diff;
          if (j > 0) {
            p1.x += offsetX * 0.45;
            p1.y += offsetY * 0.45;
          }
          p2.x -= offsetX * 0.95;
          p2.y -= offsetY * 0.95;
        }
      }
    }

    // Render snake rope onto canvas
    ctx.clearRect(0, 0, w, h);

    // 1. Soft drop-shadow
    ctx.beginPath();
    ctx.moveTo(nodes[0].x + 3, nodes[0].y + 4);
    for (var k = 1; k < numNodes - 1; k++) {
      var mx = (nodes[k].x + nodes[k + 1].x) * 0.5 + 3;
      var my = (nodes[k].y + nodes[k + 1].y) * 0.5 + 4;
      ctx.quadraticCurveTo(nodes[k].x + 3, nodes[k].y + 4, mx, my);
    }
    ctx.lineTo(nodes[numNodes - 1].x + 3, nodes[numNodes - 1].y + 4);
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.22)';
    ctx.lineWidth = 6;
    ctx.lineCap = 'round';
    ctx.stroke();

    // 2. Twisted snake rope cord
    ctx.beginPath();
    ctx.moveTo(nodes[0].x, nodes[0].y);
    for (var m = 1; m < numNodes - 1; m++) {
      var cx = (nodes[m].x + nodes[m + 1].x) * 0.5;
      var cy = (nodes[m].y + nodes[m + 1].y) * 0.5;
      ctx.quadraticCurveTo(nodes[m].x, nodes[m].y, cx, cy);
    }
    ctx.lineTo(nodes[numNodes - 1].x, nodes[numNodes - 1].y);
    ctx.strokeStyle = '#cdb287';
    ctx.lineWidth = 4.5;
    ctx.lineCap = 'round';
    ctx.stroke();

    // Inner highlight core
    ctx.strokeStyle = '#f5e4c4';
    ctx.lineWidth = 2;
    ctx.stroke();

    // 3. Wooden ball pull-handle at tip
    var tipNode = nodes[numNodes - 1];
    var prevNode = nodes[numNodes - 2];
    var hAngle = Math.atan2(tipNode.y - prevNode.y, tipNode.x - prevNode.x);

    ctx.save();
    ctx.translate(tipNode.x, tipNode.y);
    ctx.rotate(hAngle - Math.PI / 2);
    ctx.fillStyle = '#6b5329';
    ctx.fillRect(-3, -2, 6, 5);

    // Polished wooden ball
    ctx.beginPath();
    ctx.arc(0, 10, 8.5, 0, Math.PI * 2);
    var ballGrad = ctx.createRadialGradient(-2.5, 7.5, 1, 0, 10, 8.5);
    ballGrad.addColorStop(0, '#f2d8a7');
    ballGrad.addColorStop(0.5, '#b08b51');
    ballGrad.addColorStop(1, '#664e26');
    ctx.fillStyle = ballGrad;
    ctx.fill();
    ctx.strokeStyle = '#e0c391';
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.restore();

    requestAnimationFrame(updateSnakePhysics);
  }

  requestAnimationFrame(updateSnakePhysics);
"""

# Find where snake physics begins in content and replace it
snake_start = content.find("var page = document.getElementById('page');")
if snake_start == -1:
    snake_start = content.find("/* ---- Light Switch State ---- */")
if snake_start == -1:
    snake_start = content.find("/* ============================================================\n     SNAKE ROPE PHYSICS ENGINE")

snake_end = content.find("/* ---- mobile drawer ---- */")
if snake_start != -1 and snake_end != -1:
    content = content[:snake_start] + new_lamp_js + "\n\n  " + content[snake_end:]
    print("Replaced snake physics with reliable click & J-curve animation!")
else:
    print("ERROR: could not locate snake physics region (start:", snake_start, "end:", snake_end, ")")

# ---------------------------------------------------------------------------
# 5. UPDATE NAVIGATION EVENT LISTENERS:
# Click anywhere on about-section redirects to projects-section
# ---------------------------------------------------------------------------

old_nav_js = re.search(r'/\* ---- Navigation Event Handlers ---- \*/.*?(?=\}\)\(\);)', content, re.DOTALL)
new_nav_js = """/* ---- Navigation Event Handlers ---- */
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

  var aboutSec = document.getElementById('about-section');
  if (aboutSec) {
    aboutSec.addEventListener('click', function (e) {
      var projSec = document.getElementById('projects-section');
      if (projSec) {
        projSec.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  var aboutTouchPrompt = document.getElementById('aboutTouchPrompt');
  if (aboutTouchPrompt) {
    aboutTouchPrompt.addEventListener('click', function (e) {
      e.stopPropagation();
      var projSec = document.getElementById('projects-section');
      if (projSec) {
        projSec.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  var backToTopBtn = document.getElementById('backToTopBtn');
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
"""

if old_nav_js:
    content = content[:old_nav_js.start()] + new_nav_js + content[old_nav_js.end():]
    print("Updated navigation event handlers!")
else:
    print("WARNING: old_nav_js not found verbatim, appending before closing script")
    content = content.replace("})();", new_nav_js + "\n})();")

# Write out to both files
with open('app/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated app/index.html successfully!")

with open('marcus-bennet-pull-light.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated marcus-bennet-pull-light.html successfully!")

