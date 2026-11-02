import subprocess, os

with open('temp_inspect/test_eval_cycle.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <div id="testLog" style="position:fixed;top:0;left:0;z-index:999999;color:yellow;background:black;padding:10px;"></div>
    <script>
    window.addEventListener('load', function() {
      var log = document.getElementById('testLog');
      var cvs = document.getElementById('snakeCanvas');
      var page = document.getElementById('hero-section');
      
      // Click 1:
      cvs.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true, cancelable: true, clientX: 200, clientY: 200, pointerId: 1 }));
      cvs.dispatchEvent(new PointerEvent('pointerup', { bubbles: true, cancelable: true, clientX: 200, clientY: 200, pointerId: 1 }));
      cvs.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 200, clientY: 200 }));
      
      var state1 = page.classList.contains('light-off');
      
      // Click 2 after 400ms:
      setTimeout(function() {
        cvs.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true, cancelable: true, clientX: 200, clientY: 200, pointerId: 1 }));
        cvs.dispatchEvent(new PointerEvent('pointerup', { bubbles: true, cancelable: true, clientX: 200, clientY: 200, pointerId: 1 }));
        cvs.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 200, clientY: 200 }));
        var state2 = page.classList.contains('light-off');
        log.innerText = 'STATE1:' + state1 + ' | STATE2:' + state2;
      }, 400);
    });
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('temp_inspect/test_eval_cycle.html')
res = subprocess.run([chrome, '--headless', '--disable-gpu', '--virtual-time-budget=1000', '--dump-dom', html], capture_output=True, text=True)
for line in res.stdout.splitlines():
    if 'testLog' in line:
        print(line)

