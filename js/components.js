/**
 * Componentes Web Reutilizables - I.E. Dionisio Manco Campos (Mala, Cañete)
 * Web Components estándar (Custom Elements) para Navbar, Footer, Breadcrumbs y Botones
 */

// Función utilitaria para calcular la ruta relativa a la raíz según profundidad
function getRootPrefix() {
  const path = window.location.pathname.replace(/\/$/, '');
  const segments = path.split('/').filter(Boolean);
  // Si estamos en la raíz o /index
  if (segments.length === 0) return './';
  // Generar ../ tantas veces como segmentos de profundidad
  return '../'.repeat(segments.length);
}

// 1. Componente de Botón Institucional Reutilizable: <dmc-button>
class DmcButton extends HTMLElement {
  connectedCallback() {
    const href = this.getAttribute('href') || '#';
    const variant = this.getAttribute('variant') || 'gold'; // gold, navy, outline
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
customElements.define('dmc-button', DmcButton);

// 2. Componente de Breadcrumb Interactivo y Dinámico: <dmc-breadcrumb>
class DmcBreadcrumb extends HTMLElement {
  connectedCallback() {
    const root = this.getAttribute('root-prefix') || getRootPrefix();
    const current = this.getAttribute('current') || document.title.split('|')[0].trim();
    const section = this.getAttribute('section') || '';
    const category = this.getAttribute('category') || '';

    // Mapeo de secciones y categorías a URLs reales
    const sectionUrls = {
      'Institucional': `${root}pages/institutional/about`,
      'Académico': `${root}pages/academics/pedagogical-proposal`,
      'Vida Escolar': `${root}pages/school-life/workshops-overview`,
      'Servicios': `${root}pages/services/contact`
    };

    const categoryUrls = {
      'Historia': `${root}pages/institutional/history/`,
      'Símbolos': `${root}pages/institutional/symbols/`,
      'Gestión': `${root}pages/institutional/management/`,
      'Grados': `${root}pages/academics/grades/`,
      'Áreas Curriculares': `${root}pages/academics/curricular-areas/`,
      'CEBA': `${root}pages/academics/ceba/`,
      'Talleres': `${root}pages/school-life/workshops/`,
      'Estudiantes': `${root}pages/school-life/students/`,
      'Familias': `${root}pages/school-life/families/`,
      'Admisión': `${root}pages/services/admissions/`,
      'Infraestructura': `${root}pages/services/infrastructure/`,
      'Trámites': `${root}pages/services/procedures/`,
      'Noticias': `${root}pages/services/news/`
    };

    let breadcrumbsHtml = `
      <div class="bg-white border-b border-slate-200 py-3 px-4 sm:px-8 text-xs text-slate-500 font-medium">
        <div class="max-w-7xl mx-auto flex items-center gap-2 flex-wrap">
          <a href="${root}" class="text-slate-600 hover:text-amber-600 flex items-center gap-1.5 transition-colors">
            <i class="fas fa-home text-amber-500"></i> Inicio
          </a>
    `;

    if (section) {
      const sUrl = sectionUrls[section] || '#';
      breadcrumbsHtml += `
        <span class="text-slate-300">/</span>
        <a href="${sUrl}" class="text-slate-600 hover:text-amber-600 transition-colors font-semibold">${section}</a>
      `;
    }

    if (category) {
      const cUrl = categoryUrls[category] || '#';
      breadcrumbsHtml += `
        <span class="text-slate-300">/</span>
        <a href="${cUrl}" class="text-slate-600 hover:text-amber-600 transition-colors font-semibold">${category}</a>
      `;
    }

    breadcrumbsHtml += `
          <span class="text-slate-300">/</span>
          <span class="text-slate-900 font-bold truncate max-w-md">${current}</span>
        </div>
      </div>
    `;

    this.innerHTML = breadcrumbsHtml;
  }
}
customElements.define('dmc-breadcrumb', DmcBreadcrumb);

// 3. Componente de Footer Institucional Unificado y Reutilizable: <dmc-footer>
class DmcFooter extends HTMLElement {
  connectedCallback() {
    const root = this.getAttribute('root-prefix') || getRootPrefix();

    this.innerHTML = `
      <footer class="bg-dmcNavy-900 text-slate-300 pt-16 pb-12 border-t-4 border-amber-500 mt-auto">
        <div class="max-w-7xl mx-auto px-4 sm:px-8">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 pb-12 border-b border-slate-800">
            
            <!-- Columna 1: Institución y Códigos Oficiales -->
            <div class="space-y-4">
              <div class="flex items-center gap-3">
                <img src="${root}img/escudo-dmc.svg" alt="Escudo DMC" class="h-12 w-auto">
                <div>
                  <p class="font-heading font-black text-white text-base leading-tight">I.E. DIONISIO MANCO CAMPOS</p>
                  <p class="text-xs text-amber-400 font-semibold uppercase">Mala &bull; Cañete &bull; Perú</p>
                </div>
              </div>
              <p class="text-xs text-slate-400 leading-relaxed">
                Institución Educativa Pública fundada en 1962. Alma máter de la secundaria maleña dedicada a formar juventudes íntegras, científicas y solidarias.
              </p>
              <div class="text-xs text-slate-400 space-y-1">
                <p><strong>Cód. Modular Secundaria:</strong> 0286385</p>
                <p><strong>Cód. Modular CEBA:</strong> 0285676</p>
                <p><strong>Cód. Local:</strong> 353596 | UGEL 08 Cañete</p>
              </div>
            </div>

            <!-- Columna 2: Módulos Principales -->
            <div>
              <h4 class="font-heading font-bold text-white text-sm uppercase tracking-wider mb-4 border-l-2 border-amber-500 pl-2.5">
                Módulos Principales
              </h4>
              <ul class="space-y-2 text-xs">
                <li><a href="${root}" class="hover:text-amber-400 transition-colors">Inicio</a></li>
                <li><a href="${root}pages/institutional/about" class="hover:text-amber-400 transition-colors">Reseña Histórica</a></li>
                <li><a href="${root}pages/academics/pedagogical-proposal" class="hover:text-amber-400 transition-colors">Propuesta Curricular</a></li>
                <li><a href="${root}pages/academics/grades/" class="hover:text-amber-400 transition-colors">Grados de Secundaria</a></li>
                <li><a href="${root}pages/school-life/workshops/" class="hover:text-amber-400 transition-colors">Talleres & Deportes</a></li>
                <li><a href="${root}pages/services/admissions/" class="hover:text-amber-400 transition-colors">Admisión Escolar</a></li>
                <li><a href="${root}pages/services/contact" class="hover:text-amber-400 transition-colors">Contacto y Mesa de Partes</a></li>
              </ul>
            </div>

            <!-- Columna 3: Enlaces Oficiales -->
            <div>
              <h4 class="font-heading font-bold text-white text-sm uppercase tracking-wider mb-4 border-l-2 border-amber-500 pl-2.5">
                Enlaces Oficiales
              </h4>
              <ul class="space-y-2 text-xs">
                <li><a href="http://ugel08canete.gob.pe/" target="_blank" rel="noopener noreferrer" class="hover:text-amber-400 transition-colors">UGEL N° 08 Cañete</a></li>
                <li><a href="https://www.gob.pe/minedu" target="_blank" rel="noopener noreferrer" class="hover:text-amber-400 transition-colors">Ministerio de Educación (MINEDU)</a></li>
                <li><a href="https://siagie.minedu.gob.pe/" target="_blank" rel="noopener noreferrer" class="hover:text-amber-400 transition-colors">Plataforma SIAGIE</a></li>
                <li><a href="https://www.gob.pe/pronabec" target="_blank" rel="noopener noreferrer" class="hover:text-amber-400 transition-colors">PRONABEC - Beca 18</a></li>
                <li><a href="https://www.facebook.com/iepdmc" target="_blank" rel="noopener noreferrer" class="hover:text-amber-400 transition-colors">Facebook Oficial IEP DMC</a></li>
                <li><a href="https://www.facebook.com/dmc19" target="_blank" rel="noopener noreferrer" class="hover:text-amber-400 transition-colors">Facebook CEBA DMC</a></li>
              </ul>
            </div>

            <!-- Columna 4: Sede y Contacto -->
            <div class="space-y-3">
              <h4 class="font-heading font-bold text-white text-sm uppercase tracking-wider mb-4 border-l-2 border-amber-500 pl-2.5">
                Sede y Contacto
              </h4>
              <p class="text-xs text-slate-400 flex items-start gap-2">
                <i class="fas fa-map-marker-alt text-amber-400 mt-0.5"></i>
                <span>Jr. Enrique Swayne s/n, Distrito de Mala, Cañete, Lima - Perú</span>
              </p>
              <p class="text-xs text-slate-400 flex items-center gap-2">
                <i class="fas fa-phone-alt text-amber-400"></i>
                <span>(01) 339-6215 &bull; (01) 301-7765</span>
              </p>
              <p class="text-xs text-slate-400 flex items-center gap-2">
                <i class="fas fa-envelope text-amber-400"></i>
                <span>mesadepartes@dmc.edu.pe</span>
              </p>
              <div class="pt-3">
                <a href="https://wa.me/51987654321?text=Hola,%20deseo%20información%20de%20la%20I.E.%20Dionisio%20Manco%20Campos" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 btn-whatsapp text-white font-bold px-4 py-2 rounded-xl text-xs">
                  <i class="fab fa-whatsapp text-base"></i> WhatsApp de Atención
                </a>
              </div>
            </div>

          </div>

          <!-- Sub-footer copyright -->
          <div class="pt-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-xs text-slate-400">
            <p>&copy; 1962 - 2026 <strong>I.E. Dionisio Manco Campos</strong>. Todos los derechos reservados.</p>
            <p class="flex items-center gap-4">
              <a href="${root}pages/institutional/management/ri" class="hover:text-amber-400">Reglamento Interno</a>
              <span>&bull;</span>
              <a href="${root}pages/services/procedures/libro-reclamaciones" class="hover:text-amber-400">Libro de Reclamaciones</a>
              <span>&bull;</span>
              <a href="${root}pages/services/procedures/tupa" class="hover:text-amber-400">TUPA</a>
            </p>
          </div>
        </div>
      </footer>

      <!-- Botón flotante para volver arriba -->
      <button id="btn-scroll-top" class="fixed bottom-6 right-6 z-40 btn-scroll-top text-white w-12 h-12 rounded-full flex items-center justify-center text-lg opacity-0 pointer-events-none transition-all duration-300 shadow-xl" aria-label="Volver arriba">
        <i class="fas fa-arrow-up"></i>
      </button>
    `;
  }
}
customElements.define('dmc-footer', DmcFooter);
