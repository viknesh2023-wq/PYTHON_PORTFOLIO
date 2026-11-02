with open('app/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('Lines in app/index.html:', len(c.splitlines()))
for token in [
    'id="hero-section"',
    'id="about-section"',
    'id="projects-section"',
    'ABOUT ME',
    'PROJECT',
    'Computer Science Engineering student',
    'Stars & Recognitions Collected',
    'Project Audio Recording & Commentary',
    'clickAnywhereBtn',
    'exploreProjectBtn',
    'explorerBtn'
]:
    print(f'{token}: {token in c}')

