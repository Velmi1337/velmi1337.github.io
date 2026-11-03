// SPDX-License-Identifier: GPL-3.0-only
(() => {
  const root = document.documentElement;
  root.classList.add('js');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const dialog = document.querySelector('#appearance');
  const update = () => {
    document.querySelectorAll('[data-set-mode]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.setMode === root.dataset.mode)));
    document.querySelectorAll('[data-set-palette]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.setPalette === root.dataset.palette)));
  };
  document.querySelector('[data-open-appearance]')?.addEventListener('click', () => { update(); dialog.showModal(); });
  document.querySelector('[data-close-appearance]')?.addEventListener('click', () => dialog.close());
  dialog?.addEventListener('click', e => { if (e.target === dialog) { const r = dialog.getBoundingClientRect(); if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dialog.close(); } });
  document.querySelectorAll('[data-set-mode],[data-set-palette]').forEach(button => button.addEventListener('click', () => {
    const kind = button.dataset.setMode ? 'mode' : 'palette';
    root.dataset[kind] = button.dataset.setMode || button.dataset.setPalette;
    try { localStorage.setItem('velmi-md3-' + kind, root.dataset[kind]); } catch {}
    update();
  }));
  document.addEventListener('pointerdown', event => {
    const target = event.target.closest('.state-layer');
    if (!target || reduced.matches || event.button !== 0) return;
    const rect = target.getBoundingClientRect();
    const ripple = document.createElement('span');
    const size = Math.max(rect.width, rect.height) * 2;
    ripple.className = 'ripple'; ripple.setAttribute('aria-hidden', 'true');
    Object.assign(ripple.style, { width: size+'px', height:size+'px', left:event.clientX-rect.left-size/2+'px', top:event.clientY-rect.top-size/2+'px' });
    target.append(ripple);
    ripple.animate([{transform:'scale(0)',opacity:'.18'},{transform:'scale(1)',opacity:'0'}], {duration:600,easing:'cubic-bezier(.2,0,0,1)'}).onfinish = () => ripple.remove();
  });
  if (!reduced.matches && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.animate([{opacity:0,transform:'translateY(18px)'},{opacity:1,transform:'translateY(0)'}], {duration:500,easing:'cubic-bezier(.38,1.21,.22,1)'});
      observer.unobserve(entry.target);
    }), {threshold:.08});
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  }
  update();
})();
