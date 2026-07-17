with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

def logo_card(name, color='#1a1a2e', text_color='white', bg=None):
    bg_style = f'background:{bg};' if bg else f'background:{color};'
    return f'<div class="logo-card logo-img-card" style="{bg_style}"><span class="logo-text-label" style="color:{text_color};">{name}</span></div>'

corporate_html = '''    <div class="clients-panel active" id="panel-corporate" data-aos="fade-up">
      <div class="logo-grid">
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><img src="https://www.perkinelmer.com/favicon.ico" alt="" style="display:none"><span class="logo-text-label" style="color:#003087;font-weight:800;font-size:15px;">PerkinElmer</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#dc3545;font-weight:700;">Ashland</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#0066b3;font-weight:700;">GainInsights</span></div>
        <div class="logo-card logo-img-card" style="background:#003087;"><span class="logo-text-label" style="color:#f7a800;font-weight:800;">ICICI Prudential</span></div>
        <div class="logo-card logo-img-card" style="background:#003087;"><span class="logo-text-label" style="color:#fff;font-weight:700;">TATA Capital</span></div>
        <div class="logo-card logo-img-card" style="background:#800000;"><span class="logo-text-label" style="color:#fff;font-weight:800;">AXIS BANK</span></div>
        <div class="logo-card logo-img-card" style="background:#7b2d8b;"><span class="logo-text-label" style="color:#fff;font-weight:700;">IndusInd Bank</span></div>
        <div class="logo-card logo-img-card" style="background:#006b8f;"><span class="logo-text-label" style="color:#fff;font-weight:900;font-size:22px;letter-spacing:2px;">SCOR</span></div>
        <div class="logo-card logo-img-card" style="background:#003a70;"><span class="logo-text-label" style="color:#fff;font-weight:700;">sace<sup style="font-size:9px;color:#e63946;">■</sup></span></div>
        <div class="logo-card logo-img-card" style="background:#e63946;"><span class="logo-text-label" style="color:#fff;font-weight:700;">aventri</span></div>
        <div class="logo-card logo-img-card" style="background:#004c8f;"><span class="logo-text-label" style="color:#fff;font-weight:800;">HDFC BANK</span></div>
        <div class="logo-card logo-img-card" style="background:#003399;"><span class="logo-text-label" style="color:#fff;font-weight:700;">BAJAJ Finserv</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#006837;font-weight:800;">FOTON</span></div>
        <div class="logo-card logo-img-card" style="background:#e63946;"><span class="logo-text-label" style="color:#fff;font-weight:900;font-size:17px;">goibibo<span style="font-size:11px;">.com</span></span></div>
        <div class="logo-card logo-img-card" style="background:#003087;"><span class="logo-text-label" style="color:#fff;font-weight:800;font-size:14px;">YES <span style="color:#e63946;">✓</span> BANK</span></div>
        <div class="logo-card logo-img-card" style="background:#006b3c;"><span class="logo-text-label" style="color:#fff;font-weight:900;">H&amp;R Block</span></div>
      </div>
    </div>'''

