with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.findall(r'(--dark:[^;]+;)', text)
print("Definition of --dark:", m)

m2 = re.findall(r'(--red-orange:[^;]+;)', text)
print("Definition of --red-orange:", m2)

