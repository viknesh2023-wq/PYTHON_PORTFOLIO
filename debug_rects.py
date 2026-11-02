import os, subprocess

script = """
const puppeteer = require('puppeteer'); // if available or let's use node
"""
with open('temp_inspect/test_rects.html', 'w', encoding='utf-8') as f:
    with open('app/index.html', 'r', encoding='utf-8') as src:
        c = src.read()
    # Inject logger to console
    inject = """
    <script>
    window.addEventListener('load', () => {
      const hero = document.getElementById('hero-section');
      const about = document.getElementById('about-section');
      const proj = document.getElementById('projects-section');
      console.log('HERO rect:', JSON.stringify(hero.getBoundingClientRect()));
      console.log('ABOUT rect:', JSON.stringify(about.getBoundingClientRect()));
      console.log('PROJ rect:', JSON.stringify(proj.getBoundingClientRect()));
    });
    </script>
    """
    f.write(c.replace('</body>', inject + '</body>'))

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
res = subprocess.run([
    chrome, '--headless', '--disable-gpu',
    '--enable-logging=stderr', '--v=1',
    os.path.abspath('temp_inspect/test_rects.html')
], capture_output=True, text=True)

for line in res.stderr.splitlines():
    if 'rect:' in line:
        print(line)

