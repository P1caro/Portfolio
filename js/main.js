/* reveal on scroll */
const io = new IntersectionObserver(e => e.forEach(x => {
  if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target) }
}), { threshold: .15 });
document.querySelectorAll('.rv').forEach(el => io.observe(el));

/* language rings — draw the arcs when the chart scrolls into view */
const ring = document.querySelector('.ring svg');
if (ring) {
  const ro = new IntersectionObserver(e => e.forEach(x => {
    if (!x.isIntersecting) return;
    ring.querySelectorAll('.arc').forEach((a, i) => {
      setTimeout(() => { a.style.strokeDashoffset = a.dataset.off }, i * 180);
    });
    ro.disconnect();
  }), { threshold: .3 });
  ro.observe(ring);
}

/* dark / light toggle */
const tog = document.getElementById('tog');
if (tog) tog.addEventListener('click', () => {
  const r = document.documentElement;
  const t = r.dataset.theme === 'dark' ? 'light' : 'dark';
  r.dataset.theme = t;
  try { localStorage.setItem('theme', t) } catch (e) {}
});

/* "See all subjects" toggle on the coursework list */
document.querySelectorAll('.showmore').forEach(btn => {
  const list = document.getElementById(btn.dataset.target);
  if (!list) return;
  btn.addEventListener('click', () => {
    const open = list.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
    btn.querySelector('span').textContent = open ? btn.dataset.less : btn.dataset.more;
  });
});

/* scroll spy — highlights Home / About / Projects in the header */
const spy = document.querySelectorAll('nav ul a[data-spy]');
if (spy.length) {
  const secs = [...spy].map(a => document.querySelector(a.dataset.spy)).filter(Boolean);
  const mark = () => {
    let cur = secs[0];
    for (const s of secs) if (window.scrollY + 140 >= s.offsetTop) cur = s;
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 120) cur = secs[secs.length - 1];
    spy.forEach(a => a.classList.toggle('on', document.querySelector(a.dataset.spy) === cur));
  };
  mark();
  addEventListener('scroll', mark, { passive: true });
  addEventListener('resize', mark);
}

/* project slider — auto-advances every 5s */
const slides = document.querySelectorAll('.slide');
if (slides.length) {
  const dots = document.querySelectorAll('.sctl button');
  let i = 0, timer;
  const show = n => {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => s.classList.toggle('act', k === i));
    dots.forEach((d, k) => {
      d.classList.remove('act');
      if (k === i) { void d.offsetWidth; d.classList.add('act') }
    });
  };
  const play = () => { clearInterval(timer); timer = setInterval(() => show(i + 1), 5000) };
  dots.forEach((d, k) => d.addEventListener('click', () => { show(k); play() }));
  const box = document.querySelector('.slider');
  box.addEventListener('mouseenter', () => clearInterval(timer));
  box.addEventListener('mouseleave', play);
  show(0); play();
}
