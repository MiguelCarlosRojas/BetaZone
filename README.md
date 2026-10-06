# 🏫 Portal Web Oficial | I.E. Dionisio Manco Campos (Mala - Cañete)

[![Sitio Web Oficial](https://img.shields.io/badge/Sitio%20Web-Online-success?style=for-the-badge&logo=vercel)](https://landing-page-beta-chi.vercel.app)
[![Institución Educativa](https://img.shields.io/badge/Nivel-Secundaria%20%7C%20EBR%20%26%20CEBA-blue?style=for-the-badge)](https://landing-page-beta-chi.vercel.app)
[![UGEL](https://img.shields.io/badge/UGEL-08%20Cañete-orange?style=for-the-badge)](http://ugel08canete.gob.pe/)
[![Licencia](https://img.shields.io/badge/Licencia-Educativa%20Libre-brightgreen?style=for-the-badge)](COPYRIGHT.md)

Portal web institucional moderno, dinámico y responsivo para la **Institución Educativa Pública "Dionisio Manco Campos"**, alma máter de la educación secundaria en el distrito de Mala, provincia de Cañete, región Lima, Perú.

---

## 📌 Datos de la Configuración del Repositorio en GitHub (**Edit repository details**)

Para configurar la cabecera de este repositorio en GitHub:

* **Description (Menor a 350 caracteres):**  
  > Portal web oficial de la I.E. Dionisio Manco Campos (Mala, Cañete). Alma máter de la educación secundaria con más de 60 años de excelencia pedagógica bajo el lema "Patria, Estudio y Disciplina". Información institucional, propuesta pedagógica, admisión y mesa de partes.
* **Website:**  
  `https://landing-page-beta-chi.vercel.app`
* **Topics (Temas a añadir):**  
  `colegio-secundaria`, `dionisio-manco-campos`, `mala-canete`, `educacion-peru`, `landing-page`, `html5`, `tailwind-css`, `ugel-08`, `portal-escolar`, `responsive-web-design`
* **Include in the home page:**  
  ☑️ **Releases**  
  ☑️ **Deployments**  
  ☑️ **Packages**  

---

## 🏛️ Sobre la Institución (Datos Reales y Verificados)

* **Nombre Oficial:** Institución Educativa Pública "Dionisio Manco Campos"
* **Lema Oficial:** *"Patria, Estudio y Disciplina"*
* **Fundación:** 15 de abril de 1962 (Creada como Colegio Municipal Secundario Mixto, bajo el liderazgo del alcalde **Don José Huapaya Soriano** y dirigida inicialmente por el **Prof. Eusebio Ruiz Yaya**).
* **Patrono Escolar:** Maestro **Dionisio Manco Campos** (Nacido el 8 de mayo de 1914 en Mala, educador egresado de la Pontificia Universidad Católica del Perú - PUCP).
* **Niveles de Atención:** Educación Básica Regular (Secundaria de Menores) y CEBA (Educación Básica Alternativa para jóvenes y adultos).
* **Códigos Identificadores:**
  * Código Modular EBR Secundaria: **0286385**
  * Código Modular CEBA: **0285676**
  * Código de Local Educativo: **353596**
  * Jurisdicción: **UGEL N° 08 - Cañete | DRE Lima Provincias**
* **Ubicación Oficial:** Jr. Enrique Swayne s/n, Distrito de Mala, Provincia de Cañete, Región Lima - Perú.
* **Central Telefónica:** (01) 339-6215 / (01) 301-7765
* **Redes:** [facebook.com/iepdmc](https://www.facebook.com/iepdmc) &bull; CEBA: [facebook.com/dmc19](https://www.facebook.com/dmc19)

---

## 📂 Arquitectura Jerárquica del Ecosistema Web (118 Páginas)

Toda la estructura de páginas está organizada bajo la carpeta principal `paginas/` en subcarpetas y sub-subcarpetas temáticas:

```text
BetaZone/
├── index.html                                 # Gran Portal Principal & Directorio
├── nosotros.html                              # Portada Institucional
├── propuesta-pedagogica.html                  # Portada Curricular
├── talleres.html                              # Portada de Talleres
├── admision.html                              # Portada de Admisión
├── contacto.html                              # Portada de Contacto & Mesa de Partes
│
├── paginas/                                   # CARPETA PRINCIPAL DE PÁGINAS
│   │
│   ├── institucional/                         # [SUBCARPETA 1] Identidad y Gestión
│   │   ├── historia/                          # index.html, fundadores.html, biografia-patrono.html
│   │   ├── simbolos/                          # index.html, escudo.html, himno.html, valores.html
│   │   └── gestion/                           # index.html, direccion.html, subdireccion.html,
│   │                                          # organigrama.html, mision-vision.html, pei.html,
│   │                                          # pat.html, ri.html, pci.html
│   │
│   ├── academico/                             # [SUBCARPETA 2] Secundaria y CEBA
│   │   ├── grados/                            # index.html, primer-grado.html, 1°-secciones.html,
│   │   │                                      # segundo-grado.html, 2°-secciones.html, tercer-grado.html,
│   │   │                                      # 3°-secciones.html, cuarto-grado.html, 4°-secciones.html,
│   │   │                                      # quinto-grado.html, 5°-secciones.html, cuadro-merito.html,
│   │   │                                      # evaluacion.html, horarios-turnos.html, normas-aula.html
│   │   ├── areas-curriculares/                # index.html, matematica.html, comunicacion.html,
│   │   │                                      # ciencia-tecnologia.html, ciencias-sociales.html,
│   │   │                                      # dpcc.html, ingles.html, arte-cultura.html,
│   │   │                                      # educacion-fisica.html, EPT.html, religion.html, tutoria.html
│   │   └── ceba/                              # index.html, ciclo-inicial.html, ciclo-intermedio.html,
│   │                                          # ciclo-avanzado.html, matricula-ceba.html,
│   │                                          # horarios-ceba.html, docentes-ceba.html, certificacion.html
│   │
│   ├── vida-escolar/                          # [SUBCARPETA 3] Talleres, Alumnos y Familias
│   │   ├── talleres/                          # index.html, banda-guerra.html, banda-musica.html,
│   │   │                                      # club-ciencias-eureka.html, robotica-computo.html,
│   │   │                                      # danzas-folclor.html, futbol.html, voleibol.html,
│   │   │                                      # atletismo.html, ajedrez.html, teatro-oratoria.html,
│   │   │                                      # medio-ambiente.html
│   │   ├── estudiantes/                       # index.html, municipio-escolar.html, policia-escolar.html,
│   │   │                                      # brigada-defensa-civil.html, brigada-ecologica.html,
│   │   │                                      # defensoria-escolar.html, juegos-florales.html,
│   │   │                                      # jedpa.html, aniversario.html, periodico-mural.html
│   │   └── familias/                          # index.html, directiva-apafa.html, escuela-padres.html,
│   │                                          # comites-aula.html, reuniones-entrevistas.html,
│   │                                          # convivencia-familiar.html, comunicados-apafa.html,
│   │                                          # rendicion-cuentas.html
│   │
│   └── servicios/                             # [SUBCARPETA 4] Admisión, Trámites y Noticias
│       ├── infraestructura/                   # index.html, aulas-ordinarias.html, aip-computo.html,
│       │                                      # laboratorios-ciencias.html, biblioteca.html,
│       │                                      # losas-deportivas.html, auditorio-civico.html,
│       │                                      # reconstruccion-gestion.html
│       ├── admision/                          # index.html, cronograma.html, requisitos.html,
│       │                                      # vacantes.html, traslados.html, siagie.html,
│       │                                      # preguntas-frecuentes.html, formulario-prematricula.html
│       ├── tramites/                          # index.html, mesa-de-partes.html, certificados-estudio.html,
│       │                                      # constancias-matricula.html, rectificacion-datos.html,
│       │                                      # horarios-atencion.html, tupa.html, libro-reclamaciones.html
│       └── noticias/                          # index.html, calendario-civico.html, comunicados.html,
│                                              # galeria-aniversario.html, galeria-desfiles.html,
│                                              # convenios-alianzas.html, exalumnos.html
│
├── img/                                       # IMÁGENES VECTORIALES OFICIALES
│   ├── escudo-dmc.svg                         # Escudo heráldico oficial
│   ├── favicon.svg                            # Icono de navegador oficial
│   └── logo-dmc-horizontal.svg                # Logo horizontal institucional
├── styles/                                    # ESTILOS
│   └── colegio.css                            # CSS profesional responsivo
└── js/                                        # SCRIPTS
    └── app.js                                 # Interacciones, menú móvil y formularios
```

---

## 🎨 Identidad Visual Oficial

* **Escudo Oficial Vectorial:** Diseñado conforme a la heráldica tradicional con la antorcha olímpica del saber, el libro abierto de las ciencias, las tres estrellas doradas, laureles de victoria y el lema institucional.
* **Colores Oficiales:** Azul Marino Imperial (`#0f2942`), Oro Heroico (`#eab308`) y Rojo Patrio (`#dc2626`).

---

## 🚀 Despliegue en Vercel

El proyecto está configurado para despliegue estático continuo mediante Vercel CLI o Git Integration:

```bash
npx vercel --prod
```

URL de producción: [https://landing-page-beta-chi.vercel.app](https://landing-page-beta-chi.vercel.app)
