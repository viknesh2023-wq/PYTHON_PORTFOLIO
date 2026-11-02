with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.findall(r'(\.page[^{]*\{[^}]*\})', text)
for r in m[:10]:
    print(r)
    print('-'*40)

m2 = re.findall(r'(\.bg-wrap[^{]*\{[^}]*\})', text)
for r in m2[:10]:
    print(r)
    print('-'*40)

