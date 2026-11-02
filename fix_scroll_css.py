with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace html and body CSS with standard native scrolling
old_css = """html {
  height: 100%;
  scroll-behavior: smooth;
  background: #000000;
}

body {
  font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #000000;
  overflow-x: hidden;
  overflow-y: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  scroll-behavior: smooth;
}"""

new_css = """html {
  scroll-behavior: smooth;
  background: #000000;
  color: #ffffff;
}

body {
  font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #000000;
  color: #ffffff;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}"""

text = text.replace(old_css, new_css)

# Also fix the duplicate id on hero-section
text = text.replace('id="hero-section" id="page"', 'id="hero-section"')

with open('app/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('marcus-bennet-pull-light.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated html/body CSS for native window scrolling!")

