import os, subprocess

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_file = os.path.abspath('app/index.html')

with open('app/index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# 1. About section screenshot (pure white, top-left, plain)
about_only = orig.replace(
    '<section class="page" id="hero-section">',
    '<section class="page" id="hero-section" style="display:none;">'
)
with open('temp_inspect/vis_about.html', 'w', encoding='utf-8') as f:
    f.write(about_only)

p_about = os.path.abspath('temp_inspect/vis_about.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p_about}', '--window-size=1440,900', os.path.abspath('temp_inspect/vis_about.html')])

# 2. Project section screenshot (reduced sizes, pure white titles, no 15 milestone)
proj_only = orig.replace(
    '<section class="page" id="hero-section">',
    '<section class="page" id="hero-section" style="display:none;">'
).replace(
    '<section id="about-section"',
    '<section id="about-section" style="display:none;"'
)
with open('temp_inspect/vis_proj.html', 'w', encoding='utf-8') as f:
    f.write(proj_only)

p_proj = os.path.abspath('temp_inspect/vis_proj.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p_proj}', '--window-size=1440,900', os.path.abspath('temp_inspect/vis_proj.html')])

# 3. Light OFF hero screenshot (dark mode toggled)
dark_hero = orig.replace(
    '<section class="page" id="hero-section">',
    '<section class="page light-off" id="hero-section">'
)
with open('temp_inspect/vis_dark_hero.html', 'w', encoding='utf-8') as f:
    f.write(dark_hero)

p_dark = os.path.abspath('temp_inspect/vis_dark_hero.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p_dark}', '--window-size=1440,900', os.path.abspath('temp_inspect/vis_dark_hero.html')])

print("About preview exists:", os.path.exists(p_about))
print("Project preview exists:", os.path.exists(p_proj))
print("Dark hero preview exists:", os.path.exists(p_dark))

