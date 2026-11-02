with open('app/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's test by making the about section the first section, or scrolling directly
c_about_top = c.replace(
    '<section class="page" id="hero-section">',
    '<section class="page" id="hero-section" style="display:none;">'
)

with open('temp_inspect/about_direct.html', 'w', encoding='utf-8') as f:
    f.write(c_about_top)

import subprocess, os
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
p = os.path.abspath('temp_inspect/about_direct.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p}', '--window-size=1440,900', os.path.abspath('temp_inspect/about_direct.html')])
print('Saved about_direct.png')

c_proj_top = c.replace(
    '<section class="page" id="hero-section">',
    '<section class="page" id="hero-section" style="display:none;">'
).replace(
    '<section id="about-section"',
    '<section id="about-section" style="display:none;"'
)

with open('temp_inspect/proj_direct.html', 'w', encoding='utf-8') as f:
    f.write(c_proj_top)

p2 = os.path.abspath('temp_inspect/proj_direct.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p2}', '--window-size=1440,900', os.path.abspath('temp_inspect/proj_direct.html')])
print('Saved proj_direct.png')

