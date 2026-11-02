with open('temp_inspect/test_eval_simple.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <script>
    try {
      console.log('Script loaded successfully');
      var b = document.getElementById('plBulb');
      b.click();
    } catch(e) {
      console.error('ERROR IN SCRIPT:', e);
    }
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

import subprocess, os
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('temp_inspect/test_eval_simple.html')
res = subprocess.run([chrome, '--headless', '--disable-gpu', '--dump-dom', html], capture_output=True, text=True)
print("Hero class in dumped DOM:")
for line in res.stdout.splitlines():
    if 'id="hero-section"' in line or 'class="page' in line:
        print(line)

