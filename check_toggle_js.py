# Test click toggle
import os, subprocess

with open('app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the toggle light script
print("heroPage query:", "var heroPage = document.getElementById('hero-section')" in text)
print("triggerJPull defined:", "function triggerJPull()" in text)
print("canvas click listener:", "canvas.addEventListener('pointerup'" in text)
print("bulb click listener:", "bulbEl.addEventListener('click'" in text)

