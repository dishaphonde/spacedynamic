/* ==========================================================================
   SPACE DYNAMICS — main.js
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Preloader ---------- */
  const preloader = document.getElementById('preloader');
  window.addEventListener('load', () => {
    setTimeout(() => preloader && preloader.classList.add('loaded'), 400);
  });
  // Fallback in case 'load' is delayed
  setTimeout(() => preloader && preloader.classList.add('loaded'), 2500);

  /* ---------- AOS init (graceful fallback if CDN blocked) ---------- */
  if (window.AOS) {
    AOS.init({ duration: 800, easing: 'ease-out-cubic', once: true, offset: 80 });
  } else {
    // Fallback: IntersectionObserver reveal for [data-aos]
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('aos-animate'); io.unobserve(e.target); } });
    }, { threshold: 0.15 });
    document.querySelectorAll('[data-aos]').forEach(el => io.observe(el));
  }

  /* ---------- Sticky navbar + scroll progress ---------- */
  const navbar = document.getElementById('navbar');
  const progressBar = document.getElementById('scroll-progress');
  const backToTop = document.getElementById('back-to-top');

  function onScroll () {
    const scrollY = window.scrollY || window.pageYOffset;
    navbar.classList.toggle('scrolled', scrollY > 60);
    backToTop.classList.toggle('show', scrollY > 500);

    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;
    progressBar.style.width = pct + '%';
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ---------- Mobile nav toggle ---------- */
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
    document.body.classList.toggle('nav-open', navMenu.classList.contains('active'));
  });

  // Close mobile nav on resize past breakpoint
  window.addEventListener('resize', () => {
    if (window.innerWidth > 992 && navMenu.classList.contains('active')) {
      navMenu.classList.remove('active');
      navToggle.classList.remove('active');
      document.body.classList.remove('nav-open');
    }
  });

  // Mobile mega-menu accordion open
  document.querySelectorAll('.nav-menu > li').forEach(li => {
    const link = li.querySelector('> a');
    const mega = li.querySelector('.mega-menu');
    if (!mega) return;
    link.addEventListener('click', (e) => {
      if (window.innerWidth <= 992) {
        e.preventDefault();
        li.classList.toggle('mega-open');
      }
    });
  });

  // Close mobile nav on link click
  document.querySelectorAll('.mega-menu a, .nav-menu > li > a:not(:has(+ .mega-menu))').forEach(a => {
    a.addEventListener('click', () => {
      navMenu.classList.remove('active');
      navToggle.classList.remove('active');
      document.body.classList.remove('nav-open');
    });
  });

  /* ---------- Search overlay ---------- */
  const searchBtn = document.getElementById('navSearchBtn');
  const searchOverlay = document.getElementById('searchOverlay');
  const searchClose = document.getElementById('searchClose');
  const searchInput = document.getElementById('searchInput');

  searchBtn.addEventListener('click', () => {
    searchOverlay.classList.add('active');
    setTimeout(() => searchInput.focus(), 300);
  });
  searchClose.addEventListener('click', () => searchOverlay.classList.remove('active'));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') searchOverlay.classList.remove('active'); });

  searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const q = searchInput.value.trim().toLowerCase();
      searchOverlay.classList.remove('active');
      if (!q) return;
      // Simple on-page search: jump to first matching section/project heading
      const targets = document.querySelectorAll('h2, h3, h4');
      let matchEl = null;
      targets.forEach(t => { if (!matchEl && t.textContent.toLowerCase().includes(q)) matchEl = t; });
      if (matchEl) matchEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      searchInput.value = '';
    }
  });

  /* ---------- Animated counters ---------- */
  const counters = document.querySelectorAll('.stat-num[data-target]');
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach(c => counterObserver.observe(c));

  function animateCounter (el) {
    const target = parseInt(el.getAttribute('data-target'), 10);
    const suffix = el.getAttribute('data-suffix') || '';
    const duration = 1800;
    const start = performance.now();
    function tick (now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const val = Math.floor(eased * target);
      el.childNodes[0].nodeValue = val;
      if (progress < 1) requestAnimationFrame(tick);
      else el.childNodes[0].nodeValue = target;
    }
    el.innerHTML = '0<span>' + suffix + '</span>';
    requestAnimationFrame(tick);
  }

  /* ---------- Key Clients tabs ---------- */
  document.querySelectorAll('.clients-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.clients-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.clients-panel').forEach(p => p.classList.remove('active'));
      tab.classList.add('active');
      document.getElementById(tab.dataset.target).classList.add('active');
    });
  });

  /* ---------- Project filter ---------- */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      projectCards.forEach(card => {
        const show = filter === 'all' || card.dataset.status === filter;
        card.style.display = show ? '' : 'none';
      });
    });
  });

  /* ---------- Project modal ---------- */
  const modalOverlay = document.getElementById('projectModal');
  const modalMedia = modalOverlay.querySelector('.modal-media img');
  const modalBody = modalOverlay.querySelector('.modal-body');
  const modalClose = modalOverlay.querySelector('.modal-close');

  document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('click', () => {
      const img = card.querySelector('.project-media img').src;
      const title = card.querySelector('h3').textContent;
      const loc = card.querySelector('.project-loc').textContent;
      const year = card.querySelector('.project-year').textContent;
      const status = card.querySelector('.project-status').textContent;
      const desc = card.dataset.full || card.querySelector('p').textContent;

      modalMedia.src = img;
      modalMedia.alt = title;
      modalBody.innerHTML = `
        <div class="modal-meta">
          <span><i class="fa-solid fa-location-dot"></i> ${loc}</span>
          <span><i class="fa-regular fa-calendar"></i> ${year}</span>
          <span><i class="fa-solid fa-circle-check"></i> ${status}</span>
        </div>
        <h2>${title}</h2>
        <p>${desc}</p>
      `;
      modalOverlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeModal () {
    modalOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }
  modalClose.addEventListener('click', closeModal);
  modalOverlay.addEventListener('click', (e) => { if (e.target === modalOverlay) closeModal(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.faq-item').forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => {
        i.classList.remove('open');
        i.querySelector('.faq-answer').style.maxHeight = null;
      });
      if (!isOpen) {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  /* ---------- Testimonials — Swiper ---------- */
  if (window.Swiper) {
    new Swiper('.testimonial-swiper', {
      loop: true,
      autoplay: { delay: 4500, disableOnInteraction: false },
      spaceBetween: 28,
      pagination: { el: '.swiper-pagination', clickable: true },
      breakpoints: {
        0: { slidesPerView: 1 },
        768: { slidesPerView: 2 },
        1100: { slidesPerView: 3 }
      }
    });
  }

  /* ---------- Contact form (front-end only) ---------- */
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = contactForm.querySelector('button[type="submit"]');
      const originalText = btn.innerHTML;
      btn.innerHTML = '<i class="fa-solid fa-check"></i> Message Sent';
      btn.disabled = true;
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.disabled = false;
        contactForm.reset();
      }, 2600);
    });
  }

  /* ---------- Newsletter form ---------- */
  const newsletterForm = document.getElementById('newsletterForm');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = newsletterForm.querySelector('button');
      btn.textContent = 'Subscribed ✓';
      setTimeout(() => { btn.textContent = 'Subscribe'; newsletterForm.reset(); }, 2400);
    });
  }

  /* ---------- Cookie banner ---------- */
  const cookieBanner = document.getElementById('cookieBanner');
  const cookieAccept = document.getElementById('cookieAccept');
  if (!localStorage.getItem('sd_cookie_consent')) {
    setTimeout(() => cookieBanner.classList.add('show'), 1600);
  }
  cookieAccept.addEventListener('click', () => {
    localStorage.setItem('sd_cookie_consent', 'true');
    cookieBanner.classList.remove('show');
  });

  /* ---------- Smooth scroll for in-page anchors ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId.length > 1) {
        const target = document.querySelector(targetId);
        if (target) {
          e.preventDefault();
          const offset = target.getBoundingClientRect().top + window.pageYOffset - 84;
          window.scrollTo({ top: offset, behavior: 'smooth' });
        }
      }
    });
  });

  /* ---------- Active nav link on scroll ---------- */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-menu > li');
  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(sec => {
      const top = sec.offsetTop - 120;
      if (window.scrollY >= top) current = sec.getAttribute('id');
    });
    navLinks.forEach(li => {
      li.classList.remove('active');
      const a = li.querySelector('a');
      if (a && a.getAttribute('href') === '#' + current) li.classList.add('active');
    });
  }, { passive: true });

  /* ---------- Simple hero parallax (disabled on mobile for performance) ---------- */
  const heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
    window.addEventListener('scroll', () => {
      if (window.innerWidth <= 768) return; // skip parallax on mobile
      const y = window.scrollY;
      if (y < window.innerHeight) heroBg.style.transform = `scale(1.08) translateY(${y * 0.25}px)`;
    }, { passive: true });
  }

});
