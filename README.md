# 🏫 Portal Web Oficial | I.E. Dionisio Manco Campos (Mala - Cañete)

[![Sitio Web Oficial](https://img.shields.io/badge/Sitio%20Web-dmc--betazone.vercel.app-success?style=for-the-badge&logo=vercel)](https://dmc-betazone.vercel.app)
[![Institución Educativa](https://img.shields.io/badge/Nivel-Secundaria%20%7C%20EBR%20%26%20CEBA-navy?style=for-the-badge)](https://dmc-betazone.vercel.app)
[![UGEL](https://img.shields.io/badge/UGEL-08%20Cañete-orange?style=for-the-badge)](http://ugel08canete.gob.pe/)
[![Rama Principal](https://img.shields.io/badge/Branch-main-blue?style=for-the-badge&logo=git)](https://github.com/MiguelCarlosRojas/BetaZone/tree/main)
[![Licencia](https://img.shields.io/badge/Licencia-Educativa%20Libre-brightgreen?style=for-the-badge)](COPYRIGHT.md)

Portal web institucional moderno, dinámico y responsivo para la **Institución Educativa Pública "Dionisio Manco Campos"**, alma máter de la educación secundaria en el distrito de Mala, provincia de Cañete, región Lima, Perú.

---

## 📌 Datos de Configuración del Repositorio en GitHub (**Edit repository details**)

Metadatos sincronizados en la configuración oficial del repositorio en GitHub:

* **Description (Menor a 350 caracteres):**  
  > Portal Web Oficial de la I.E. Dionisio Manco Campos (Mala, Cañete). Educación secundaria y CEBA fundada en 1962 bajo el lema 'Patria, Estudio y Disciplina'. Sistema modular SPA, vida escolar, talleres, trámites y admisión.
* **Website:**  
  `https://dmc-betazone.vercel.app`
* **Topics (Temas oficiales configurados):**  
  `colegio-peru`, `educacion-secundaria`, `dionisio-manco-campos`, `ceba`, `mala-canete`, `ugel08`, `cneb`, `minedu`, `portal-educativo`, `tailwind-css`, `web-components`, `vercel`, `single-page-application`
* **Include in the home page:**  
  ☑️ **Releases**  
  ☑️ **Deployments** *(Activo y verificado en Vercel)*  
  ☑️ **Packages** *(Opcional)*  

---

## 🏛️ Sobre la Institución (Datos Reales y Verificados)

* **Nombre Oficial:** Institución Educativa Pública "Dionisio Manco Campos"
* **Lemas Oficiales:**  
  * *"Patria, Estudio y Disciplina"* (Lema Institucional Cívico)  
  * *"Estudio, Disciplina y Superación"* (Lema en el Escudo DMC)
* **Fundación Histórica:** **15 de abril de 1962**. Nació formalmente como *Colegio Municipal Secundario Mixto de Mala* por acuerdo unánime liderado por el alcalde distrital **Don José Huapaya Soriano**, iniciando labores con más de 600 estudiantes bajo la conducción de su primer director, el **Prof. Eusebio Ruiz Yaya**.
* **Patrono Escolar:** Maestro **Dionisio Manco Campos** (Nacido en Mala el 8 de mayo de 1914, exalumno guadalupano y destacado pedagogo egresado de la Facultad de Educación de la PUCP en 1942).
* **Niveles y Modalidades Educativas:** 
  * **Educación Básica Regular (EBR):** Nivel Secundaria de Menores (1° a 5° de Secundaria, turnos mañana y tarde).
  * **Educación Básica Alternativa (CEBA):** Ciclos Inicial, Intermedio y Avanzado para jóvenes y adultos (turnos vespertino y nocturno).
* **Códigos Identificadores Oficiales (MINEDU / ESCALE):**
  * Código Modular EBR Secundaria: **0286385**
  * Código Modular CEBA: **0285676**
  * Código de Local Educativo: **353596**
  * Jurisdicción Educativa: **UGEL N° 08 - Cañete | DRE Lima Provincias**
* **Sede Central:** Jr. Enrique Swayne s/n, Distrito de Mala, Provincia de Cañete, Región Lima - Perú.
* **Centrales Telefónicas:** (01) 339-6215 / (01) 301-7765
* **Mesa de Partes Virtual:** [https://dmc-betazone.vercel.app/pages/services/contact#mesa-de-partes](https://dmc-betazone.vercel.app/pages/services/contact#mesa-de-partes)
* **Canales Oficiales:**
  * [Facebook Oficial IEP DMC](https://www.facebook.com/iepdmc)
  * [Facebook Oficial CEBA DMC](https://www.facebook.com/dmc19)

---

## 📂 Arquitectura Jerárquica del Proyecto (`src/`)

Todo el código fuente y recursos del portal residen ordenadamente dentro de `src/`, comunicados mediante el enrutador SPA nativo y URLs limpias:

```text
BetaZone/
├── index.html                                 # Punto de entrada raíz (Home)
├── vercel.json                                # Configuración de Clean URLs y Rewrites a /src
├── README.md                                  # Documentación institucional técnica
├── CODE_OF_CONDUCT.md                         # Código de conducta y convivencia escolar
├── COPYRIGHT.md                               # Propiedad intelectual y licencia DL 822
│
└── src/                                       # CÓDIGO FUENTE CENTRALIZADO
    ├── components/                            # Ecosistema de Web Components reutilizables
    │   ├── index.js                           # Registro central de Custom Elements
    │   ├── layout/                            # Componentes estructurales
    │   │   ├── header/header.js               # <dmc-header>: Encabezado sticky y barra informativa
    │   │   └── footer/footer.js               # <dmc-footer>: Footer institucional unificado
    │   ├── navigation/                        # Componentes de navegación
    │   │   ├── breadcrumb/breadcrumb.js       # <dmc-breadcrumb>: Migas de pan interactivas y dinámicas
    │   │   └── drawer/drawer.js               # <dmc-drawer>: Menú deslizable para dispositivos móviles
    │   └── ui/                                # Componentes de interfaz de usuario
    │       ├── button/button.js               # <dmc-button>: Botones institucionales (gold, navy, outline)
    │       ├── card/card.js                   # <dmc-card>: Tarjetas modulares de contenido
    │       └── modal/modal.js                 # <dmc-modal>: Ventana modal interactiva de confirmación
    │
    ├── pages/                                 # 117 módulos HTML estructurados en inglés
    │   ├── institutional/                     # about.html, history/, symbols/, management/
    │   ├── academics/                         # pedagogical-proposal.html, grades/, curricular-areas/, ceba/
    │   ├── school-life/                       # workshops-overview.html, workshops/, students/, families/
    │   └── services/                          # contact.html, admissions/, infrastructure/, procedures/, news/
    │
    ├── styles/
    │   └── colegio.css                        # Sistema responsive universal (320px a 4K) y diseño full-width
    ├── js/
    │   ├── components.js                      # Loader universal de componentes
    │   └── app.js                             # Router SPA nativo (sin recarga) e interactividad
    └── img/
        ├── escudo-dmc.svg                     # Escudo heráldico oficial
        ├── logo-dmc-horizontal.svg            # Isotipo y logotipo institucional
        └── favicon.svg                        # Favicon vectorial oficial
```

---

## 🚀 Despliegue en Vercel (Producción Activa)

- **URL Oficial Única:** [https://dmc-betazone.vercel.app](https://dmc-betazone.vercel.app)
- **Deployment Status:** `READY` (200 OK)
- **Rama Oficial de Despliegue:** `main`

---

## 📜 Normas Comunitarias y Propiedad Intelectual
- Ver [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) para pautas de convivencia digital escolar bajo la Ley N° 29719.
- Ver [COPYRIGHT.md](COPYRIGHT.md) para derechos protegidos bajo el D.L. 822 de la República del Perú.
