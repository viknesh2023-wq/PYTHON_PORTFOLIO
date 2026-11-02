with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('EXPLORER')
print("Position:", p)
print(text[p-400:p+200])

