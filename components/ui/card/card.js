/**
 * Componente: dmc-card
 * Ubicación: components/ui/card/card.js
 * Descripción: Tarjeta de contenido estandarizada con variantes (glass, dark, stat)
 */

class DmcCard extends HTMLElement {
  connectedCallback() {
    const variant = this.getAttribute('variant') || 'glass'; // glass, dark, stat
    const icon = this.getAttribute('icon') || '';
    const title = this.getAttribute('title') || '';
    const badge = this.getAttribute('badge') || '';

    let cardClass = 'p-6 transition-all ';
    if (variant === 'glass') {
      cardClass += 'glass-card text-slate-800';
    } else if (variant === 'dark') {
      cardClass += 'glass-card-dark text-white';
    } else if (variant === 'stat') {
      cardClass += 'stat-card text-center';
    }

    const originalContent = this.innerHTML;

    this.innerHTML = `
      <div class="${cardClass}">
        ${badge ? `<span class="text-[10px] font-bold uppercase tracking-wider bg-amber-100 text-amber-800 px-2.5 py-1 rounded-full inline-block mb-3">${badge}</span>` : ''}
        ${icon ? `<div class="w-12 h-12 rounded-xl bg-amber-100 text-amber-600 flex items-center justify-center text-xl mb-4"><i class="${icon}"></i></div>` : ''}
        ${title ? `<h3 class="font-heading font-bold text-lg mb-2">${title}</h3>` : ''}
        <div>${originalContent}</div>
      </div>
    `;
  }
}

if (!customElements.get('dmc-card')) {
  customElements.define('dmc-card', DmcCard);
}
