with open('temp_inspect/test_hit.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <script>
    window.addEventListener('load', function() {
      var lamp = document.getElementById('lampWrapper');
      var canvas = document.getElementById('snakeCanvas');
      var bulb = document.getElementById('plBulb');
      var rectLamp = lamp.getBoundingClientRect();
      var rectCanvas = canvas.getBoundingClientRect();
      var rectBulb = bulb.getBoundingClientRect();

      // Check what element is hit at the bulb center
      var hitAtBulb = document.elementFromPoint(rectBulb.left + 10, rectBulb.top + 10);
      // Check what element is hit at canvas center (middle of cord)
      var hitAtCord = document.elementFromPoint(rectCanvas.left + 70, rectCanvas.top + 150);
      // Check what element is hit at tip of cord
      var hitAtTip = document.elementFromPoint(rectCanvas.left + 70, rectCanvas.top + 280);

      var d = document.createElement('div');
      d.id = 'hit-results';
      d.style.position = 'fixed';
      d.style.top = '10px';
      d.style.left = '10px';
      d.style.zIndex = '999999';
      d.style.background = 'white';
      d.style.color = 'black';
      d.style.padding = '12px';
      d.style.fontFamily = 'monospace';
      d.innerHTML = 'Bulb hit: ' + (hitAtBulb ? hitAtBulb.tagName + '.' + hitAtBulb.className : 'null') + '<br>' +
                    'Cord hit: ' + (hitAtCord ? hitAtCord.tagName + '.' + hitAtCord.className : 'null') + '<br>' +
                    'Tip hit: ' + (hitAtTip ? hitAtTip.tagName + '.' + hitAtTip.className : 'null') + '<br>' +
                    'Lamp rect: ' + rectLamp.left + ',' + rectLamp.top + ',' + rectLamp.width + ',' + rectLamp.height;
      document.body.appendChild(d);
    });
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

import subprocess, os
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
p = os.path.abspath('temp_inspect/hit_test.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p}', '--window-size=1440,900', os.path.abspath('temp_inspect/test_hit.html')])
print('Saved hit_test.png')

