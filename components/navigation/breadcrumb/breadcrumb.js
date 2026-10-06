/**
 * Componente: dmc-breadcrumb
 * Ubicación: components/navigation/breadcrumb/breadcrumb.js
 * Descripción: Migas de pan interactivas y navegables reutilizables
 */

class DmcBreadcrumb extends HTMLElement {
  connectedCallback() {
    const root = this.getAttribute('root-prefix') || './';
    const current = this.getAttribute('current') || document.title.split('|')[0].trim();
    const section = this.getAttribute('section') || '';
    const category = this.getAttribute('category') || '';

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
      <div class="bg-white border-b border-slate-200 py-3 px-4 sm:px-8 text-xs text-slate-500 font-medium w-full">
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

if (!customElements.get('dmc-breadcrumb')) {
  customElements.define('dmc-breadcrumb', DmcBreadcrumb);
}
