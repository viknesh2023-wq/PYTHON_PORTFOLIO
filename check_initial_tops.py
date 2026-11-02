import subprocess
import json
import re

eval_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var cards = Array.from(document.querySelectorAll('.stack-card'));

    // Cache initial absolute top of each card when scrollY = 0
    window.scrollTo(0, 0);
    var initialTops = cards.map(function(c) {
      var r = c.getBoundingClientRect();
      var stickyTop = parseFloat(window.getComputedStyle(c).top) || 65;
      return {
        id: c.id,
        top: Math.round(r.top + window.scrollY),
        stickyTop: stickyTop,
        triggerY: Math.round(r.top + window.scrollY - stickyTop)
      };
    });

    var res = {
      initialTops: initialTops,
      docHeight: document.documentElement.scrollHeight,
      winHeight: window.innerHeight
    };

    var div = document.createElement('div');
    div.id = 'INITIAL_TOPS_OUT';
    div.textContent = JSON.stringify(res);
    document.body.appendChild(div);
  }, 400);
});
</script>
"""

with open('app/index.html', 'r', encoding='utf-8') as f:
    h = f.read()

with open('test_initial_tops.html', 'w', encoding='utf-8') as f:
    f.write(h.replace('</body>', eval_script + '\n</body>'))

cmd = [
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,900',
    '--virtual-time-budget=2000',
    '--dump-dom',
    'file:///d:/python_portfolio/test_initial_tops.html'
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
m = re.search(r'<div id="INITIAL_TOPS_OUT">(.+?)</div>', res.stdout)
if m:
    data = json.loads(m.group(1))
    print(f"Doc Height: {data['docHeight']}px | Win Height: {data['winHeight']}px\n")
    print(f"{'SLIDE':<10} | {'TOP':<8} | {'STICKY_TOP':<10} | {'TRIGGER_Y'}")
    print("-" * 45)
    for t in data['initialTops']:
        print(f"{t['id']:<10} | {t['top']:<8} | {t['stickyTop']:<10} | {t['triggerY']}px")

