document.addEventListener('DOMContentLoaded', () => {
  const cards = [...document.querySelectorAll('.journal-card')];
  if (cards.length) {
    const input = document.getElementById('article-search');
    const filters = document.querySelector('.journal-filters');
    const buttons = [...filters.querySelectorAll('button')];
    const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    const requested = new URLSearchParams(location.search).get('categoria');
    let topic = buttons.some(button => button.dataset.topic === requested) ? requested : 'todos';
    document.querySelector('.journal-search').hidden = false;
    document.querySelector('.journal-toolbar').hidden = false;
    const update = () => {
      const query = normalize(input.value.trim());
      let count = 0;
      cards.forEach(card => {
        card.hidden = !(topic === 'todos' || card.dataset.category === topic) || !normalize(card.dataset.search).includes(query);
        if (!card.hidden) count++;
      });
      buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.topic === topic)));
      document.querySelector('.results-count').textContent = `${count} artigo${count === 1 ? '' : 's'}`;
      document.querySelector('.journal-empty').hidden = count !== 0;
    };
    filters.addEventListener('click', event => {
      const button = event.target.closest('button[data-topic]');
      if (!button) return;
      topic = button.dataset.topic;
      update();
    });
    input.addEventListener('input', update);
    document.getElementById('clear-search').addEventListener('click', () => {
      topic = 'todos'; input.value = ''; update(); input.focus();
    });
    update();
  }
  const content = document.getElementById('article-content');
  const progress = document.querySelector('.reading-progress span');
  if (content && progress) {
    let scheduled = false;
    const updateProgress = () => {
      const rect = content.getBoundingClientRect();
      const distance = Math.max(1, rect.height - window.innerHeight);
      const ratio = Math.min(1, Math.max(0, -rect.top / distance));
      progress.style.transform = `scaleX(${ratio})`;
      scheduled = false;
    };
    const schedule = () => {
      if (!scheduled) { scheduled = true; requestAnimationFrame(updateProgress); }
    };
    window.addEventListener('scroll', schedule, { passive: true });
    window.addEventListener('resize', schedule);
    updateProgress();
  }
  const copy = document.querySelector('.copy-article');
  if (copy && navigator.clipboard && window.isSecureContext) {
    copy.hidden = false;
    copy.addEventListener('click', async () => {
      const url = new URL(location.href); url.hash = '';
      const status = document.querySelector('.share-status');
      try { await navigator.clipboard.writeText(url.href); status.textContent = 'Link copiado.'; }
      catch { status.textContent = 'Copie o endereço na barra do navegador.'; }
    });
  }
});
