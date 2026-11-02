with open('app/index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# For headless test only: disable smooth scroll so it jumps immediately
test_instant = orig.replace(
    'scroll-behavior: smooth;',
    'scroll-behavior: auto !important;'
)

import subprocess, os
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Test 1: About section
with open('temp_inspect/test_about_jump.html', 'w', encoding='utf-8') as f:
    f.write(test_instant.replace(
        '</body>',
        '<script>window.onload = function() { location.hash = "about-section"; };</script></body>'
    ))

p_about = os.path.abspath('temp_inspect/about_jump.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p_about}', '--window-size=1440,900', os.path.abspath('temp_inspect/test_about_jump.html')])

# Test 2: Project section
with open('temp_inspect/test_proj_jump.html', 'w', encoding='utf-8') as f:
    f.write(test_instant.replace(
        '</body>',
        '<script>window.onload = function() { location.hash = "projects-section"; };</script></body>'
    ))

p_proj = os.path.abspath('temp_inspect/proj_jump.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p_proj}', '--window-size=1440,900', os.path.abspath('temp_inspect/test_proj_jump.html')])

print("About jump exists:", os.path.exists(p_about))
print("Proj jump exists:", os.path.exists(p_proj))

