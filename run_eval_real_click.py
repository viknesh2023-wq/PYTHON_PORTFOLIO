with open('temp_inspect/test_eval_real_click.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <script>
    window.addEventListener('load', function() {
      var cvs = document.getElementById('snakeCanvas');
      var pDown = new PointerEvent('pointerdown', { bubbles: true, cancelable: true, clientX: 200, clientY: 200, pointerId: 1 });
      var pUp = new PointerEvent('pointerup', { bubbles: true, cancelable: true, clientX: 200, clientY: 200, pointerId: 1 });
      var clk = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 200, clientY: 200 });

      cvs.dispatchEvent(pDown);
      cvs.dispatchEvent(pUp);
      cvs.dispatchEvent(clk);
    });
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

import subprocess, os
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('temp_inspect/test_eval_real_click.html')
res = subprocess.run([chrome, '--headless', '--disable-gpu', '--dump-dom', html], capture_output=True, text=True)
print("Hero class in dumped DOM after realistic mouse click sequence:")
for line in res.stdout.splitlines():
    if 'id="hero-section"' in line or 'class="page' in line:
        print(line)

