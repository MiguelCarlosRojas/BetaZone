/**
 * Portal Institucional - I.E. Dionisio Manco Campos (Mala - Cañete)
 * Script principal de interactividad, navegación SPA y utilidades
 */

// 1. Router SPA Nativo para navegación fluida instantánea sin recargar la página entera
(function initSPARouter() {
  // Solo interceptar enlaces internos relativos o del mismo host
  document.addEventListener('click', async (e) => {
    const link = e.target.closest('a');
    if (!link) return;

    const href = link.getAttribute('href');
    if (!href) return;

    // Ignorar anclas solas, enlaces externos, protocolos tel/mailto/wa
    if (href.startsWith('#') || href.startsWith('tel:') || href.startsWith('mailto:') || href.startsWith('javascript:')) return;
    if (link.target === '_blank' || link.hasAttribute('download')) return;

    // Verificar si es un enlace interno del sitio
    let targetUrl;
    try {
      targetUrl = new URL(href, window.location.href);
    } catch {
      return;
    }

    if (targetUrl.origin !== window.location.origin) return;

    // Evitar interceptar si es un hash dentro de la misma ruta actual
    if (targetUrl.pathname === window.location.pathname && targetUrl.hash) {
      return; // permitir scroll nativo a ancla
    }

    // Interceptar navegación
    e.preventDefault();
    await navigateTo(targetUrl.href);
  });

  // Manejar botones adelante / atrás del navegador
  window.addEventListener('popstate', async () => {
    await loadContent(window.location.href, false);
  });
})();

async function navigateTo(url) {
  // Transición visual sutil
  document.body.classList.add('opacity-90');
  const success = await loadContent(url, true);
  document.body.classList.remove('opacity-90');
  if (success) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else {
    // Si falla el fetch asíncrono, fallback a recarga nativa
    window.location.href = url;
  }
}

async function loadContent(url, push = true) {
  try {
    const response = await fetch(url);
    if (!response.ok) return false;

    const htmlText = await response.text();
    const parser = new DOMParser();
    const newDoc = parser.parseFromString(htmlText, 'text/html');

    // Actualizar título
    document.title = newDoc.title;

    // Actualizar breadcrumb si existe
    const currentBreadcrumb = document.querySelector('dmc-breadcrumb');
    const newBreadcrumb = newDoc.querySelector('dmc-breadcrumb');
    if (currentBreadcrumb && newBreadcrumb) {
      currentBreadcrumb.replaceWith(newBreadcrumb);
    }

    // Actualizar main o contenedor principal de contenido
    const currentMain = document.querySelector('main');
    const newMain = newDoc.querySelector('main');
    if (currentMain && newMain) {
      currentMain.innerHTML = newMain.innerHTML;
    } else {
      return false; // si las estructuras difieren sustancialmente
    }

    // Actualizar banner hero si existe en la subpágina
    const currentHero = document.querySelector('.hero-subpage, .hero-gradient');
    const newHero = newDoc.querySelector('.hero-subpage, .hero-gradient');
    if (currentHero && newHero) {
      currentHero.replaceWith(newHero);
    }

    // Actualizar estado en History API
    if (push) {
      window.history.pushState({}, '', url);
    }

    // Actualizar clase activa en enlaces de navegación
    updateActiveNavLinks(window.location.pathname);

    // Reinicializar interactividad para el nuevo contenido inyectado
    initDynamicFeatures();

    return true;
  } catch (err) {
    console.warn('SPA Navigation fallback:', err);
    return false;
  }
}

function updateActiveNavLinks(pathname) {
  document.querySelectorAll('.nav-link').forEach((link) => {
    const href = link.getAttribute('href');
    if (!href) return;
    try {
      const linkUrl = new URL(href, window.location.href);
      if (linkUrl.pathname === pathname || (pathname === '/' && href.includes('index'))) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    } catch {}
  });
}

