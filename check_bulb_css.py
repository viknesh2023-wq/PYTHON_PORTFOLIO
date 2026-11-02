with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('.light-off .pl-bulb')
print(text[p-50:p+300])

