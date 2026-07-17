import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Nav Links
content = re.sub(r'<li><a href="#projects">Projects</a></li>\s*<li><a href="#clients">Clients</a></li>\s*<li><a href="#success\">Success Stories</a></li>\s*<li><a href=\"#why-us\">Why Us</a></li>\s*<li><a href=\"#testimonials\">Testimonials</a></li>', '<li><a href="#clients">Clients</a></li>\n        <li><a href="#success">Work Milestone\'s</a></li>', content)

# 2. Services Dropdown
dropdown_old = r'<div class="mega-menu">\s*<a href="#services"><i class="fa-solid fa-store"></i> Retail Leasing</a>\s*<a href="#services"><i class="fa-solid fa-building"></i> Commercial Leasing</a>\s*<a href="#services"><i class="fa-solid fa-briefcase"></i> Office Sales</a>\s*<a href="#services"><i class="fa-solid fa-shop"></i> Retail Sales</a>\s*<a href="#services"><i class="fa-solid fa-chart-line"></i> Investment Advisory</a>\s*<a href="#services"><i class="fa-solid fa-bullhorn\"></i> Project Marketing</a>\s*<a href="#services"><i class="fa-solid fa-handshake\"></i> Landlord Representation</a>\s*<a href="#services"><i class="fa-solid fa-user-tie\"></i> Tenant Representation</a>\s*<a href="#services"><i class="fa-solid fa-scale-balanced\"></i> Legal Advisory</a>\s*<a href="#services"><i class="fa-solid fa-comments-dollar\"></i> Negotiation</a>\s*</div>'
dropdown_new = '''<div class="mega-menu">
            <a href="#services"><i class="fa-solid fa-chart-line"></i> Investment Advisory (Commercial Spaces only)</a>
            <a href="#services"><i class="fa-solid fa-store"></i> Leasing (Retail & Office)</a>
            <a href="#services"><i class="fa-solid fa-bullhorn"></i> Project Marketing (Commercial Spaces & Studios)</a>
          </div>'''
content = re.sub(dropdown_old, dropdown_new, content)

# 3. What We Do Cards
grid_old = r'<div class="services-grid">.*?</div>\n  </div>\n</section>'
grid_new = '''<div class="services-grid">
      <div class="service-card" data-aos="fade-up"><span class="num">01</span><div class="service-icon"><i class="fa-solid fa-chart-line"></i></div><h3>INVESTMENT ADVISORY</h3><p>Commercial Spaces only</p></div>
      <div class="service-card" data-aos="fade-up" data-aos-delay="50"><span class="num">02</span><div class="service-icon"><i class="fa-solid fa-store"></i></div><h3>LEASING</h3><p>Retail &amp; Office</p></div>
      <div class="service-card" data-aos="fade-up" data-aos-delay="100"><span class="num">03</span><div class="service-icon"><i class="fa-solid fa-bullhorn"></i></div><h3>PROJECT MARKETING</h3><p>Commercial Spaces &amp; Studios</p></div>
    </div>
  </div>
</section>'''
content = re.sub(grid_old, grid_new, content, flags=re.DOTALL)

# 4. Remove Projects Section
content = re.sub(r'<!-- ===================== 5\. FEATURED PROJECTS ===================== -->\s*<section class="section-pad bg-gray" id="projects">.*?</section>\s*', '', content, flags=re.DOTALL)

# 5. Success Stories -> Work Milestones
content = re.sub(r'<h2>Success Stories</h2>', '<h2>Work Milestone\'s</h2>', content)

# 6. Remove Why Choose Us Section
content = re.sub(r'<!-- ===================== 7\. WHY CHOOSE US ===================== -->\s*<section class="section-pad bg-navy" id="why-us">.*?</section>\s*', '', content, flags=re.DOTALL)

# 7. Remove Testimonials Section
content = re.sub(r'<!-- ===================== 8\. TESTIMONIALS ===================== -->\s*<section class="section-pad bg-gray" id="testimonials">.*?</section>\s*', '', content, flags=re.DOTALL)

# 8. Footer Links
content = re.sub(r'<li><a href="#success">Success Stories</a></li>\s*<li><a href="#why-us">Why Choose Us</a></li>\s*<li><a href="#testimonials\">Testimonials</a></li>', '<li><a href="#success">Work Milestone\'s</a></li>', content)

# 9. Footer Services
content = re.sub(r'<li><a href="#services">Retail Leasing</a></li>\s*<li><a href="#services">Commercial Leasing</a></li>\s*<li><a href="#services">Investment Advisory</a></li>\s*<li><a href="#services">Project Marketing</a></li>\s*<li><a href="#services\">Legal Advisory</a></li>', '<li><a href="#services">Investment Advisory</a></li>\n          <li><a href="#services">Leasing</a></li>\n          <li><a href="#services">Project Marketing</a></li>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
