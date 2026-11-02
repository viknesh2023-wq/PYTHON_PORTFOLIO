with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all children of .page
p_start = text.find('<section class="page"')
p_end = text.find('</section>')
print("Hero length:", p_end - p_start)
hero_str = text[p_start:p_end+10]

import re
tags = re.findall(r'<([a-zA-Z0-9\-]+)[^>]*class="([^"]*)"', hero_str)
for t, c in tags:
    print(f"<{t} class='{c}'>")

