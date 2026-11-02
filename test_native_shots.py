import os, subprocess

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_file = os.path.abspath('app/index.html')

# Screenshot 1: About section via hash
p_about = os.path.abspath('temp_inspect/test_about_native.png')
url_about = 'file:///' + html_file.replace('\\', '/') + '#about-section'
subprocess.run([
    chrome, '--headless', '--disable-gpu',
    f'--screenshot={p_about}',
    '--window-size=1440,900',
    url_about
], capture_output=True)

# Screenshot 2: Projects section via hash
p_proj = os.path.abspath('temp_inspect/test_proj_native.png')
url_proj = 'file:///' + html_file.replace('\\', '/') + '#projects-section'
subprocess.run([
    chrome, '--headless', '--disable-gpu',
    f'--screenshot={p_proj}',
    '--window-size=1440,900',
    url_proj
], capture_output=True)

print("About native exists:", os.path.exists(p_about))
print("Proj native exists:", os.path.exists(p_proj))

