with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

p_html = text.find('class="lamp-wrapper"')
print("=== LAMP HTML ===")
print(text[p_html-50:p_html+500].encode('ascii', 'replace').decode('ascii'))

p_css = text.find('.lamp-wrapper {')
print("\n=== LAMP CSS ===")
print(text[p_css-50:p_css+800].encode('ascii', 'replace').decode('ascii'))
