# Let's inspect the HTML and CSS of hero and about section
with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see what CSS rules apply to .page, #about-section, etc.
import re
print("Found #about-section in HTML:", '#about-section' in text)
print("Found #projects-section in HTML:", '#projects-section' in text)

