/**
 * Componente: dmc-button
 * Ubicación: components/ui/button/button.js
 * Descripción: Botón de diseño institucional con variantes (gold, navy, outline)
 */

class DmcButton extends HTMLElement {
  connectedCallback() {
    const href = this.getAttribute('href') || '#';
    const variant = this.getAttribute('variant') || 'gold';
    const icon = this.getAttribute('icon') || '';
    const text = this.textContent.trim() || this.getAttribute('text') || '';
    const target = this.getAttribute('target') || '';
    const rel = target === '_blank' ? 'noopener noreferrer' : '';

    let baseClass = 'inline-flex items-center justify-center gap-2 font-bold px-5 py-2.5 rounded-xl text-xs sm:text-sm uppercase tracking-wider transition-all shadow-md ';
    if (variant === 'gold') {
      baseClass += 'btn-gold text-slate-950 hover:-translate-y-0.5';
    } else if (variant === 'navy') {
      baseClass += 'btn-navy text-white hover:-translate-y-0.5';
    } else if (variant === 'outline') {
      baseClass += 'border border-amber-500/40 text-amber-400 hover:bg-amber-500/10 hover:border-amber-400 hover:-translate-y-0.5';
    }

    this.innerHTML = `
      <a href="${href}" class="${baseClass}" ${target ? `target="${target}"` : ''} ${rel ? `rel="${rel}"` : ''}>
        ${icon ? `<i class="${icon}"></i>` : ''}
        <span>${text}</span>
      </a>
    `;
  }
}

if (!customElements.get('dmc-button')) {
  customElements.define('dmc-button', DmcButton);
}
