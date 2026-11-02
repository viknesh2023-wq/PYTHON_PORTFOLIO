with open('temp_inspect/test_double_click.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <script>
    window.addEventListener('load', function() {
      var d = document.createElement('div');
      d.id = 'toggle-count-log';
      d.style.position = 'fixed';
      d.style.top = '10px';
      d.style.left = '10px';
      d.style.zIndex = '999999';
      d.style.background = 'white';
      d.style.color = 'black';
      d.style.padding = '12px';
      d.style.fontSize = '18px';

      var toggleCallCount = 0;
      var origToggle = toggleLight;
      toggleLight = function() {
        toggleCallCount++;
        origToggle();
      };

      var canvas = document.getElementById('snakeCanvas');

      // Dispatch realistic mouse sequence: mousedown/pointerdown, pointerup, click
      var pDown = new PointerEvent('pointerdown', { clientX: 100, clientY: 100, pointerId: 1 });
      var pUp = new PointerEvent('pointerup', { clientX: 100, clientY: 100, pointerId: 1 });
      var clk = new MouseEvent('click', { clientX: 100, clientY: 100 });

      canvas.dispatchEvent(pDown);
      canvas.dispatchEvent(pUp);
      canvas.dispatchEvent(clk);

      d.innerHTML = 'Toggle call count: ' + toggleCallCount + '<br>' +
                    'Final isLightOn: ' + isLightOn;
      document.body.appendChild(d);
    });
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

import subprocess, os
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
p = os.path.abspath('temp_inspect/double_toggle.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p}', '--window-size=1440,900', os.path.abspath('temp_inspect/test_double_click.html')])
print('Saved double_toggle.png')

