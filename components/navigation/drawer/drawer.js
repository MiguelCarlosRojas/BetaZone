/**
 * Componente: dmc-drawer
 * Ubicación: components/navigation/drawer/drawer.js
 * Descripción: Menú lateral responsivo deslizable (Drawer) para dispositivos móviles
 */

class DmcDrawer extends HTMLElement {
  connectedCallback() {
    const root = this.getAttribute('root-prefix') || './';

    this.innerHTML = `
      <div id="mobile-backdrop" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 hidden transition-opacity"></div>
      <div id="mobile-menu" class="fixed top-0 right-0 h-full w-4/5 max-w-sm bg-dmcNavy-900 border-l border-amber-500/30 z-50 transform translate-x-full transition-transform duration-300 p-6 flex flex-col justify-between overflow-y-auto">
        <div>
          <div class="flex items-center justify-between pb-6 border-b border-slate-800">
            <div class="flex items-center gap-3">
              <img src="${root}img/escudo-dmc.svg" alt="Escudo DMC" class="h-10 w-auto">
              <div>
                <span class="font-heading font-black text-white text-base block leading-tight">I.E. DMC</span>
                <span class="text-[10px] text-amber-400 font-bold tracking-wider uppercase">Mala - Cañete</span>
              </div>
            </div>
            <button id="mobile-menu-close" class="text-slate-400 hover:text-white text-2xl p-1" aria-label="Cerrar Menú">
              <i class="fas fa-times"></i>
            </button>
          </div>

          <nav class="flex flex-col gap-3 mt-6 text-slate-200 text-sm font-semibold">
            <a href="${root}" class="hover:text-amber-400 py-2 border-b border-slate-800/60 flex items-center justify-between">
              <span><i class="fas fa-home w-6 text-amber-400"></i> Inicio</span>
              <i class="fas fa-chevron-right text-xs"></i>
            </a>
            <a href="${root}pages/institutional/about" class="hover:text-amber-400 py-2 border-b border-slate-800/60 flex items-center justify-between">
              <span><i class="fas fa-landmark w-6 text-amber-400"></i> Nosotros</span>
              <i class="fas fa-chevron-right text-xs"></i>
            </a>
            <a href="${root}pages/academics/pedagogical-proposal" class="hover:text-amber-400 py-2 border-b border-slate-800/60 flex items-center justify-between">
              <span><i class="fas fa-graduation-cap w-6 text-amber-400"></i> Propuesta Pedagógica</span>
              <i class="fas fa-chevron-right text-xs"></i>
            </a>
            <a href="${root}pages/school-life/workshops-overview" class="hover:text-amber-400 py-2 border-b border-slate-800/60 flex items-center justify-between">
              <span><i class="fas fa-palette w-6 text-amber-400"></i> Talleres & Vida Escolar</span>
              <i class="fas fa-chevron-right text-xs"></i>
            </a>
            <a href="${root}pages/services/admissions/" class="hover:text-amber-400 py-2 border-b border-slate-800/60 flex items-center justify-between">
              <span><i class="fas fa-user-plus w-6 text-amber-400"></i> Admisión & Matrícula</span>
              <i class="fas fa-chevron-right text-xs"></i>
            </a>
            <a href="${root}pages/services/contact" class="hover:text-amber-400 py-2 border-b border-slate-800/60 flex items-center justify-between">
              <span><i class="fas fa-map-marker-alt w-6 text-amber-400"></i> Contacto</span>
              <i class="fas fa-chevron-right text-xs"></i>
            </a>
          </nav>
        </div>

        <div class="pt-6 border-t border-slate-800 flex flex-col gap-3">
          <a href="${root}pages/services/contact#mesa-de-partes" class="btn-gold text-slate-950 font-bold py-3 text-center rounded-xl text-xs uppercase tracking-wider block">
            <i class="fas fa-file-invoice mr-1.5"></i> Mesa de Partes Virtual
          </a>
          <p class="text-[11px] text-slate-400 text-center">
            &copy; I.E. Dionisio Manco Campos &bull; Mala
          </p>
        </div>
      </div>
    `;
  }
}

if (!customElements.get('dmc-drawer')) {
  customElements.define('dmc-drawer', DmcDrawer);
}
