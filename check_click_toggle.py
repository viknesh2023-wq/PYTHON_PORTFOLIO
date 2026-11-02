with open('temp_inspect/test_click_toggle.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <script>
    window.addEventListener('load', function() {
      var d = document.createElement('div');
      d.id = 'toggle-log';
      d.style.position = 'fixed';
      d.style.top = '10px';
      d.style.left = '10px';
      d.style.zIndex = '999999';
      d.style.background = 'white';
      d.style.color = 'black';
      d.style.padding = '12px';
      d.style.fontFamily = 'monospace';

      var pageBefore = document.getElementById('hero-section').className;
      var bodyBefore = document.body.className;

      // Click the bulb
      var bulb = document.getElementById('plBulb');
      bulb.click();

      var pageAfter = document.getElementById('hero-section').className;
      var bodyAfter = document.body.className;

      d.innerHTML = 'page before: ' + pageBefore + '<br>' +
                    'page after click: ' + pageAfter + '<br>' +
                    'body after click: ' + bodyAfter;
      document.body.appendChild(d);
    });
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

import subprocess, os
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
p = os.path.abspath('temp_inspect/click_toggle_test.png')
subprocess.run([chrome, '--headless', '--disable-gpu', f'--screenshot={p}', '--window-size=1440,900', os.path.abspath('temp_inspect/test_click_toggle.html')])
print('Saved click_toggle_test.png')

