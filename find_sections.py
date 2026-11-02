with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<section', text)]
print("Matches for <section:", matches)
for m in matches:
    print(text[m:m+80])

matches_close = [m.start() for m in re.finditer(r'</section>', text)]
print("Matches for </section>:", matches_close)
for m in matches_close:
    print(text[m-80:m+20])

