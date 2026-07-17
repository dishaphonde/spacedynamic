with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<span class="brand-mark">SPACEDYNAMICS&trade;</span>', '<img src="images/logo.png" alt="Space Dynamics Logo" class="brand-logo">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('\n.brand-logo { max-height: 40px; width: auto; display: block; }\n')

print('HTML and CSS updated for image logo.')