function initDynamicFeatures() {
  // FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item) => {
    const trigger = item.querySelector('.faq-trigger');
    const content = item.querySelector('.faq-content');
    const icon = item.querySelector('.faq-icon');

    if (trigger && content) {
      // Remover listener viejo clonando
      const newTrigger = trigger.cloneNode(true);
      trigger.parentNode.replaceChild(newTrigger, trigger);

      newTrigger.addEventListener('click', () => {
        const isOpen = !content.classList.contains('hidden');
        document.querySelectorAll('.faq-content').forEach((c) => c.classList.add('hidden'));
        document.querySelectorAll('.faq-icon').forEach((i) => i.classList.remove('rotate-180'));

        if (!isOpen) {
          content.classList.remove('hidden');
          icon?.classList.add('rotate-180');
        }
      });
    }
  });

  // Filtros de Talleres
  const filterBtns = document.querySelectorAll('[data-filter-tab]');
  const filterItems = document.querySelectorAll('[data-filter-category]');

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const category = btn.getAttribute('data-filter-tab');
      filterBtns.forEach((b) => {
        b.classList.remove('bg-yellow-500', 'text-slate-900', 'font-bold');
        b.classList.add('bg-slate-100', 'text-slate-700');
      });
      btn.classList.add('bg-yellow-500', 'text-slate-900', 'font-bold');
      btn.classList.remove('bg-slate-100', 'text-slate-700');

      filterItems.forEach((card) => {
        if (category === 'all' || card.getAttribute('data-filter-category') === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });

  // Formulario Admisión
  const admisionForm = document.getElementById('form-admision');
  if (admisionForm) {
    admisionForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nombre = admisionForm.querySelector('[name="nombre"]')?.value || 'Padre de familia';
      window.showFeedbackModal(
        '¡Solicitud Registrada con Éxito!',
        `Estimado(a) ${nombre}, su pre-registro para el proceso de matrícula en la I.E. Dionisio Manco Campos ha sido recibido. La secretaría pedagógica se pondrá en contacto pronto vía correo o WhatsApp.`,
        true
      );
      admisionForm.reset();
    });
  }

  // Formulario Contacto
  const contactoForm = document.getElementById('form-contacto');
  if (contactoForm) {
    contactoForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const emisor = contactoForm.querySelector('[name="nombre"]')?.value || 'Usuario';
      window.showFeedbackModal(
        '¡Mesa de Partes Virtual - Trámite Ingresado!',
        `Gracias, ${emisor}. Su consulta o documento ha sido registrado en el sistema de atención de la I.E. Dionisio Manco Campos (Mala, Cañete). Código de seguimiento generado para su trámite.`,
        true
      );
      contactoForm.reset();
    });
  }
}

// 2. Inicialización de interfaz y eventos globales
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Drawer Toggle
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenuClose = document.getElementById('mobile-menu-close');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileBackdrop = document.getElementById('mobile-backdrop');

  function openMobileMenu() {
    if (mobileMenu && mobileBackdrop) {
      mobileMenu.classList.remove('translate-x-full');
      mobileBackdrop.classList.remove('hidden');
      document.body.classList.add('overflow-hidden');
    }
  }

  function closeMobileMenu() {
    if (mobileMenu && mobileBackdrop) {
      mobileMenu.classList.add('translate-x-full');
      mobileBackdrop.classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
    }
  }

  if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMobileMenu);
  if (mobileMenuClose) mobileMenuClose.addEventListener('click', closeMobileMenu);
  if (mobileBackdrop) mobileBackdrop.addEventListener('click', closeMobileMenu);

  // Cerrar el drawer al hacer click en cualquier enlace interno dentro de él
  document.addEventListener('click', (e) => {
    if (e.target.closest('#mobile-menu a')) {
      closeMobileMenu();
    }
  });

  // Sticky Navbar Glass Effect on Scroll
  const mainHeader = document.getElementById('main-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      mainHeader?.classList.add('shadow-xl', 'py-2');
      mainHeader?.classList.remove('py-4');
    } else {
      mainHeader?.classList.remove('shadow-xl', 'py-2');
      mainHeader?.classList.add('py-4');
    }

    // Scroll to Top Button Visibility
    const scrollTopBtn = document.getElementById('btn-scroll-top');
    if (scrollTopBtn) {
      if (window.scrollY > 400) {
        scrollTopBtn.classList.remove('opacity-0', 'pointer-events-none');
        scrollTopBtn.classList.add('opacity-100', 'pointer-events-auto');
      } else {
        scrollTopBtn.classList.remove('opacity-100', 'pointer-events-auto');
        scrollTopBtn.classList.add('opacity-0', 'pointer-events-none');
      }
    }
  });

  // Scroll to Top Button Action (delegado)
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('#btn-scroll-top');
    if (btn) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  });

  // Modales de Feedback
  window.showFeedbackModal = function(title, message, isSuccess = true) {
    const modal = document.getElementById('feedback-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalMessage = document.getElementById('modal-message');
    const modalIcon = document.getElementById('modal-icon');

    if (modal && modalTitle && modalMessage && modalIcon) {
      modalTitle.textContent = title;
      modalMessage.textContent = message;
      if (isSuccess) {
        modalIcon.className = 'fas fa-check-circle text-5xl text-emerald-500 mb-4 animate-bounce';
      } else {
        modalIcon.className = 'fas fa-exclamation-circle text-5xl text-red-500 mb-4 animate-pulse';
      }
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    } else {
      alert(`${title}: ${message}`);
    }
  };

  window.closeFeedbackModal = function() {
    const modal = document.getElementById('feedback-modal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
  };

  // Inicializar dinámicas
  initDynamicFeatures();
});
