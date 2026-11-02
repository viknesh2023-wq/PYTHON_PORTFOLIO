with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('footer-left')
print(text[p-500:p+100])
