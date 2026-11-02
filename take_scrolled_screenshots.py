import subprocess, os, time

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's create a temporary HTML that loads app/index.html and scrolls to #about-section or #projects-section
with open('app/index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Create about preview version
about_preview = orig.replace(
    '<body>',
    '<body><script>window.addEventListener("DOMContentLoaded", function() { window.scrollTo(0, window.innerHeight); });</script>'
)
with open('temp_inspect/about_preview.html', 'w', encoding='utf-8') as f:
    f.write(about_preview)

subprocess.run([
    chrome_path, '--headless', '--disable-gpu',
    '--screenshot=temp_inspect/about_section.png',
    '--window-size=1440,900',
    os.path.abspath('temp_inspect/about_preview.html')
], capture_output=True)

# Create project preview version
project_preview = orig.replace(
    '<body>',
    '<body><script>window.addEventListener("DOMContentLoaded", function() { window.scrollTo(0, window.innerHeight * 2); });</script>'
)
with open('temp_inspect/project_preview.html', 'w', encoding='utf-8') as f:
    f.write(project_preview)

subprocess.run([
    chrome_path, '--headless', '--disable-gpu',
    '--screenshot=temp_inspect/project_section.png',
    '--window-size=1440,900',
    os.path.abspath('temp_inspect/project_preview.html')
], capture_output=True)

print("About section exists:", os.path.exists('temp_inspect/about_section.png'))
print("Project section exists:", os.path.exists('temp_inspect/project_section.png'))

