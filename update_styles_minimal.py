import os
import re

css_file = r"c:\Users\phond\Music\spacedynamics\css\style.css"

with open(css_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update :root variables
new_root = """:root {
  --color-bg: #ffffff;
  --color-bg-soft: #f7faf8;
  --color-heading: #111111;
  --color-text: #4a4a4a;
  --color-accent: #2fa860;
  --color-accent-gradient: linear-gradient(90deg, #2fa860, #6fcf87);
  --color-border: #eaeaea;

  /* Remap old variables to new minimal palette */
  --navy: var(--color-heading); /* Previously dark blue/green, now heading color where used for text */
  --navy-deep: var(--color-bg);
  --navy-soft: var(--color-bg-soft);
  --gold: var(--color-accent);
  --gold-light: var(--color-accent);
  --white: var(--color-bg);
  --gray-bg: var(--color-bg-soft);
  --gray-line: var(--color-border);
  --slate: var(--color-text);
  --ink: var(--color-heading);

  --font-display: 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;

  --shadow-soft: 0 4px 16px rgba(0,0,0,0.03);
  --shadow-strong: 0 10px 30px rgba(0,0,0,0.06);

  --container: 1240px;
  --nav-h: 90px;
}"""
content = re.sub(r':root\s*\{[\s\S]*?\n\}', new_root, content, count=1)

# 2. Hero Background Overlay -> White/Light to make black text readable
content = re.sub(r'\.hero-bg::after\{[\s\S]*?\}', 
                 ".hero-bg::after{\n  content:''; position:absolute; inset:0;\n  background: rgba(255,255,255,0.88);\n}", content)

# 3. Hero text colors -> Black
content = re.sub(r'\.hero h1\{\s*color:var\(--white\);', '.hero h1{\n  color:var(--color-heading);', content)
content = re.sub(r'\.hero-sub\{\s*color:rgba\(255,255,255,\.82\);', '.hero-sub{\n  color:var(--color-text);', content)
content = re.sub(r'\.hero-eyebrow\{\s*display:inline-flex; align-items:center; gap:10px; color:var\(--white\);', 
                 '.hero-eyebrow{\n  display:inline-flex; align-items:center; gap:10px; color:var(--color-text);', content)

# 4. Navbar Background -> White
content = re.sub(r'background:rgba\(26,93,58,\.35\);\s*backdrop-filter:blur\(14px\);\s*-webkit-backdrop-filter:blur\(14px\);\s*border-bottom:1px solid rgba\(255,255,255,\.08\);', 
                 'background:rgba(255,255,255,0.9); backdrop-filter:blur(14px); -webkit-backdrop-filter:blur(14px); border-bottom:1px solid var(--color-border);', content)
content = re.sub(r'background:rgba\(26,93,58,\.96\);\s*box-shadow:0 10px 30px rgba\(0,0,0,\.15\);', 
                 'background:rgba(255,255,255,1); box-shadow:var(--shadow-soft);', content)

# Navbar text colors (brand and menu links)
content = re.sub(r'\.brand-mark\{\s*font-family:\'Michroma\', sans-serif; font-weight:400; font-size:18px; color:var\(--white\);',
                 '.brand-mark{ font-family:\'Michroma\', sans-serif; font-weight:400; font-size:18px; color:var(--color-heading);', content)
content = re.sub(r'\.brand-sub\{\s*display:block; font-size:9px; letter-spacing:\.3em; color:rgba\(255,255,255,\.55\);',
                 '.brand-sub{ display:block; font-size:9px; letter-spacing:.3em; color:var(--color-text);', content)
content = re.sub(r'\.nav-menu > li > a\{\s*display:flex; align-items:center; gap:6px; padding:14px 16px; font-size:14\.5px; font-weight:500;\s*color:rgba\(255,255,255,\.88\);',
                 '.nav-menu > li > a{\n  display:flex; align-items:center; gap:6px; padding:14px 16px; font-size:14.5px; font-weight:500;\n  color:var(--color-heading);', content)

content = re.sub(r'\.nav-search-btn,\s*\.nav-toggle\{\s*width:42px; height:42px; border-radius:var\(--radius-sm\); border:1px solid rgba\(255,255,255,\.25\);\s*background:transparent; color:var\(--white\);',
                 '.nav-search-btn, .nav-toggle{\n  width:42px; height:42px; border-radius:var(--radius-sm); border:1px solid var(--color-border);\n  background:transparent; color:var(--color-heading);', content)

content = re.sub(r'\.hero-scroll\{[\s\S]*?color:rgba\(255,255,255,\.6\);',
                 '.hero-scroll{\n  position:absolute; bottom:38px; left:50%; transform:translateX(-50%); z-index:2;\n  display:flex; flex-direction:column; align-items:center; gap:10px; color:var(--color-text);', content)

# 5. Buttons -> pill shaped gradient green
content = re.sub(r'\.btn\{\s*display:inline-flex; align-items:center; justify-content:center; gap:10px;\s*padding:16px 32px; border-radius:var\(--radius-sm\);',
                 '.btn{\n  display:inline-flex; align-items:center; justify-content:center; gap:10px;\n  padding:16px 32px; border-radius:30px;', content)
content = re.sub(r'\.btn-gold\{\s*background:var\(--gold\);\s*color:var\(--navy\);\s*\}',
                 '.btn-gold{ background:var(--color-accent-gradient); color:#ffffff; font-weight:bold; }', content)
content = re.sub(r'\.btn-gold:hover\{\s*background:var\(--gold-light\);\s*transform:translateY\(-3px\);\s*box-shadow:0 14px 30px rgba\(47,158,92,\.35\);\s*\}',
                 '.btn-gold:hover{ transform:translateY(-3px); box-shadow:0 8px 20px rgba(47,168,96,0.3); }', content)
content = re.sub(r'\.btn-outline\{\s*border-color:rgba\(255,255,255,\.5\);\s*color:var\(--white\);\s*\}',
                 '.btn-outline{ border-color:var(--color-border); color:var(--color-heading); }', content)
content = re.sub(r'\.btn-outline:hover\{\s*background:rgba\(255,255,255,\.12\);\s*border-color:var\(--white\);\s*transform:translateY\(-3px\);\s*\}',
                 '.btn-outline:hover{ background:var(--color-bg-soft); border-color:var(--color-accent); color:var(--color-accent); transform:translateY(-3px); }', content)

# 6. Adjust big blocks that had navy background
content = re.sub(r'\.stats-strip\{\s*position:relative; z-index:3; background:var\(--navy-deep\); border-top:1px solid rgba\(255,255,255,\.08\);\s*\}',
                 '.stats-strip{\n  position:relative; z-index:3; background:var(--color-bg); border-top:1px solid var(--color-border); border-bottom:1px solid var(--color-border);\n}', content)
content = re.sub(r'\.stat-item\{\s*padding:34px 20px; text-align:center; border-right:1px solid rgba\(255,255,255,\.08\); position:relative;\s*\}',
                 '.stat-item{\n  padding:34px 20px; text-align:center; border-right:1px solid var(--color-border); position:relative;\n}', content)
content = re.sub(r'\.stat-label\{\s*font-size:12\.5px; color:rgba\(255,255,255,\.68\);',
                 '.stat-label{ font-size:12.5px; color:var(--color-text);', content)

# 7. Founder card & Newsletter & Contact info card & Footer -> white/soft background
content = re.sub(r'\.founder-card\{\s*background:var\(--navy\);\s*border-radius:var\(--radius-lg\);\s*padding:44px; position:relative; overflow:hidden;\s*display:flex; gap:26px; align-items:flex-start;\s*\}',
                 '.founder-card{\n  background:var(--color-bg); border:1px solid var(--color-border); box-shadow:var(--shadow-soft); border-radius:var(--radius-lg); padding:44px; position:relative; overflow:hidden;\n  display:flex; gap:26px; align-items:flex-start;\n}', content)
content = re.sub(r'\.founder-info h3\{\s*color:var\(--white\);', '.founder-info h3{ color:var(--color-heading);', content)
content = re.sub(r'\.founder-info p\{\s*color:rgba\(255,255,255,\.75\);', '.founder-info p{ color:var(--color-text);', content)
content = re.sub(r'\.founder-tags span\{\s*font-size:11\.5px; background:rgba\(255,255,255,\.08\);\s*color:var\(--gold-light\);\s*padding:6px 12px; border-radius:100px;\s*border:1px solid rgba\(47,158,92,\.3\);\s*\}',
                 '.founder-tags span{\n  font-size:11.5px; background:var(--color-bg-soft); color:var(--color-text); padding:6px 12px; border-radius:100px;\n  border:1px solid var(--color-border);\n}', content)
content = re.sub(r'\.newsletter\{\s*background:linear-gradient\(120deg, var\(--navy\), var\(--navy-deep\)\);\s*border-radius:var\(--radius-lg\);',
                 '.newsletter{\n  background:var(--color-bg-soft); border:1px solid var(--color-border); border-radius:var(--radius-lg);', content)
content = re.sub(r'\.newsletter h3\{\s*color:var\(--white\);', '.newsletter h3{ color:var(--color-heading);', content)
content = re.sub(r'\.newsletter p\{\s*color:rgba\(255,255,255,\.7\);', '.newsletter p{ color:var(--color-text);', content)
content = re.sub(r'\.newsletter-form input\{\s*padding:15px 22px; border-radius:100px; border:1px solid rgba\(255,255,255,\.25\); background:rgba\(255,255,255,\.08\);\s*color:var\(--white\);',
                 '.newsletter-form input{\n  padding:15px 22px; border-radius:100px; border:1px solid var(--color-border); background:var(--color-bg);\n  color:var(--color-heading);', content)
content = re.sub(r'\.newsletter-form input::placeholder\{\s*color:rgba\(255,255,255,\.5\);\s*\}',
                 '.newsletter-form input::placeholder{ color:var(--color-text); }', content)

content = re.sub(r'\.contact-info-card\{\s*background:var\(--navy\);\s*border-radius:var\(--radius-lg\);\s*padding:44px; color:var\(--white\);\s*\}',
                 '.contact-info-card{ background:var(--color-bg-soft); border:1px solid var(--color-border); border-radius:var(--radius-lg); padding:44px; color:var(--color-text); }', content)
content = re.sub(r'\.contact-info-card h3\{\s*color:var\(--white\);', '.contact-info-card h3{ color:var(--color-heading);', content)
content = re.sub(r'\.contact-item h5\{\s*font-size:14\.5px; margin-bottom:4px; color:var\(--white\);\s*\}',
                 '.contact-item h5{ font-size:14.5px; margin-bottom:4px; color:var(--color-heading); }', content)
content = re.sub(r'\.contact-item p\{\s*font-size:13\.5px; margin:0; color:rgba\(255,255,255,\.68\);\s*\}',
                 '.contact-item p{ font-size:13.5px; margin:0; color:var(--color-text); }', content)
content = re.sub(r'\.contact-social a\{\s*width:42px; height:42px; border-radius:50%; border:1px solid rgba\(255,255,255,\.25\); display:flex;\s*align-items:center; justify-content:center; color:var\(--white\);',
                 '.contact-social a{\n  width:42px; height:42px; border-radius:50%; border:1px solid var(--color-border); display:flex;\n  align-items:center; justify-content:center; color:var(--color-text);', content)

content = re.sub(r'\.footer\{\s*background:var\(--navy-deep\);\s*color:rgba\(255,255,255,\.7\);\s*padding-top:80px;\s*\}',
                 '.footer{ background:var(--color-bg-soft); color:var(--color-text); border-top:1px solid var(--color-border); padding-top:80px; }', content)
content = re.sub(r'\.footer-grid\{\s*display:grid; grid-template-columns:1\.4fr 1fr 1fr 1\.2fr; gap:40px; padding-bottom:60px; border-bottom:1px solid rgba\(255,255,255,\.08\);\s*\}',
                 '.footer-grid{ display:grid; grid-template-columns:1.4fr 1fr 1fr 1.2fr; gap:40px; padding-bottom:60px; border-bottom:1px solid var(--color-border); }', content)
content = re.sub(r'\.footer-brand p\{\s*color:rgba\(255,255,255,\.55\);', '.footer-brand p{ color:var(--color-text);', content)
content = re.sub(r'\.footer h5\{\s*color:var\(--white\);', '.footer h5{ color:var(--color-heading);', content)
content = re.sub(r'\.footer-links a\{\s*font-size:13\.5px; color:rgba\(255,255,255,\.6\);', '.footer-links a{ font-size:13.5px; color:var(--color-text);', content)
content = re.sub(r'\.footer-social a\{\s*width:38px; height:38px; border-radius:50%; border:1px solid rgba\(255,255,255,\.15\);\s*display:flex;\s*align-items:center; justify-content:center; font-size:13px; transition:\.25s ease;\s*\}',
                 '.footer-social a{\n  width:38px; height:38px; border-radius:50%; border:1px solid var(--color-border); display:flex;\n  align-items:center; justify-content:center; color:var(--color-text); font-size:13px; transition:.25s ease;\n}', content)
content = re.sub(r'\.footer-bottom a\{\s*color:rgba\(255,255,255,\.5\);', '.footer-bottom a{ color:var(--color-text);', content)

# 8. Service / Highlight Card hover states -> white backgrounds, no inverted colors
content = re.sub(r'\.service-card:hover\{\s*background:var\(--navy\);\s*transform:translateY\(-6px\);\s*box-shadow:var\(--shadow-strong\);\s*border-color:var\(--navy\);\s*\}',
                 '.service-card:hover{ background:var(--color-bg); transform:translateY(-6px); box-shadow:var(--shadow-strong); border-color:var(--color-accent); }', content)
content = re.sub(r'\.service-card:hover h3\{\s*color:var\(--white\);\s*\}', '.service-card:hover h3{ color:var(--color-accent); }', content)
content = re.sub(r'\.service-card:hover p\{\s*color:rgba\(255,255,255,\.7\);\s*\}', '.service-card:hover p{ color:var(--color-text); }', content)

content = re.sub(r'\.highlight-card\{\s*background:var\(--navy\);\s*border-radius:var\(--radius-md\);\s*padding:30px; display:flex; gap:20px; align-items:center;\s*\}',
                 '.highlight-card{ background:var(--color-bg); border:1px solid var(--color-border); box-shadow:var(--shadow-soft); border-radius:var(--radius-md); padding:30px; display:flex; gap:20px; align-items:center; }', content)
content = re.sub(r'\.highlight-card h4\{\s*color:var\(--white\);', '.highlight-card h4{ color:var(--color-heading);', content)
content = re.sub(r'\.highlight-card p\{\s*color:rgba\(255,255,255,\.7\);', '.highlight-card p{ color:var(--color-text);', content)

# 9. bg-navy class -> bg-white
content = re.sub(r'\.bg-navy\{\s*background:var\(--navy\);\s*color:var\(--white\);\s*\}',
                 '.bg-navy{ background:var(--color-bg); color:var(--color-text); }', content)
content = re.sub(r'\.bg-navy h2,\s*\.bg-navy h3,\s*\.bg-navy h4\{\s*color:var\(--white\);\s*\}',
                 '.bg-navy h2, .bg-navy h3, .bg-navy h4{ color:var(--color-heading); }', content)

# 10. Floating buttons / Preloader
content = re.sub(r'\.float-btn\{\s*width:56px; height:56px; border-radius:50%; display:flex; align-items:center; justify-content:center;\s*font-size:22px; color:var\(--white\);\s*box-shadow:0 10px 24px rgba\(0,0,0,\.25\);',
                 '.float-btn{\n  width:56px; height:56px; border-radius:50%; display:flex; align-items:center; justify-content:center;\n  font-size:22px; color:#ffffff; box-shadow:var(--shadow-strong);', content)
content = re.sub(r'\#preloader\{\s*position:fixed; inset:0; z-index:99999; background:var\(--navy\);',
                 '#preloader{\n  position:fixed; inset:0; z-index:99999; background:var(--color-bg);', content)
content = re.sub(r'\.preloader-mark\{\s*font-family:\'Michroma\', sans-serif; font-size:15px; letter-spacing:\.1em; color:var\(--white\);',
                 '.preloader-mark{ font-family:\'Michroma\', sans-serif; font-size:15px; letter-spacing:.1em; color:var(--color-heading);', content)
content = re.sub(r'\.preloader-bar\{\s*width:180px; height:2px; background:rgba\(255,255,255,\.15\);',
                 '.preloader-bar{ width:180px; height:2px; background:var(--color-border);', content)

# Spacing updates
content = re.sub(r'\.section-pad\{\s*padding:80px 0;\s*\}', '.section-pad{ padding:110px 0; }', content)

with open(css_file, "w", encoding="utf-8") as f:
    f.write(content)

print("style.css minimalist update complete.")
