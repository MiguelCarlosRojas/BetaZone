/**
 * Bundler / Loader Universal de Componentes Web
 * Centraliza e incluye los componentes modulares de la carpeta /components
 * para garantizar compatibilidad directa con navegadores sin bundlers externos.
 */

// 1. Cargar Componentes de Layout
import '../components/layout/header/header.js';
import '../components/layout/footer/footer.js';

// 2. Cargar Componentes de Navegación
import '../components/navigation/breadcrumb/breadcrumb.js';
import '../components/navigation/drawer/drawer.js';

// 3. Cargar Componentes de UI
import '../components/ui/button/button.js';
import '../components/ui/card/card.js';
import '../components/ui/modal/modal.js';
