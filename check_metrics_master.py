import subprocess
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read app/index.html
with open('app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a measurement script before </body>
eval_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var cards = Array.from(document.querySelectorAll('.stack-card'));
    var cardData = cards.map(function(c, idx) {
      var rect = c.getBoundingClientRect();
      var style = window.getComputedStyle(c);
      return {
        idx: idx + 1,
        id: c.id,
        height: Math.round(rect.height),
        scrollHeight: c.scrollHeight,
        clientHeight: c.clientHeight,
        hasScrollbar: c.scrollHeight > c.clientHeight + 4,
        offsetTop: Math.round(c.offsetTop)
      };
    });

    var travelData = [];
    for (var i = 0; i < cards.length - 1; i++) {
      var d = Math.round(cards[i + 1].offsetTop - cards[i].offsetTop);
      travelData.push({ from: i + 1, to: i + 2, dist: d });
    }

    var res = { cards: cardData, travels: travelData };
    var div = document.createElement('div');
    div.id = 'TEST_RESULTS_OUTPUT';
    div.textContent = JSON.stringify(res);
    document.body.appendChild(div);
  }, 300);
});
</script>
"""

with open('test_measure_master.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', eval_script + '\n</body>'))

# Run Chrome headless to dump DOM with virtual time
cmd = [
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--window-size=1400,900',
    '--virtual-time-budget=2000',
    '--dump-dom',
    'file:///d:/python_portfolio/test_measure_master.html'
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
match = re.search(r'<div id="TEST_RESULTS_OUTPUT">(.+?)</div>', res.stdout)
if match:
    data = json.loads(match.group(1))
    print("=== CARD DIMENSIONS & SCROLLBAR CHECK (MASTER) ===")
    all_clean = True
    for c in data['cards']:
        status = "❌ HAS SCROLLBAR (TRAP!)" if c['hasScrollbar'] else "✅ CLEAN (No Trap)"
        if c['hasScrollbar']:
            all_clean = False
        print(f"Slide {c['idx']:02d} ({c['id']}): H={c['height']}px (client: {c['clientHeight']}px, scroll: {c['scrollHeight']}px) -> {status}")
    
    print("\n=== TRAVEL DISTANCES BETWEEN CONSECUTIVE CARDS ===")
    dists = [t['dist'] for t in data['travels']]
    for t in data['travels']:
        print(f"Slide {t['from']:02d} -> Slide {t['to']:02d}: travel = {t['dist']}px")
    
    avg_d = sum(dists) / len(dists)
    min_d = min(dists)
    max_d = max(dists)
    print(f"\nAverage Travel: {avg_d:.1f}px | Min: {min_d}px | Max: {max_d}px | Spread: {max_d - min_d}px")
    print(f"All cards free of mousewheel traps: {all_clean}")
else:
    print("Could not find TEST_RESULTS_OUTPUT")

