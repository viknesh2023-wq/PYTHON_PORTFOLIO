with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'[^{}]*cursor[^{}]*:[^;]+;', text)
print(f"Total cursor rules: {len(matches)}")
for m in matches[:15]:
    print(" -", m.strip())

