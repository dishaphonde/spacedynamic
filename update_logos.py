import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

corporate_html = '''    <div class="clients-panel active" id="panel-corporate" data-aos="fade-up">
      <div class="logo-grid">
        <div class="logo-card"><img src="https://logo.clearbit.com/perkinelmer.com" alt="PerkinElmer" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">PerkinElmer</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/ashland.com" alt="Ashland" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Ashland</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/gaininsights.com" alt="GainInsights" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">GainInsights</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/iciciprulife.com" alt="ICICI Prudential" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">ICICI Prudential</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/tatacapital.com" alt="Tata Capital" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Tata Capital</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/axisbank.com" alt="Axis Bank" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Axis Bank</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/indusind.com" alt="IndusInd Bank" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">IndusInd Bank</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/scor.com" alt="SCOR" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">SCOR</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/sace.it" alt="SACE" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">SACE &middot; Gruppo CDP</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/aventri.com" alt="Aventri" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Aventri</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/hdfcbank.com" alt="HDFC Bank" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">HDFC Bank</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/bajajfinserv.in" alt="Bajaj Finserv" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Bajaj Finserv</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/foton-global.com" alt="Foton" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Foton</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/goibibo.com" alt="Goibibo" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Goibibo.com</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/yesbank.in" alt="Yes Bank" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Yes Bank</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/hrblock.com" alt="H&R Block" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">H&amp;R Block</span></div>
      </div>
    </div>'''

retail_html = '''    <div class="clients-panel" id="panel-retail" data-aos="fade-up">
      <div class="logo-grid">
        <div class="logo-card"><img src="https://logo.clearbit.com/shopforaurelia.com" alt="Aurelia" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Aurelia</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/blackberrys.com" alt="BlackBerrys" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">BlackBerrys</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/abfrl.com" alt="Aditya Birla Fashion" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Aditya Birla Fashion</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/bose.com" alt="Bose" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Bose</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/ddecor.com" alt="D'Decor" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">D'Decor</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/lacoste.com" alt="Lacoste" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Lacoste</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/helioswatchstore.com" alt="Helios by Titan" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Helios by Titan</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/visionexpress.in" alt="Vision Express" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Vision Express</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/goldsgym.in" alt="Gold's Gym" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Gold's Gym</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/multifit.co.in" alt="MultiFit" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">MultiFit</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/lakmesalon.in" alt="Lakmé Salon" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Lakmé Salon</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/apollopharmacy.in" alt="Apollo Pharmacy" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Apollo Pharmacy</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/puma.com" alt="Puma" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Puma</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/bigbasket.com" alt="BigBasket" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">BigBasket</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/vanheusenindia.com" alt="Van Heusen" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Van Heusen</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/kawediyajewellers.com" alt="Kawediya Jewellers" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Kawediya Jewellers</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/planetfashion.in" alt="Planet Fashion" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Planet Fashion</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/teapost.in" alt="Tea Post" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Tea Post</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/smoor.in" alt="Smoor" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Smoor</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/mcdonalds.com" alt="McDonald's" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">McDonald's</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/thebarstockexchange.com" alt="The Bar Stock Exchange" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">The Bar Stock Exchange</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/nrshospital.com" alt="NRS Hospital" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">NRS Hospital</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/levi.in" alt="Levi's" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Levi's</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/adidas.com" alt="Adidas" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Adidas</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/nike.com" alt="Nike" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Nike</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/reebok.com" alt="Reebok" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Reebok</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/gangareyenation.com" alt="Gangar Eyenation" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Gangar Eyenation</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/patanjaliayurved.net" alt="Patanjali" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Patanjali</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/madoverdonuts.com" alt="Mad Over Donuts" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Mad Over Donuts</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/justintime.in" alt="Just In Time" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Just In Time</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/wowmomo.com" alt="Wow! Momo" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Wow! Momo</span></div>
        <div class="logo-card"><img src="https://logo.clearbit.com/wowmomo.com" alt="Wow! China" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"><span style="display:none;">Wow! China</span></div>
      </div>
    </div>'''

c = re.sub(r'<div class="clients-panel active" id="panel-corporate".*?</div>\s*</div>', corporate_html, c, flags=re.DOTALL)
c = re.sub(r'<div class="clients-panel" id="panel-retail".*?</div>\s*</div>', retail_html, c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Logos updated!')
