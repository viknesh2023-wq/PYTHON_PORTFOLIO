# Check console
with open('temp_inspect/test_double_click.html', 'w', encoding='utf-8') as out:
    with open('app/index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    test_code = """
    <script>
    window.addEventListener('DOMContentLoaded', function() {
      console.log('Testing click events:');
      var canvas = document.getElementById('snakeCanvas');
      var bulb = document.getElementById('plBulb');
      console.log('canvas:', !!canvas, 'bulb:', !!bulb);
    });
    </script>
    """
    out.write(c.replace('</body>', test_code + '</body>'))

with open('temp_inspect/eval_click.py', 'w', encoding='utf-8') as out:
    out.write('''
import subprocess, os
chrome = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
html = os.path.abspath('temp_inspect/test_double_click.html')
res = subprocess.run([chrome, '--headless', '--disable-gpu', '--dump-dom', html], capture_output=True, text=True)
for line in res.stdout.splitlines():
    if 'Toggle call count' in line or 'toggle-count-log' in line or 'isLightOn' in line:
        print(line)
''')