retail_html = '''    <div class="clients-panel" id="panel-retail" data-aos="fade-up">
      <div class="logo-grid">
        <div class="logo-card logo-img-card" style="background:#f4a130;"><span class="logo-text-label" style="color:#fff;font-weight:700;font-style:italic;">aurelia</span></div>
        <div class="logo-card logo-img-card" style="background:#111;"><span class="logo-text-label" style="color:#fff;font-weight:800;letter-spacing:1px;">BLACKBERRYS</span></div>
        <div class="logo-card logo-img-card" style="background:#c8102e;"><span class="logo-text-label" style="color:#fff;font-weight:700;font-size:11px;">ADITYA BIRLA<br>FASHION &amp; RETAIL</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#000;font-weight:900;letter-spacing:2px;">BOSE</span></div>
        <div class="logo-card logo-img-card" style="background:#2b2b2b;"><span class="logo-text-label" style="color:#c0a060;font-weight:700;letter-spacing:1px;">D'DECOR</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#006633;font-weight:900;font-size:20px;letter-spacing:2px;">LACOSTE</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#000;font-weight:700;">HELIOS<br><small style="font-size:9px;">THE WATCH STORE by TITAN</small></span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#0066b3;font-weight:800;">vision e<span style="color:#e63946;">x</span>press</span></div>
        <div class="logo-card logo-img-card" style="background:#000;"><span class="logo-text-label" style="color:#f7a800;font-weight:900;">GOLD'S GYM</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#e8b800;font-weight:900;">M<span style="color:#333;"> MultiFit</span></span></div>
        <div class="logo-card logo-img-card" style="background:#c8102e;"><span class="logo-text-label" style="color:#fff;font-weight:900;">LAKMÉ SALON</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#006b8f;font-weight:700;">Apollo Pharmacy</span></div>
        <div class="logo-card logo-img-card" style="background:#c8102e;"><span class="logo-text-label" style="color:#fff;font-weight:900;letter-spacing:2px;">PUMA</span></div>
        <div class="logo-card logo-img-card" style="background:#84c225;"><span class="logo-text-label" style="color:#fff;font-weight:900;">bb bigbasket</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#003087;font-weight:700;">Van Heusen<br><small style="font-size:9px;">POWER DRESSING</small></span></div>
        <div class="logo-card logo-img-card" style="background:#2b2b2b;"><span class="logo-text-label" style="color:#c0a060;font-weight:700;">Kawediya<br><small>Jewellers</small></span></div>
        <div class="logo-card logo-img-card" style="background:#c8102e;"><span class="logo-text-label" style="color:#fff;font-weight:900;letter-spacing:1px;">PLANET FASHION</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#5c3d11;font-weight:700;">☕ tea post</span></div>
        <div class="logo-card logo-img-card" style="background:#2b2b2b;"><span class="logo-text-label" style="color:#c0a060;font-weight:700;letter-spacing:2px;">SMOOR</span></div>
        <div class="logo-card logo-img-card" style="background:#c8102e;"><span class="logo-text-label" style="color:#f7a800;font-weight:900;font-size:18px;">McDonald's</span></div>
        <div class="logo-card logo-img-card" style="background:#111;"><span class="logo-text-label" style="color:#fff;font-weight:700;font-size:12px;">THE BAR STOCK<br>EXCHANGE</span></div>
        <div class="logo-card logo-img-card" style="background:#006b8f;"><span class="logo-text-label" style="color:#fff;font-weight:700;">🏥 NRS Hospital</span></div>
        <div class="logo-card logo-img-card" style="background:#c8102e;"><span class="logo-text-label" style="color:#fff;font-weight:900;letter-spacing:2px;">LEVI'S</span></div>
        <div class="logo-card logo-img-card" style="background:#000;"><span class="logo-text-label" style="color:#fff;font-weight:900;letter-spacing:3px;font-size:20px;">adidas</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#000;font-weight:900;font-size:28px;letter-spacing:-1px;">✓</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#c8102e;font-weight:900;font-size:18px;letter-spacing:1px;">Reebok</span></div>
        <div class="logo-card logo-img-card" style="background:#0077c8;"><span class="logo-text-label" style="color:#fff;font-weight:800;font-size:12px;">GANGAR<br>EYENATION</span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#e63946;font-weight:900;font-size:14px;">PATANJALI</span></div>
        <div class="logo-card logo-img-card" style="background:#c45c00;"><span class="logo-text-label" style="color:#fff;font-weight:700;font-size:12px;">m.o.d<br><small>mad over donuts</small></span></div>
        <div class="logo-card logo-img-card" style="background:#fff;border:1px solid #eee;"><span class="logo-text-label" style="color:#000;font-weight:900;font-size:11px;letter-spacing:1px;">JUST IN TIME</span></div>
        <div class="logo-card logo-img-card" style="background:#e63946;"><span class="logo-text-label" style="color:#fff;font-weight:900;font-size:15px;">WOW! momo</span></div>
        <div class="logo-card logo-img-card" style="background:#e63946;"><span class="logo-text-label" style="color:#f7a800;font-weight:900;font-size:15px;">WOW! China</span></div>
      </div>
    </div>'''

import re

c = re.sub(
    r'<div class="clients-panel active" id="panel-corporate".*?</div>\s*</div>\s*</div>',
    corporate_html,
    c, flags=re.DOTALL, count=1
)

c = re.sub(
    r'<div class="clients-panel" id="panel-retail".*?</div>\s*</div>',
    retail_html,
    c, flags=re.DOTALL, count=1
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done! Logo-styled cards written.')
