import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Title & Meta
c = c.replace('<title>Space Dynamics | Commercial Real Estate Advisory — Pune &amp; Mumbai</title>', '<title>Space Dynamics | Commercial Real Estate Specialists</title>')
c = c.replace('based in Pune, India, specializing in retail leasing, commercial sales and investment advisory since 2008.', 'specializing in very niche and select works only.')

# 2. Hero & Header
c = c.replace('<span class=\"brand-sub\">CRE Advisory · Pune &amp; Mumbai</span>', '<span class=\"brand-sub\">Specialist CRE Advisory</span>')
c = c.replace('<div class=\"hero-eyebrow\">Boutique CRE Advisory · Pune, Maharashtra</div>', '<div class=\"hero-eyebrow\">Boutique CRE Advisory · Specialists in Niche Works</div>')
c = c.replace('<div class=\"stat-label\">Pune &amp; Mumbai Presence</div>', '<div class=\"stat-label\">Select Niche Projects</div>')

# 3. About us / Timeline
c = re.sub(r'based in Pune, Maharashtra.*?in Mumbai\.', 'specializing in very niche and select commercial real estate projects.', c, flags=re.DOTALL)
c = c.replace('Kotak Mahindra, Mumbai', 'Kotak Mahindra')
c = c.replace('reunites in Pune to launch', 'reunites to launch')
c = c.replace('partner for commercial real estate in Pune and Mumbai,', 'partner for commercial real estate,')

# 4. Founders
c = c.replace('Leads Pune Region', 'Specialist')
c = c.replace('Leads Mumbai Region', 'Specialist')
c = c.replace('Leading the Pune business since 2008.', '')
c = c.replace('Leading the Mumbai business since 2008.', '')
c = c.replace('<span><i class=\"fa-solid fa-location-dot\"></i> Pune</span>', '')
c = c.replace('<span><i class=\"fa-solid fa-location-dot\"></i> Mumbai</span>', '')
c = c.replace('<span><i class=\"fa-solid fa-graduation-cap\"></i> Mumbai University</span>', '')
c = c.replace('from Mumbai University ', '')

# 5. Milestones
c = c.replace('across Pune.', '.')
c = c.replace('across Pune', '')

# 6. FAQ
c = c.replace('<p>We are based in Pune, Maharashtra, with business leadership covering both the Pune and Mumbai regions.</p>', '<p>We are specialists taking on very niche and select works only. (See Contact section for our office addresses).</p>')
c = c.replace('Stay ahead of Pune\'s commercial market', 'Stay ahead of the commercial market')

# 7. Footer
c = c.replace('based in Pune, specializing', 'specializing')

# 8. Mandates (Invitation basis)
c = c.replace('Exclusive mandates on marquee developer projects', 'Mandate sales strictly on an invitation basis for marquee developer projects')
c = c.replace('An entire retail high-street strata sold by Space Dynamics on an exclusive mandate.', 'An entire retail high-street strata sold by Space Dynamics (by invitation mandate).')
c = c.replace('A landmark Balewadi high-street tower, fully leased under an exclusive Space Dynamics mandate.', 'A landmark Balewadi high-street tower, fully leased under an invitation-basis mandate.')
c = c.replace('Do you work with developers on exclusive mandates?', 'Do you take on mandate sales for developers?')
c = c.replace('Yes — projects such as SBH1, SBH2, SBH3, ONE WEST Baner and VTP R10 Kharadi were all handled on an exclusive mandate basis.', 'We position mandate sales strictly on an invitation basis. Projects such as SBH1, SBH2, SBH3, ONE WEST Baner and VTP R10 Kharadi are examples of our select works.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done!')
