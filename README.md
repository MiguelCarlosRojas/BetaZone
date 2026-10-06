# 🏫 Portal Web Oficial | I.E. Dionisio Manco Campos (Mala - Cañete)

[![Sitio Web Oficial](https://img.shields.io/badge/Sitio%20Web-dmc--betazone.vercel.app-success?style=for-the-badge&logo=vercel)](https://dmc-betazone.vercel.app)
[![Institución Educativa](https://img.shields.io/badge/Nivel-Secundaria%20%7C%20EBR%20%26%20CEBA-navy?style=for-the-badge)](https://dmc-betazone.vercel.app)
[![UGEL](https://img.shields.io/badge/UGEL-08%20Cañete-orange?style=for-the-badge)](http://ugel08canete.gob.pe/)
[![Licencia](https://img.shields.io/badge/Licencia-Educativa%20Libre-brightgreen?style=for-the-badge)](COPYRIGHT.md)

Portal web institucional moderno, dinámico y responsivo para la **Institución Educativa Pública "Dionisio Manco Campos"**, alma máter de la educación secundaria en el distrito de Mala, provincia de Cañete, región Lima, Perú.

---

## 📌 Datos de Configuración del Repositorio en GitHub (**Edit repository details**)

Para actualizar los metadatos en la configuración principal del repositorio de GitHub:

* **Description (Menor a 350 caracteres):**  
  > Portal oficial de la I.E. Dionisio Manco Campos (Mala, Cañete). Educación secundaria y CEBA fundada en 1962 con módulos académicos, vida escolar, talleres, trámites y admisión bajo el lema "Patria, Estudio y Disciplina".
* **Website:**  
  `https://dmc-betazone.vercel.app`
* **Topics (Temas recomendados):**  
  `colegio-peru`, `educacion-secundaria`, `dionisio-manco-campos`, `ceba`, `mala-canete`, `ugel08`, `cneb`, `minedu`, `portal-educativo`, `html5`, `css3`, `tailwind-css`, `vercel`, `clean-urls`
* **Include in the home page:**  
  ☑️ **Releases**  
  ☑️ **Deployments** *(Activo y verificado en Vercel)*  
  ☑️ **Packages** *(Opcional)*  

---

## 🏛️ Sobre la Institución (Datos Reales y Verificados)

* **Nombre Oficial:** Institución Educativa Pública "Dionisio Manco Campos"
* **Lema Oficial:** *"Patria, Estudio y Disciplina"* *(en el escudo: "Estudio, Disciplina y Superación")*
* **Fundación:** 15 de abril de 1962 (Iniciada como Colegio Municipal Secundario Mixto, liderado por el alcalde maleño **Don José Huapaya Soriano** y su primer director, el educador **Eusebio Ruiz Yaya**).
* **Patrono Escolar:** Maestro **Dionisio Manco Campos** (Nacido el 8 de mayo de 1914 en Mala, destacado pedagogo egresado de la Pontificia Universidad Católica del Perú - PUCP).
* **Niveles y Modalidades:** 
  * Educación Básica Regular (Secundaria de Menores: 1° a 5° de Secundaria).
  * Educación Básica Alternativa (CEBA: Ciclos Inicial, Intermedio y Avanzado en horarios vespertino y nocturno).
* **Códigos Identificadores Oficiales (MINEDU / ESCALE):**
  * Código Modular EBR Secundaria: **0286385**
  * Código Modular CEBA: **0285676**
  * Código de Local Educativo: **353596**
  * Jurisdicción: **UGEL N° 08 - Cañete | DRE Lima Provincias**
* **Ubicación Oficial:** Jr. Enrique Swayne s/n, Distrito de Mala, Provincia de Cañete, Región Lima - Perú.
* **Central Telefónica:** (01) 339-6215 / (01) 301-7765
* **Redes Sociales Oficiales:** 
  * [Facebook Oficial IEP DMC](https://www.facebook.com/iepdmc)
  * [Facebook Oficial CEBA DMC](https://www.facebook.com/dmc19)

---

## 📂 Arquitectura Jerárquica del Ecosistema Web en Inglés (118 Páginas)

Toda la estructura de subcarpetas ha sido renombrada al inglés con URLs limpias (**clean URLs** sin `.html` visible):

```text
BetaZone/
├── index.html                                 # Portal Principal & Directorio Maestro
├── vercel.json                                # Configuración de Clean URLs para Vercel
│
├── pages/                                     # DIRECTORIO RAÍZ DE PÁGINAS Y MÓDULOS
│   ├── institutional/                         # Módulo Institucional (16 páginas)
│   │   ├── about.html                         # Reseña institucional completa
│   │   ├── history/                           # Historia, Fundación 1962 y Patrono
│   │   ├── symbols/                           # Himno, Escudo, Lema y Valores
│   │   └── management/                        # Dirección, Subdirección, PEI, PAT, RI, APAFA, CONEI
│   │
│   ├── academics/                             # Módulo Académico & Curricular (36 páginas)
│   │   ├── pedagogical-proposal.html          # Propuesta Pedagógica CNEB
│   │   ├── grades/                            # 1° a 5° de Secundaria, turnos, desempeños y evaluación
│   │   ├── curricular-areas/                  # Las 11 áreas curriculares oficiales del MINEDU
│   │   └── ceba/                              # Ciclo Inicial, Intermedio, Avanzado, turnos y docentes
│   │
│   ├── school-life/                           # Módulo de Vida Escolar (31 páginas)
│   │   ├── workshops-overview.html            # Visión general de talleres extracurriculares
│   │   ├── workshops/                         # Cómputo, Robótica, Ajedrez, Música, Danzas, Deportes
│   │   ├── students/                          # Municipio Escolar, Policía Escolar, Brigadas, Florales
│   │   └── families/                          # Escuela de Padres, APAFA, Reuniones y Rendición de cuentas
│   │
│   └── services/                              # Módulo de Servicios y Trámites (34 páginas)
│       ├── contact.html                       # Contacto institucional, mapa satelital y teléfonos
│       ├── admissions/                        # Admisión, vacantes, cronograma, requisitos, traslados
│       │   ├── index.html                     # Portal principal de admisión
│       │   └── overview.html                  # Formulario y consultas de vacantes
│       ├── infrastructure/                    # Aulas, laboratorios AIP, losas deportivas y auditorio
│       ├── procedures/                        # Mesa de partes virtual, certificados, constancias, FUT, TUPA
│       └── news/                              # Comunicados de dirección, desfiles, aniversarios, convenios
│
├── components/                                # COMPONENTES MODULARES REUTILIZABLES
│   ├── index.js                               # Registro central de Custom Elements
│   ├── layout/                                # Componentes de Maquetación y Estructura
│   │   ├── header/header.js                   # Header unificado y barra de avisos
│   │   └── footer/footer.js                   # Footer institucional con códigos, sedes y enlaces
│   ├── navigation/                            # Componentes de Navegación Interactiva
│   │   ├── breadcrumb/breadcrumb.js           # Migas de pan dinámicas y funcionales
│   │   └── drawer/drawer.js                   # Menú móvil deslizable accesible
│   └── ui/                                    # Componentes de Interfaz de Usuario
│       ├── button/button.js                   # Botón institucional con variantes (gold/navy/outline)
│       ├── card/card.js                       # Tarjetas de contenido (glass, dark, stat)
│       └── modal/modal.js                     # Ventana modal de feedback y trámites
│
├── styles/
│   └── colegio.css                            # Sistema de diseño full-width con Plus Jakarta Sans y Outfit
├── js/
│   ├── components.js                          # Loader modular para componentes
│   └── app.js                                 # Buscador, filtros de talleres, modal interactivo y drawer
└── img/
    ├── escudo-dmc.svg                         # Escudo vectorial oficial
    ├── logo-dmc-horizontal.svg                # Logo horizontal institucional
    └── favicon.svg                            # Favicon vectorial oficial
```

---

## 🚀 Despliegue en Vercel (Producción Activa)

El portal está optimizado y desplegado en producción:
- **URL Oficial Única:** [https://dmc-betazone.vercel.app](https://dmc-betazone.vercel.app)

---

## 📜 Licencia y Normas Comunitarias
- Consultar [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) para pautas de convivencia digital escolar.
- Consultar [COPYRIGHT.md](COPYRIGHT.md) para avisos legales y propiedad intelectual.
