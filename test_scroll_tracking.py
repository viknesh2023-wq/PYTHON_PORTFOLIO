import subprocess
import json
import re

eval_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var cards = Array.from(document.querySelectorAll('.stack-card'));

    // Check what getBoundingClientRect() returns at scrollY = 0, scrollY = 5000, scrollY = 12000
    // And what happens when scrolling back from 12000 to 11000, 10000, 9000, etc.

    function evaluateAt(scrollY) {
      window.scrollTo(0, scrollY);
      var curY = window.pageYOffset;

      // Current logic in app/index.html
      var activeId = cards[0].id;
      var debug = [];
      for (var i = 0; i < cards.length; i++) {
        var card = cards[i];
        var rect = card.getBoundingClientRect();
        var docTop = rect.top + curY;
        var stickyTop = parseFloat(window.getComputedStyle(card).top) || 65;
        var targetArrival = docTop - stickyTop - 30;

        debug.push({
          id: card.id,
          rectTop: Math.round(rect.top),
          docTop: Math.round(docTop),
          targetArrival: Math.round(targetArrival),
          cond: curY >= targetArrival
        });

        if (curY >= targetArrival) {
          activeId = card.id;
        } else {
          break;
        }
      }
      return { scrollY: curY, activeId: activeId, debug: debug };
    }

    // Scroll down to bottom first
    window.scrollTo(0, 12000);
    setTimeout(function() {
      var r12000 = evaluateAt(12000);
      var r11000 = evaluateAt(11000); // Scrolling UP
      var r10000 = evaluateAt(10000); // Scrolling UP
      var r8000 = evaluateAt(8000);   // Scrolling UP
      var r5000 = evaluateAt(5000);   // Scrolling UP

      var res = {
        at_12000: r12000.activeId,
        at_11000: r11000.activeId,
        at_10000: r10000.activeId,
        at_8000: r8000.activeId,
        at_5000: r5000.activeId,
        debug_11000: r11000.debug
      };

      var div = document.createElement('div');
      div.id = 'TEST_TRACKING_OUT';
      div.textContent = JSON.stringify(res);
      document.body.appendChild(div);
    }, 400);
  }, 400);
});
</script>
"""

with open('app/index.html', 'r', encoding='utf-8') as f:
    h = f.read()

with open('test_scroll_debug.html', 'w', encoding='utf-8') as f:
    f.write(h.replace('</body>', eval_script + '\n</body>'))

cmd = [
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,900',
    '--virtual-time-budget=3000',
    '--dump-dom',
    'file:///d:/python_portfolio/test_scroll_debug.html'
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
m = re.search(r'<div id="TEST_TRACKING_OUT">(.+?)</div>', res.stdout)
if m:
    data = json.loads(m.group(1))
    print("=== SCROLL TRACKING RESULTS (DECREASING ORDER) ===")
    print("At 12000px:", data['at_12000'])
    print("At 11000px (scrolled back 1000px):", data['at_11000'])
    print("At 10000px (scrolled back 2000px):", data['at_10000'])
    print("At 8000px (scrolled back 4000px):", data['at_8000'])
    print("At 5000px (scrolled back 7000px):", data['at_5000'])
    print("\nDebug at 11000px:")
    for d in data['debug_11000'][:5]: print(d)
else:
    print("Failed to get TEST_TRACKING_OUT")

