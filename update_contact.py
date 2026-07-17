import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

founder_old = """          <span class="founder-role">Co-Founder · Specialist</span>
          <p>A management graduate from Symbiosis (Batch of 2000) with more than 23 years of corporate experience across Investment, Banking and Media. </p>
          <div class="founder-tags">
            <span><i class="fa-solid fa-graduation-cap"></i> Symbiosis, 2000</span>
            <span><i class="fa-solid fa-briefcase"></i> 23+ Yrs Experience</span>
            
          </div>"""

founder_new = """          <span class="founder-role">Enabler, Commercial Realty Investments &amp; Lease</span>
          <p>A management graduate from Symbiosis (Batch of 2000) with more than 23 years of corporate experience across Investment, Banking and Media. </p>
          <div class="founder-tags">
            <span><i class="fa-solid fa-graduation-cap"></i> Symbiosis, 2000</span>
            <span><i class="fa-solid fa-briefcase"></i> 23+ Yrs Experience</span>
            <a href="https://www.linkedin.com/in/satbirbagga" target="_blank" style="color:var(--gold);"><i class="fa-brands fa-linkedin-in"></i></a>
            <a href="https://twitter.com/CRE_Dynamics" target="_blank" style="color:var(--gold);"><i class="fa-brands fa-x-twitter"></i></a>
          </div>"""

c = c.replace(founder_old, founder_new)

contact_old = """        <div class="contact-item">
          <div class="ic"><i class="fa-solid fa-phone"></i></div>
          <div><h5>Phone</h5><p>+91 98XXX XXXXX</p></div>
        </div>
        <div class="contact-item">
          <div class="ic"><i class="fa-solid fa-envelope"></i></div>
          <div><h5>Email</h5><p>info@spacedynamics.in</p></div>
        </div>"""

contact_new = """        <div class="contact-item">
          <div class="ic"><i class="fa-solid fa-phone"></i></div>
          <div><h5>Phone</h5><p><a href="tel:+919822222666">+91 98222 22666</a></p></div>
        </div>
        <div class="contact-item">
          <div class="ic"><i class="fa-solid fa-envelope"></i></div>
          <div><h5>Email</h5><p><a href="mailto:satbir.bagga@spacedynamics.in">satbir.bagga@spacedynamics.in</a><br><a href="mailto:satbir.bagga@gmail.com">satbir.bagga@gmail.com</a></p></div>
        </div>"""

c = c.replace(contact_old, contact_new)


socials_old = """          <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
          <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="#" aria-label="Twitter"><i class="fa-brands fa-x-twitter"></i></a>"""

socials_new = """          <a href="https://www.linkedin.com/in/satbirbagga" aria-label="LinkedIn" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
          <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="https://twitter.com/CRE_Dynamics" aria-label="Twitter" target="_blank"><i class="fa-brands fa-x-twitter"></i></a>"""

c = c.replace(socials_old, socials_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Contact details updated successfully!')
