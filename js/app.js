/**
 * Portal Institucional - I.E. Dionisio Manco Campos (Mala - Cañete)
 * Script principal de interactividad, navegación y utilidades
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Drawer Toggle
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

  // 2. Sticky Navbar Glass Effect on Scroll
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

  // 3. Scroll to Top Button Action
  const scrollTopBtn = document.getElementById('btn-scroll-top');
  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 4. FAQ Accordion Toggle
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item) => {
    const trigger = item.querySelector('.faq-trigger');
    const content = item.querySelector('.faq-content');
    const icon = item.querySelector('.faq-icon');

    if (trigger && content) {
      trigger.addEventListener('click', () => {
        const isOpen = !content.classList.contains('hidden');
        // Close all
        document.querySelectorAll('.faq-content').forEach((c) => c.classList.add('hidden'));
        document.querySelectorAll('.faq-icon').forEach((i) => i.classList.remove('rotate-180'));

        if (!isOpen) {
          content.classList.remove('hidden');
          icon?.classList.add('rotate-180');
        }
      });
    }
  });

  // 5. Tabs Filter (Talleres & Niveles)
  const filterBtns = document.querySelectorAll('[data-filter-tab]');
  const filterItems = document.querySelectorAll('[data-filter-category]');

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const category = btn.getAttribute('data-filter-tab');
      // Update button active state
      filterBtns.forEach((b) => {
        b.classList.remove('bg-yellow-500', 'text-slate-900', 'font-bold');
        b.classList.add('bg-slate-100', 'text-slate-700');
      });
      btn.classList.add('bg-yellow-500', 'text-slate-900', 'font-bold');
      btn.classList.remove('bg-slate-100', 'text-slate-700');

      // Filter cards
      filterItems.forEach((card) => {
        if (category === 'all' || card.getAttribute('data-filter-category') === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });

  // 6. Interactive Modal Alert for Forms
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

  // 7. Form Handlers
  const admisionForm = document.getElementById('form-admision');
  if (admisionForm) {
    admisionForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nombre = admisionForm.querySelector('[name="nombre"]')?.value || 'Padre de familia';
      showFeedbackModal(
        '¡Solicitud Registrada con Éxito!',
        `Estimado(a) ${nombre}, su pre-registro para el proceso de matrícula en la I.E. Dionisio Manco Campos ha sido recibido. La secretaría pedagógica se pondrá en contacto pronto vía correo o WhatsApp.`,
        true
      );
      admisionForm.reset();
    });
  }

  const contactoForm = document.getElementById('form-contacto');
  if (contactoForm) {
    contactoForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const emisor = contactoForm.querySelector('[name="nombre"]')?.value || 'Usuario';
      showFeedbackModal(
        '¡Mesa de Partes Virtual - Trámite Ingresado!',
        `Gracias, ${emisor}. Su consulta o documento ha sido registrado en el sistema de atención de la I.E. Dionisio Manco Campos (Mala, Cañete). Código de seguimiento generado para su trámite.`,
        true
      );
      contactoForm.reset();
    });
  }

  // 8. Himno Reader / Audio Effect
  const btnToggleHimno = document.getElementById('btn-toggle-himno');
  const himnoStanzas = document.querySelectorAll('.himno-stanza');
  let himnoInterval = null;
  let isHimnoPlaying = false;

  if (btnToggleHimno && himnoStanzas.length > 0) {
    btnToggleHimno.addEventListener('click', () => {
      if (!isHimnoPlaying) {
        isHimnoPlaying = true;
        btnToggleHimno.innerHTML = '<i class="fas fa-pause mr-2 text-yellow-400"></i> Pausar Recitación';
        let currentIdx = 0;
        himnoStanzas[0].classList.add('bg-yellow-500/20', 'border-l-4', 'border-yellow-400', 'p-3', 'rounded');

        himnoInterval = setInterval(() => {
          himnoStanzas.forEach(s => s.classList.remove('bg-yellow-500/20', 'border-l-4', 'border-yellow-400', 'p-3', 'rounded'));
          currentIdx = (currentIdx + 1) % himnoStanzas.length;
          himnoStanzas[currentIdx].classList.add('bg-yellow-500/20', 'border-l-4', 'border-yellow-400', 'p-3', 'rounded');
        }, 3500);
      } else {
        isHimnoPlaying = false;
        clearInterval(himnoInterval);
        btnToggleHimno.innerHTML = '<i class="fas fa-play mr-2 text-yellow-400"></i> Iniciar Modo Lectura Musical';
        himnoStanzas.forEach(s => s.classList.remove('bg-yellow-500/20', 'border-l-4', 'border-yellow-400', 'p-3', 'rounded'));
      }
    });
  }
});
