with open('app/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update toggleLight with 300ms debounce to prevent double-triggering
old_toggle_fn = """  var heroPage = document.getElementById('hero-section') || document.querySelector('.page');
  var isLightOn = true;

  function toggleLight() {
    isLightOn = !isLightOn;
    if (heroPage) {
      heroPage.classList.toggle('light-off', !isLightOn);
    }
    document.body.classList.toggle('light-off', !isLightOn);
  }"""

new_toggle_fn = """  var heroPage = document.getElementById('hero-section') || document.querySelector('.page');
  var isLightOn = true;
  var lastToggleTime = 0;

  function toggleLight() {
    var now = Date.now();
    if (now - lastToggleTime < 320) {
      return; // Debounce: prevent double toggle on pointerup + click sequence
    }
    lastToggleTime = now;
    isLightOn = !isLightOn;
    if (heroPage) {
      heroPage.classList.toggle('light-off', !isLightOn);
    }
    document.body.classList.toggle('light-off', !isLightOn);
  }"""

c = c.replace(old_toggle_fn, new_toggle_fn)

# 2. Update dark background to pure black #000000
c = c.replace('--dark: #17191e;', '--dark: #000000;')

# 3. Add explicit click on lamp-hint ("Pull cord to switch") so clicking it also toggles!
c = c.replace(
    '<div class="lamp-hint">💡 Pull cord to switch</div>',
    '<div class="lamp-hint" id="lampHintBtn" style="cursor:pointer;" title="Click to toggle light">💡 Pull cord to switch</div>'
)

# And bind lampHintBtn in script
hint_bind = """  var lampHintBtn = document.getElementById('lampHintBtn');
  if (lampHintBtn) {
    lampHintBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      triggerJPull();
    });
  }"""

c = c.replace("/* ---- Multi-joint Snake Rope Simulation ---- */", hint_bind + "\n\n  /* ---- Multi-joint Snake Rope Simulation ---- */")

with open('app/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('marcus-bennet-pull-light.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Applied debounced toggle and pure black dark mode!")

