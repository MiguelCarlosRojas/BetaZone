/**
 * Componente: dmc-header
 * Ubicación: components/layout/header/header.js
 * Descripción: Barra de anuncios superior y encabezado sticky con menú de navegación
 */

class DmcHeader extends HTMLElement {
  connectedCallback() {
    const root = this.getAttribute('root-prefix') || './';
    const active = this.getAttribute('active') || 'inicio';

    this.innerHTML = `
      <!-- TOP BAR INFORMATIVA -->
      <div class="top-announcement text-white py-2.5 px-4 sm:px-8 text-xs sm:text-sm font-medium w-full">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-2">
          <div class="flex flex-wrap items-center justify-center md:justify-start gap-4">
            <span><i class="fas fa-school text-amber-400 mr-1.5"></i> UGEL N° 08 Cañete &bull; Cód. Modular: <strong>0286385</strong></span>
            <span class="hidden sm:inline text-slate-400">|</span>
            <span><i class="fas fa-map-marker-alt text-amber-400 mr-1.5"></i> Jr. Enrique Swayne s/n, Mala - Cañete</span>
          </div>
          <div class="flex items-center gap-4">
            <a href="tel:013396215" class="hover:text-amber-300 transition-colors"><i class="fas fa-phone-alt text-amber-400 mr-1"></i> (01) 339-6215</a>
            <span class="text-slate-400">|</span>
            <a href="https://www.facebook.com/iepdmc" target="_blank" rel="noopener noreferrer" class="hover:text-amber-300 transition-colors flex items-center gap-1.5" title="Facebook Oficial DMC">
              <i class="fab fa-facebook text-amber-400 text-sm"></i> <span class="hidden sm:inline">Facebook Oficial</span>
            </a>
          </div>
        </div>
      </div>

      <!-- HEADER / NAVEGACIÓN -->
      <header id="main-header" class="sticky top-0 z-50 glass-nav transition-all duration-300 py-3.5 px-4 sm:px-8 shadow-md w-full">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
          
          <!-- Brand Logo -->
          <a href="${root}" class="flex items-center gap-3.5 group">
            <img src="${root}img/escudo-dmc.svg" alt="Escudo I.E. Dionisio Manco Campos" class="h-12 w-auto drop-shadow-md group-hover:scale-105 transition-transform">
            <div class="flex flex-col">
              <span class="font-heading font-black text-lg sm:text-xl text-white tracking-wide leading-tight">
                I.E. DIONISIO MANCO CAMPOS
              </span>
              <span class="text-[11px] sm:text-xs font-semibold text-amber-400 tracking-wider uppercase">
                Nivel Secundaria &bull; Mala, Cañete
              </span>
            </div>
          </a>

          <!-- Desktop Nav -->
          <nav class="hidden lg:flex items-center gap-6 xl:gap-8 font-medium text-sm text-slate-200">
            <a href="${root}" class="nav-link ${active === 'inicio' ? 'active' : ''} hover:text-amber-400 py-1">Inicio</a>
            <a href="${root}pages/institutional/about.html" class="nav-link ${active === 'nosotros' ? 'active' : ''} hover:text-amber-400 py-1">Nosotros</a>
            <a href="${root}pages/academics/pedagogical-proposal.html" class="nav-link ${active === 'propuesta' ? 'active' : ''} hover:text-amber-400 py-1">Propuesta Pedagógica</a>
            <a href="${root}pages/school-life/workshops-overview.html" class="nav-link ${active === 'talleres' ? 'active' : ''} hover:text-amber-400 py-1">Talleres & Vida Escolar</a>
            <a href="${root}pages/services/admissions/overview.html" class="nav-link ${active === 'admision' ? 'active' : ''} hover:text-amber-400 py-1">Admisión</a>
            <a href="${root}pages/services/contact.html" class="nav-link ${active === 'contacto' ? 'active' : ''} hover:text-amber-400 py-1">Contacto</a>
          </nav>

          <!-- Action Button Desktop -->
          <div class="hidden lg:flex items-center gap-3">
            <a href="${root}pages/services/contact.html#mesa-de-partes" class="inline-flex items-center gap-2 btn-gold text-slate-950 font-bold px-4 py-2.5 rounded-xl text-xs uppercase tracking-wider transition-all">
              <i class="fas fa-file-invoice"></i> Mesa de Partes
            </a>
          </div>

          <!-- Mobile Hamburger Button -->
          <button id="mobile-menu-btn" class="lg:hidden text-white hover:text-amber-400 text-2xl p-2 focus:outline-none" aria-label="Abrir Menú">
            <i class="fas fa-bars"></i>
          </button>

        </div>
      </header>
    `;
  }
}

if (!customElements.get('dmc-header')) {
  customElements.define('dmc-header', DmcHeader);
}
