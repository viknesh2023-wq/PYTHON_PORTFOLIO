with open('temp_inspect/measure_about.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <script>
    window.addEventListener('load', function() {
      var a = document.getElementById('about-section');
      window.scrollTo({ top: a.offsetTop, behavior: 'instant' });
    });
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

with open('temp_inspect/measure_proj.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <script>
    window.addEventListener('load', function() {
      var p = document.getElementById('projects-section');
      window.scrollTo({ top: p.offsetTop, behavior: 'instant' });
    });
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

import subprocess, os
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
p_about = os.path.abspath('temp_inspect/about_final.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p_about}', '--window-size=1440,900', os.path.abspath('temp_inspect/measure_about.html')])

p_proj = os.path.abspath('temp_inspect/proj_final.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p_proj}', '--window-size=1440,900', os.path.abspath('temp_inspect/measure_proj.html')])

print("Saved about_final.png and proj_final.png")
