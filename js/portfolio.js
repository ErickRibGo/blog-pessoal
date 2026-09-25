document.addEventListener('DOMContentLoaded', () => {
  const filters = document.querySelector('.project-filters');
  if (filters) {
    filters.hidden = false;
    const cards = [...document.querySelectorAll('.project[data-category]')];
    filters.addEventListener('click', event => {
      const button = event.target.closest('button[data-filter]');
      if (!button) return;
      const selected = button.dataset.filter.split(',');
      let count = 0;
      for (const card of cards) {
        card.hidden = !selected.includes('all') && !selected.includes(card.dataset.category);
        if (!card.hidden) count++;
      }
      filters.querySelectorAll('button').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      document.getElementById('filter-status').textContent = `${count} projeto${count === 1 ? '' : 's'} em exibição.`;
    });
  }
  const copyButton = document.querySelector('.copy-email');
  if (copyButton && navigator.clipboard && window.isSecureContext) {
    copyButton.hidden = false;
    copyButton.addEventListener('click', async () => {
      const status = document.querySelector('.copy-status');
      try {
        await navigator.clipboard.writeText('erickribeirogon@gmail.com');
        status.textContent = 'E-mail copiado.';
      } catch {
        status.textContent = 'E-mail: erickribeirogon@gmail.com';
      }
    });
  }
});
