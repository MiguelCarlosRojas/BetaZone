/**
 * Componente: dmc-modal
 * Ubicación: components/ui/modal/modal.js
 * Descripción: Modal interactivo para respuestas de formularios, avisos y alertas
 */

class DmcModal extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <div id="feedback-modal" class="fixed inset-0 bg-slate-950/75 backdrop-blur-sm z-50 hidden items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-8 text-center shadow-2xl border border-slate-100 transform transition-all">
          <i id="modal-icon" class="fas fa-check-circle text-5xl text-emerald-500 mb-4 animate-bounce"></i>
          <h3 id="modal-title" class="font-heading font-black text-2xl text-slate-900 mb-2">¡Operación Exitosa!</h3>
          <p id="modal-message" class="text-slate-600 text-sm leading-relaxed mb-6">Su solicitud ha sido procesada correctamente.</p>
          <button type="button" onclick="window.closeFeedbackModal()" class="w-full btn-gold text-slate-950 font-bold py-3 rounded-xl text-xs uppercase tracking-wider transition-all">
            Entendido
          </button>
        </div>
      </div>
    `;
  }
}

if (!customElements.get('dmc-modal')) {
  customElements.define('dmc-modal', DmcModal);
}
