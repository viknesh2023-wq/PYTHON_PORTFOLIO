with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('.page {')
print(text[p:p+400])

