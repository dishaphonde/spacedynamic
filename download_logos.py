import urllib.request
import os
import time

os.makedirs('images/clients', exist_ok=True)

# Logo URLs from reliable sources (Wikipedia, brand CDNs, etc.)
logos = {
    # CORPORATE
    'perkinelmer': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/PerkinElmer_logo.svg/320px-PerkinElmer_logo.svg.png',
    'ashland': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Ashland_logo.svg/320px-Ashland_logo.svg.png',
    'icici_prudential': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/ICICI_Prudential_Life_Insurance_Logo.svg/320px-ICICI_Prudential_Life_Insurance_Logo.svg.png',
    'tata_capital': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Tata_Capital_Logo.svg/320px-Tata_Capital_Logo.svg.png',
    'axis_bank': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Axis_Bank_logo.svg/320px-Axis_Bank_logo.svg.png',
    'indusind': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Indusind_Bank_Logo.svg/320px-Indusind_Bank_Logo.svg.png',
    'hdfc_bank': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/HDFC_Bank_Logo.svg/320px-HDFC_Bank_Logo.svg.png',
    'bajaj_finserv': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Bajaj_finserv.svg/320px-Bajaj_finserv.svg.png',
    'goibibo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Goibibo_logo.svg/320px-Goibibo_logo.svg.png',
    'yes_bank': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Yes_Bank_Logo.svg/320px-Yes_Bank_Logo.svg.png',
    'hrblock': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/H%26R_Block_Logo.svg/320px-H%26R_Block_Logo.svg.png',
    # RETAIL
    'lacoste': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Lacoste_logo.svg/320px-Lacoste_logo.svg.png',
    'bose': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Bose_logo.svg/320px-Bose_logo.svg.png',
    'puma': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Puma_logo.svg/320px-Puma_logo.svg.png',
    'mcdonalds': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/McDonald%27s_Golden_Arches.svg/200px-McDonald%27s_Golden_Arches.svg.png',
    'levis': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Levi%27s_logo.svg/320px-Levi%27s_logo.svg.png',
    'adidas': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Adidas_Logo.svg/320px-Adidas_Logo.svg.png',
    'nike': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Logo_NIKE.svg/320px-Logo_NIKE.svg.png',
    'reebok': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Reebok_2019_logo.svg/320px-Reebok_2019_logo.svg.png',
    'patanjali': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Patanjali_Ayurved_Logo.svg/320px-Patanjali_Ayurved_Logo.svg.png',
    'apollo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Apollo_Pharmacy_logo.svg/320px-Apollo_Pharmacy_logo.svg.png',
    'bigbasket': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/BigBasket_Logo.svg/320px-BigBasket_Logo.svg.png',
}

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in logos.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            data = r.read()
        ext = 'png' if 'png' in url.lower() else 'svg'
        fname = f'images/clients/{name}.{ext}'
        with open(fname, 'wb') as f:
            f.write(data)
        print(f'OK: {name}')
        time.sleep(0.3)
    except Exception as e:
        print(f'FAIL: {name} -> {e}')

print('Done!')
