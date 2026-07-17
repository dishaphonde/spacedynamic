import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<span class="brand-mark">SPACE<span>DYNAMICS</span></span>', '<span class="brand-mark">SPACEDYNAMICS&trade;</span>')
c = c.replace('<div class="preloader-mark">SPACE DYNAMICS</div>', '<div class="preloader-mark">SPACEDYNAMICS&trade;</div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.brand-mark{ font-family:var(--font-display); font-weight:700; font-size:22px; color:var(--white); letter-spacing:.02em; }', '@import url(\'https://fonts.googleapis.com/css2?family=Michroma&display=swap\');\n.brand-mark{ font-family:\'Michroma\', sans-serif; font-weight:400; font-size:18px; color:var(--white); letter-spacing:0.08em; }')
css = css.replace('.brand-mark span{ color:var(--gold); }', '')
css = css.replace('.preloader-mark{ font-family:var(--font-display); font-size:15px; letter-spacing:.35em; color:var(--gold); text-transform:uppercase; }', '.preloader-mark{ font-family:\'Michroma\', sans-serif; font-size:15px; letter-spacing:.1em; color:var(--white); text-transform:uppercase; }')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Logo text and styling updated')
