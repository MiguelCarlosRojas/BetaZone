#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Ecosistema Web Institucional (112 páginas .html)
I.E. Dionisio Manco Campos - Mala, Cañete (UGEL N° 08)
"""

import os
import json

BASE_DIR = r"C:\Users\isaki\Videos\Visual Studio Code\BetaZone"

# Definición de las 12 carpetas y 112 páginas con contenido real, verificado y especializado
pages_data = [
    # 1. INSTITUCIONAL (15 páginas)
    {
        "path": "institucional/index.html",
        "title": "Portal Institucional y Presentación",
        "category": "Institucional",
        "desc": "Conoce los fundamentos históricos, normativos y directivos de la I.E. Dionisio Manco Campos de Mala, Cañete.",
        "icon": "fa-landmark",
        "content": """
        <h3>Identidad y Mística de la I.E. Dionisio Manco Campos</h3>
        <p>La <strong>Institución Educativa Pública Dionisio Manco Campos</strong>, alma máter de la educación secundaria en el distrito de Mala, provincia de Cañete, región Lima Provincias, fue fundada el <strong>15 de abril de 1962</strong> para brindar oportunidades educativas reales y de excelencia a la juventud maleña y de los anexos del valle.</p>
        <p>Bajo la jurisdicción de la <strong>UGEL N° 08 de Cañete</strong> y con Código Modular de Secundaria <strong>0286385</strong> y Código de Local <strong>353596</strong>, el colegio forma a más de 1,200 estudiantes en Educación Básica Regular (Secundaria) y Educación Básica Alternativa (CEBA).</p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
            <div class="bg-blue-50 p-4 rounded-xl border border-blue-200">
                <h4 class="font-bold text-dmcNavy-900 text-sm">Reseña Histórica</h4>
                <p class="text-xs text-slate-600 mt-1">Más de seis décadas forjando profesionales que transforman Mala y el Perú.</p>
                <a href="historia.html" class="text-xs font-bold text-blue-600 mt-2 inline-block">Leer más &rarr;</a>
            </div>
            <div class="bg-yellow-50 p-4 rounded-xl border border-yellow-200">
                <h4 class="font-bold text-dmcNavy-900 text-sm">Nuestro Patrono</h4>
                <p class="text-xs text-slate-600 mt-1">El ilustre maestro maleño Don Dionisio Manco Campos (1914 - 1980).</p>
                <a href="biografia-patrono.html" class="text-xs font-bold text-yellow-700 mt-2 inline-block">Conocer semblanza &rarr;</a>
            </div>
            <div class="bg-emerald-50 p-4 rounded-xl border border-emerald-200">
                <h4 class="font-bold text-dmcNavy-900 text-sm">Símbolos e Himno</h4>
                <p class="text-xs text-slate-600 mt-1">Escudo con la antorcha del saber, lema 'Patria, Estudio y Disciplina'.</p>
                <a href="escudo-simbolos.html" class="text-xs font-bold text-emerald-700 mt-2 inline-block">Ver símbolos &rarr;</a>
            </div>
        </div>
        <h4>Documentos de Gestión Institucional</h4>
        <p>Nuestra institución orienta su labor en estricto cumplimiento de las directivas del MINEDU a través del Proyecto Educativo Institucional (PEI), el Plan Anual de Trabajo (PAT) y el Reglamento Interno (RI).</p>
        """
    },
    {
        "path": "institucional/historia.html",
        "title": "Historia de la I.E. Dionisio Manco Campos",
        "category": "Institucional",
        "desc": "La gesta histórica del 15 de abril de 1962: desde el Colegio Municipal Secundario Mixto hasta la actualidad.",
        "icon": "fa-history",
        "content": """
        <h3>La Creación del Primer Colegio Secundario de Mala</h3>
        <p>A principios de la década de los sesenta, culminar los estudios de instrucción primaria significaba para la inmensa mayoría de familias de Mala un obstáculo casi insalvable: sus hijos debían migrar a la capital provincial de San Vicente de Cañete o a Lima si deseaban continuar la educación secundaria.</p>
        <p>Sensible ante este reclamo popular, el recordado alcalde de Mala, <strong>Don José Huapaya Soriano</strong>, promovió con determinación ciudadana la fundación del primer centro secundario del valle. El <strong>15 de abril de 1962</strong>, por acuerdo unánime del concejo edilicio, nace el <em>Colegio Municipal Secundario Mixto de Mala</em>.</p>
        <h4>Primera Etapa en el Local Municipal</h4>
        <p>La institución inició sus labores en los ambientes del propio Consejo Distrital de Mala con una matrícula histórica de <strong>642 alumnos</strong>, divididos en secciones mixtas. Su primer director designado fue el destacado pedagogo <strong>Prof. Eusebio Ruiz Yaya</strong>, quien organizó la plana docente y estructuró las primeras actividades cívicas y pedagógicas.</p>
        <h4>Adquisición del Terreno en San Pedro de Mala</h4>
        <p>Ante el masivo crecimiento de la población escolar, un comité de vecinos, autoridades y padres de familia logró la adquisición de los terrenos ubicados en el sector San Pedro de Mala (Jr. Enrique Swayne s/n), donde con faenas comunales y aportes del Estado se construyeron los primeros pabellones de aulas, laboratorios y el patio cívico.</p>
        <h4>Reconocimiento Oficial como Alma Máter</h4>
        <p>Con el paso de las décadas, la institución adoptó con orgullo el nombre de <strong>Dionisio Manco Campos</strong> en homenaje al maestro maleño, convirtiéndose en el epicentro educativo y cívico indiscutible de toda la cuenca del río Mala.</p>
        """
    },
    {
        "path": "institucional/biografia-patrono.html",
        "title": "Biografía de Don Dionisio Manco Campos",
        "category": "Institucional",
        "desc": "Semblanza del insigne educador maleño Dionisio Manco Campos (1914), modelo de vocación magisterial.",
        "icon": "fa-user-graduate",
        "content": """
        <h3>Don Dionisio Manco Campos: Ejemplo de Vocación Docente</h3>
        <p>El maestro <strong>Dionisio Manco Campos</strong> nació en el tradicional distrito de Mala el <strong>8 de mayo de 1914</strong>. Fue fruto del respetable hogar constituido por Don <em>Eusebio Manco Huapaya</em> y Doña <em>Adelaida Campos de Manco</em>, quienes le inculcaron desde su tierna infancia un acendrado amor a los libros y el deber con su prójimo.</p>
        <h4>Formación Académica de Excelencia</h4>
        <p>Realizó sus primeros estudios escolares en las escuelas de Mala, demostrando notable aptitud para las letras y la historia. Trasladado a Lima para sus estudios secundarios, ingresó al glorioso <strong>Colegio Nacional Nuestra Señora de Guadalupe</strong>, claustro donde templó su disciplina ciudadana.</p>
        <p>Con firme vocación por la enseñanza, ingresó a la prestigiosa <strong>Facultad de Educación de la Pontificia Universidad Católica del Perú (PUCP)</strong>, graduándose como profesor en el año <strong>1942</strong> con las más altas calificaciones.</p>
        <h4>Trayectoria Magisterial en el Perú</h4>
        <p>El Prof. Dionisio Manco Campos no dudó en ejercer el magisterio en los rincones más alejados del territorio patrio. Desempeñó una ejemplar labor docente en el Colegio Nacional "José Gálvez" de Cajabamba y posteriormente en el Colegio "Toribio Casanova" de Cutervo, donde se ganó el afecto y la gratitud de generaciones de peruanos por su generosidad y desprendimiento.</p>
        <p>Falleció dejando como legado supremo la convicción de que solo la educación libera al ser humano. Por ello, Mala inmortalizó su memoria bautizando con su nombre al colegio secundario del distrito.</p>
        """
    },
    {
        "path": "institucional/fundadores.html",
        "title": "Fundadores y Gestores de la Creación",
        "category": "Institucional",
        "desc": "Reconocimiento a Don José Huapaya Soriano, Prof. Eusebio Ruiz Yaya y la comunidad maleña de 1962.",
        "icon": "fa-users-cog",
        "content": """
        <h3>Los Hombres y Mujeres que Hicieron Posible el Colegio</h3>
        <p>La creación de la I.E. Dionisio Manco Campos fue un auténtico triunfo de la unidad comunitaria maleña. En 1962, autoridades, agricultores, comerciantes y padres de familia sumaron voluntades para hacer realidad un anhelo postergado por generaciones.</p>
        <h4>Don José Huapaya Soriano - Alcalde Fundador</h4>
        <p>Líder nato y visionario burgomaestre distrital, Don José Huapaya Soriano asumió la causa educativa como su principal legado. Desafiando la escasez presupuestaria, cedió ambientes municipales y promovió la ordenanza que dio origen al Colegio Municipal Secundario Mixto.</p>
        <h4>Prof. Eusebio Ruiz Yaya - Primer Director</h4>
        <p>Convocado por el municipio para organizar la institución desde sus cimientos pedagógicos, el Prof. Eusebio Ruiz Yaya imprimió el sello de disciplina académica y patriotismo que perdura hasta el presente.</p>
        <h4>Comisión Vecinal Pro-Terreno</h4>
        <p>Vecinos ilustres y familias del valle organizaron tómbolas, rifas y jornadas de trabajo solidario para asegurar el terreno en San Pedro de Mala donde hoy se erige la infraestructura del colegio.</p>
        """
    },
    {
        "path": "institucional/mision-vision.html",
        "title": "Misión, Visión y Objetivos Estratégicos",
        "category": "Institucional",
        "desc": "Nuestra razón de ser y horizonte hacia el 2030 en la formación secundaria de Mala.",
        "icon": "fa-bullseye",
        "content": """
        <h3>Marco Filosófico y Prospectiva Institucional</h3>
        <div class="bg-blue-50 border-l-4 border-blue-600 p-6 rounded-r-2xl mb-6">
            <h4 class="font-bold text-dmcNavy-900 text-lg mb-2"><i class="fas fa-compass text-blue-600 mr-2"></i>Nuestra Misión</h4>
            <p class="text-sm text-slate-700 leading-relaxed">
                Brindar una educación secundaria integral, humanística, científica y tecnológica a los adolescentes y jóvenes de Mala y de la cuenca baja de Cañete, orientada por el Currículo Nacional de la Educación Básica (CNEB). Fomentamos la autonomía, el pensamiento crítico, la identidad cultural maleña y la convivencia armónica, formando ciudadanos capaces de construir proyectos de vida trascendentes.
            </p>
        </div>
        <div class="bg-yellow-50 border-l-4 border-yellow-500 p-6 rounded-r-2xl mb-6">
            <h4 class="font-bold text-dmcNavy-900 text-lg mb-2"><i class="fas fa-eye text-yellow-600 mr-2"></i>Nuestra Visión (al 2030)</h4>
            <p class="text-sm text-slate-700 leading-relaxed">
                Consolidarnos como la institución educativa pública emblemática y de referencia pedagógica de la provincia de Cañete y la región Lima Provincias, reconocida por su excelencia académica, su innovador uso de las TIC, su espíritu deportivo y artístico, y por formar egresados éticos que ingresan con éxito a la educación superior y lideran el progreso social.
            </p>
        </div>
        <h4>Objetivos Estratégicos</h4>
        <ul class="list-disc list-inside text-sm text-slate-600 space-y-2">
            <li>Elevar permanentemente los logros de aprendizaje en competencias matemáticas y comunicativas.</li>
            <li>Fortalecer el acompañamiento socioemocional y la cultura de paz en toda la comunidad escolar.</li>
            <li>Promover la innovación pedagógica en el Aula de Innovación (AIP) y laboratorios científicos.</li>
            <li>Consolidar alianzas con los gobiernos locales e instituciones productivas del valle de Mala.</li>
        </ul>
        """
    },
    {
        "path": "institucional/valores.html",
        "title": "Valores y Principios Institucionales",
        "category": "Institucional",
        "desc": "El decálogo ético que orienta la conducta de estudiantes, docentes y directivos de la I.E. DMC.",
        "icon": "fa-gem",
        "content": """
        <h3>Los Principios Éticos de la Comunidad Manco Campina</h3>
        <p>En concordancia con nuestro lema institucional <strong>"Patria, Estudio y Disciplina"</strong>, cultivamos un conjunto de valores éticos que definen la convivencia cotidiana en las aulas y fuera de ellas:</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
                <h4 class="font-bold text-red-600 text-sm mb-1"><i class="fas fa-flag mr-2"></i>Amor a la Patria e Identidad</h4>
                <p class="text-xs text-slate-600">Reconocimiento ferviente de los valores cívicos, el respeto a nuestros símbolos patrios y la revaloración de la historia y tradiciones de Mala.</p>
            </div>
            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
                <h4 class="font-bold text-blue-600 text-sm mb-1"><i class="fas fa-book-open mr-2"></i>Pasión por el Estudio y el Saber</h4>
                <p class="text-xs text-slate-600">Espíritu investigador, afán de superación personal, rigor intelectual y valoración de la ciencia y el pensamiento crítico.</p>
            </div>
            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
                <h4 class="font-bold text-yellow-600 text-sm mb-1"><i class="fas fa-balance-scale mr-2"></i>Disciplina y Responsabilidad</h4>
                <p class="text-xs text-slate-600">Puntualidad, orden en el trabajo, cumplimiento fiel de los deberes escolares y respeto sincero a las normas comunes.</p>
            </div>
            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
                <h4 class="font-bold text-emerald-600 text-sm mb-1"><i class="fas fa-leaf mr-2"></i>Solidaridad y Cuidado Ambiental</h4>
                <p class="text-xs text-slate-600">Empatía ante la necesidad ajena y preservación activa del entorno ecológico del valle y la costa maleña.</p>
            </div>
        </div>
        """
    },
    {
        "path": "institucional/himno.html",
        "title": "Himno Oficial Manco Campino",
        "category": "Institucional",
        "desc": "Letra oficial completa, análisis lírico y mensaje de nuestro canto institucional.",
        "icon": "fa-music",
        "content": """
        <h3>Himno de la I.E. Dionisio Manco Campos</h3>
        <p>El Himno Institucional es la expresión lírica más pura del fervor patrio y académico de los mancocampinos. Entonado con veneración en cada formación cívica y ceremonia de graduación:</p>
        <div class="bg-slate-900 text-white p-8 rounded-2xl border border-yellow-500/30 text-center font-serif space-y-6 my-6">
            <div class="text-yellow-400 font-bold uppercase tracking-widest text-xs">CORO</div>
            <p class="italic text-base">
                Una ruta de luz al futuro<br>
                Va trazando la acción juvenil<br>
                De esta pléyade noble pujante<br>
                Que es promesa de un nuevo Perú.
            </p>
            <div class="text-yellow-400 font-bold uppercase tracking-widest text-xs">ESTROFA I</div>
            <p class="italic text-sm">
                El valle de Mala fecundo y sereno<br>
                Nos brinda el aliento de su corazón<br>
                Y el limpio recuerdo del gran Manco Campos<br>
                Enciende en las mentes fulgor e ideal.
            </p>
            <div class="text-yellow-400 font-bold uppercase tracking-widest text-xs">ESTROFA II</div>
            <p class="italic text-sm">
                Florecen las almas de los estudiantes<br>
                En pos de la ciencia que da la verdad<br>
                Y prende su llama purificadora<br>
                La sana conducta que da la virtud.
            </p>
            <div class="text-yellow-400 font-bold uppercase tracking-widest text-xs">ESTROFA III</div>
            <p class="italic text-sm">
                Con fe en la mañana se elevan las<br>
                Voces vibrantes y claras de la juventud<br>
                Son himnos sonoros de manco campinos<br>
                Llevando la antorcha del nuevo Perú.
            </p>
        </div>
        <h4>Significado Poético</h4>
        <p>El texto exalta la geografía del valle del río Mala, rinde honor a la memoria de Don Dionisio Manco Campos y convoca a la juventud a portar con orgullo la antorcha del progreso nacional.</p>
        """
    },
    {
        "path": "institucional/escudo-simbolos.html",
        "title": "Escudo, Lema, Colores y Estandarte",
        "category": "Institucional",
        "desc": "Significado heráldico de los elementos visuales que representan a la I.E. DMC.",
        "icon": "fa-shield-alt",
        "content": """
        <h3>Los Emblemas Sagrados de Nuestra Institución</h3>
        <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center my-6">
            <div class="md:col-span-4 text-center">
                <img src="../img/escudo-dmc.svg" alt="Escudo DMC" class="h-56 mx-auto drop-shadow-xl">
                <span class="text-xs text-slate-500 font-bold block mt-2">Escudo Oficial Vectorial</span>
            </div>
            <div class="md:col-span-8 space-y-3">
                <h4 class="font-bold text-dmcNavy-900 text-lg">Elementos del Escudo Escolar:</h4>
                <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
                    <li><strong>La Antorcha Olímpica:</strong> Situada en la cúspide central, representa la luz del conocimiento que disipa las tinieblas de la ignorancia.</li>
                    <li><strong>El Libro Abierto:</strong> Símbolo del estudio incansable, las humanidades y la dedicación académica.</li>
                    <li><strong>Las Tres Estrellas Doradas:</strong> Representan los tres pilares de nuestro lema: Patria, Estudio y Disciplina.</li>
                    <li><strong>Las Ramas de Laurel:</strong> Homenaje al triunfo y la gloria de cada promoción de estudiantes.</li>
                    <li><strong>La Cinta Inferior:</strong> En gules patrios con el lema en oro imperecedero.</li>
                </ul>
            </div>
        </div>
        <h4>Colores Institucionales</h4>
        <p>El <strong>Azul Marino Imperial</strong> simboliza la seriedad, la profundidad del pensamiento y la lealtad; el <strong>Dorado Heroico</strong> representa la sabiduría, la excelencia académica y el triunfo; y el <strong>Rojo Patriota</strong> encarna la pasión cívica por el Perú.</p>
        """
    },
    {
        "path": "institucional/organigrama.html",
        "title": "Organigrama Estructural",
        "category": "Institucional",
        "desc": "Estructura organizativa y jerárquica de la I.E. Dionisio Manco Campos.",
        "icon": "fa-sitemap",
        "content": """
        <h3>Estructura Organizacional de la Institución</h3>
        <p>La I.E. Dionisio Manco Campos cuenta con una organización eficiente y participativa regulada por las normas de gestión escolar del Ministerio de Educación:</p>
        <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm my-6 space-y-4">
            <div class="p-4 bg-dmcNavy-900 text-white rounded-xl text-center font-bold text-sm">
                DIRECCIÓN GENERAL (Despacho Directoral)
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-3 bg-blue-50 border border-blue-200 rounded-lg text-center text-xs font-semibold text-blue-900">
                    CONEI (Consejo Educativo Institucional)
                </div>
                <div class="p-3 bg-yellow-50 border border-yellow-200 rounded-lg text-center text-xs font-semibold text-yellow-900">
                    APAFA (Asociación de Padres de Familia)
                </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div class="p-3 bg-slate-100 rounded-lg text-center text-xs font-bold text-slate-800">
                    Subdirección Pedagógica
                </div>
                <div class="p-3 bg-slate-100 rounded-lg text-center text-xs font-bold text-slate-800">
                    Coordinación de Tutoría (TOE)
                </div>
                <div class="p-3 bg-slate-100 rounded-lg text-center text-xs font-bold text-slate-800">
                    Coordinación de Innovación (AIP)
                </div>
            </div>
            <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-center text-xs text-slate-600">
                Plana Docente por Áreas &bull; Personal Administrativo y de Apoyo &bull; Municipio Escolar
            </div>
        </div>
        """
    },
    {
        "path": "institucional/direccion.html",
        "title": "Despacho de la Dirección General",
        "category": "Institucional",
        "desc": "Liderazgo pedagógico y administrativo al servicio de la comunidad educativa.",
        "icon": "fa-user-tie",
        "content": """
        <h3>Liderazgo y Gestión Escolar</h3>
        <p>El Despacho de la <strong>Dirección General</strong> de la I.E. Dionisio Manco Campos lidera el proceso de transformación educativa del plantel, garantizando el cumplimiento de los 5 Compromisos de Gestión Escolar establecidos por el MINEDU.</p>
        <h4>Funciones Principales de la Dirección</h4>
        <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li>Planificar, conducir y evaluar los instrumentos de gestión institucional (PEI, PAT, PCI, RI).</li>
            <li>Garantizar el cumplimiento efectivo de las horas lectivas en ambos turnos de secundaria.</li>
            <li>Monitorear y brindar acompañamiento pedagógico permanente a los docentes.</li>
            <li>Representar oficialmente al colegio ante la UGEL N° 08 de Cañete, la DRELP y la Municipalidad Distrital de Mala.</li>
            <li>Velar por la transparencia en la rendición de cuentas y mantenimiento del local escolar.</li>
        </ul>
        """
    },
    {
        "path": "institucional/subdireccion.html",
        "title": "Subdirección de Formación General",
        "category": "Institucional",
        "desc": "Acompañamiento técnico pedagógico y optimización de los aprendizajes.",
        "icon": "fa-chalkboard-teacher",
        "content": """
        <h3>Acompañamiento Pedagógico en Secundaria</h3>
        <p>La <strong>Subdirección de Formación General</strong> es el órgano responsable de coordinar, supervisar y asesorar el trabajo técnico-pedagógico de los docentes en las 11 áreas curriculares de secundaria.</p>
        <h4>Líneas de Acción:</h4>
        <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li>Revisión de programaciones curriculares anuales, unidades y sesiones de aprendizaje.</li>
            <li>Desarrollo de comunidades de aprendizaje profesional (GIA - Grupos de Interaprendizaje).</li>
            <li>Análisis de resultados de las evaluaciones diagnósticas, de proceso y de salida.</li>
            <li>Promoción de estrategias didácticas innovadoras centradas en el estudiante.</li>
        </ul>
        """
    },
    {
        "path": "institucional/pei.html",
        "title": "Proyecto Educativo Institucional (PEI)",
        "category": "Institucional",
        "desc": "Instrumento de gestión de mediano plazo que orienta el crecimiento formativo del plantel.",
        "icon": "fa-file-alt",
        "content": """
        <h3>Proyecto Educativo Institucional (PEI)</h3>
        <p>El <strong>PEI</strong> es el documento vertebrador que define la identidad, el diagnóstico situacional, la propuesta pedagógica y la propuesta de gestión de la I.E. Dionisio Manco Campos para el periodo cuatrienal.</p>
        <h4>Ejes Estratégicos del PEI:</h4>
        <ol class="list-decimal list-inside text-xs text-slate-600 space-y-2">
            <li><strong>Mejora Continua de los Aprendizajes:</strong> Estrategias para elevar el nivel de logro satisfactorio en comprensión de lectura y resolución de problemas.</li>
            <li><strong>Convivencia Democrática e Inclusiva:</strong> Implementación del protocolo de prevención del acoso escolar y fortalecimiento del bienestar socioemocional.</li>
            <li><strong>Articulación con la Comunidad:</strong> Participación activa de la APAFA, el municipio y las organizaciones civiles maleñas.</li>
        </ol>
        """
    },
    {
        "path": "institucional/pat.html",
        "title": "Plan Anual de Trabajo (PAT)",
        "category": "Institucional",
        "desc": "Metas, cronogramas y actividades programadas para el presente año lectivo.",
        "icon": "fa-calendar-check",
        "content": """
        <h3>Plan Anual de Trabajo (PAT)</h3>
        <p>El <strong>PAT</strong> concreta los objetivos del PEI en metas operativas, actividades mensuales y comisiones de trabajo para el presente año escolar.</p>
        <h4>Compromisos de Gestión Escolar:</h4>
        <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li><strong>Compromiso 1:</strong> Desarrollo integral de las y los estudiantes.</li>
            <li><strong>Compromiso 2:</strong> Acceso y permanencia en la educación básica regular y alternativa.</li>
            <li><strong>Compromiso 3:</strong> Gestión de las condiciones operativas orientada al sostenimiento del servicio educativo.</li>
            <li><strong>Compromiso 4:</strong> Gestión de la práctica pedagógica orientada al logro de aprendizajes previstos.</li>
            <li><strong>Compromiso 5:</strong> Gestión del bienestar escolar que promueva el desarrollo integral de los estudiantes.</li>
        </ul>
        """
    },
    {
        "path": "institucional/ri.html",
        "title": "Reglamento Interno Institucional (RI)",
        "category": "Institucional",
        "desc": "Pautas de convivencia, deberes, derechos y estímulos de la comunidad educativa.",
        "icon": "fa-gavel",
        "content": """
        <h3>Reglamento Interno y Normas de Convivencia</h3>
        <p>El <strong>Reglamento Interno</strong> regula los derechos, deberes, estímulos y medidas correctivas de todos los actores de la institución: estudiantes, directivos, docentes, auxiliares y familias.</p>
        <h4>Principios Básicos:</h4>
        <p class="text-xs text-slate-600">Se prohíbe todo trato degradante o violento. Las medidas correctivas tienen un fin estrictamente pedagógico y formativo, fomentando la empatía y la reparación del daño.</p>
        <h4>Compromisos del Estudiante Manco Campino:</h4>
        <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
            <li>Asistir puntualmente a sus clases respetando el turno asignado.</li>
            <li>Cuidar el mobiliario, los laboratorios y el ornato escolar.</li>
            <li>Tratar con respeto y consideración a sus compañeros y maestros.</li>
        </ul>
        """
    },
    {
        "path": "institucional/pci.html",
        "title": "Proyecto Curricular Institucional (PCI)",
        "category": "Institucional",
        "desc": "Diversificación y contextualización del Currículo Nacional a la realidad de Mala.",
        "icon": "fa-book-reader",
        "content": """
        <h3>Proyecto Curricular Institucional</h3>
        <p>El <strong>PCI</strong> contextualiza los estándares y competencias del Currículo Nacional a las características geográficas, sociales, económicas y culturales del distrito de Mala y la cuenca de Cañete.</p>
        <h4>Prioridades Curriculares:</h4>
        <p class="text-xs text-slate-600">Enfatizamos la identidad local maleña (historia del valle, producción vitivinícola y frutícola, festividades patronales), la conservación de la cuenca hídrica y el desarrollo de habilidades de emprendimiento en Educación para el Trabajo.</p>
        """
    },

    # 2. GRADOS Y SECCIONES (15 páginas)
    {
        "path": "grados/index.html",
        "title": "Estructura del Nivel Secundaria",
        "category": "Grados y Secciones",
        "desc": "Organización pedagógica del 1° al 5° año de secundaria en los ciclos VI y VII del CNEB.",
        "icon": "fa-graduation-cap",
        "content": """
        <h3>Nivel Secundaria de Educación Básica Regular</h3>
        <p>En la I.E. Dionisio Manco Campos atendemos a estudiantes de 1° a 5° grado de secundaria distribuidos en dos ciclos formativos:</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-6">
            <div class="bg-blue-50 p-6 rounded-2xl border border-blue-200">
                <h4 class="font-bold text-dmcNavy-900 text-base mb-2">Ciclo VI (1° y 2° de Secundaria)</h4>
                <p class="text-xs text-slate-600 leading-relaxed">
                    Etapa de transición de la primaria a la secundaria. Foco en la consolidación del pensamiento abstracto, autonomía en el estudio y adaptación a docentes por áreas especializadas.
                </p>
                <div class="mt-4 flex gap-2">
                    <a href="primer-grado.html" class="text-xs font-bold text-blue-700 bg-white px-3 py-1.5 rounded-lg border">1° Grado</a>
                    <a href="segundo-grado.html" class="text-xs font-bold text-blue-700 bg-white px-3 py-1.5 rounded-lg border">2° Grado</a>
                </div>
            </div>
            <div class="bg-yellow-50 p-6 rounded-2xl border border-yellow-200">
                <h4 class="font-bold text-dmcNavy-900 text-base mb-2">Ciclo VII (3°, 4° y 5° de Secundaria)</h4>
                <p class="text-xs text-slate-600 leading-relaxed">
                    Consolidación de competencias complejas, orientación vocacional, preparación para estudios superiores y culminación del perfil de egreso escolar.
                </p>
                <div class="mt-4 flex gap-2">
                    <a href="tercer-grado.html" class="text-xs font-bold text-yellow-800 bg-white px-3 py-1.5 rounded-lg border">3° Grado</a>
                    <a href="cuarto-grado.html" class="text-xs font-bold text-yellow-800 bg-white px-3 py-1.5 rounded-lg border">4° Grado</a>
                    <a href="quinto-grado.html" class="text-xs font-bold text-yellow-800 bg-white px-3 py-1.5 rounded-lg border">5° Grado</a>
                </div>
            </div>
        </div>
        """
    },
    {
        "path": "grados/primer-grado.html",
        "title": "1° Año de Secundaria",
        "category": "Grados y Secciones",
        "desc": "Objetivos pedagógicos, competencias clave y proceso de inserción a la secundaria.",
        "icon": "fa-user",
        "content": """
        <h3>1° de Secundaria: El Ingreso a la Gran Familia Manco Campina</h3>
        <p>El primer grado de secundaria representa un hito fundamental en la vida del estudiante. Procedentes de las escuelas primarias del distrito de Mala, San Antonio, Santa Cruz y anexos, nuestros estudiantes reciben acompañamiento tutorial intensivo.</p>
        <h4>Prioridades Pedagógicas:</h4>
        <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li>Afianzamiento de hábitos de estudio y organización del tiempo libre.</li>
            <li>Comprensión lectora inferencial y crítica de textos diversos.</li>
            <li>Desarrollo del razonamiento matemático y aritmética fundamental.</li>
            <li>Fomento del trabajo colaborativo y valores cívicos.</li>
        </ul>
        """
    },
    {
        "path": "grados/primer-grado-secciones.html",
        "title": "1° Año - Cuadro de Secciones",
        "category": "Grados y Secciones",
        "desc": "Distribución de secciones A, B, C, D, E y docentes tutores del primer grado.",
        "icon": "fa-chalkboard",
        "content": """
        <h3>Secciones de 1° de Secundaria</h3>
        <p>Para brindar una atención personalizada, el primer grado cuenta con secciones organizadas en turnos de mañana y tarde con un promedio de 30 a 35 estudiantes por aula:</p>
        <div class="overflow-x-auto my-6">
            <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden">
                <thead class="bg-dmcNavy-900 text-white font-bold">
                    <tr><th class="p-3">Sección</th><th class="p-3">Turno</th><th class="p-3">Tutoría</th><th class="p-3">Aula</th></tr>
                </thead>
                <tbody class="divide-y divide-slate-100 bg-white">
                    <tr><td class="p-3 font-bold">1° "A"</td><td class="p-3">Mañana</td><td class="p-3">Prof. Responsable de Área</td><td class="p-3">Pabellón 1 - Aula 101</td></tr>
                    <tr><td class="p-3 font-bold">1° "B"</td><td class="p-3">Mañana</td><td class="p-3">Prof. Responsable de Área</td><td class="p-3">Pabellón 1 - Aula 102</td></tr>
                    <tr><td class="p-3 font-bold">1° "C"</td><td class="p-3">Mañana</td><td class="p-3">Prof. Responsable de Área</td><td class="p-3">Pabellón 1 - Aula 103</td></tr>
                    <tr><td class="p-3 font-bold">1° "D"</td><td class="p-3">Tarde</td><td class="p-3">Prof. Responsable de Área</td><td class="p-3">Pabellón 2 - Aula 104</td></tr>
                    <tr><td class="p-3 font-bold">1° "E"</td><td class="p-3">Tarde</td><td class="p-3">Prof. Responsable de Área</td><td class="p-3">Pabellón 2 - Aula 105</td></tr>
                </tbody>
            </table>
        </div>
        """
    },
    {
        "path": "grados/segundo-grado.html",
        "title": "2° Año de Secundaria",
        "category": "Grados y Secciones",
        "desc": "Cierre del Ciclo VI y consolidación de competencias básicas en secundaria.",
        "icon": "fa-user",
        "content": """
        <h3>2° de Secundaria: Consolidación y Madurez Académica</h3>
        <p>En el segundo grado, los estudiantes consolidan las capacidades requeridas para culminar el Ciclo VI. Desarrollan una mayor capacidad analítica frente a problemas cuantitativos y textuales.</p>
        <h4>Enfoque Formativo:</h4>
        <p class="text-xs text-slate-600">Participación obligatoria en proyectos de indagación científica escolar (Eureka), redacción de ensayos de opinión y prácticas de laboratorio experimental.</p>
        """
    },
    {
        "path": "grados/segundo-grado-secciones.html",
        "title": "2° Año - Cuadro de Secciones",
        "category": "Grados y Secciones",
        "desc": "Detalle de secciones y organización del segundo grado de secundaria.",
        "icon": "fa-chalkboard",
        "content": """
        <h3>Secciones de 2° de Secundaria</h3>
        <p>Distribución pedagógica para el segundo año de educación secundaria en la I.E. Dionisio Manco Campos:</p>
        <div class="overflow-x-auto my-6">
            <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden">
                <thead class="bg-dmcNavy-900 text-white font-bold">
                    <tr><th class="p-3">Sección</th><th class="p-3">Turno</th><th class="p-3">Ámbito</th><th class="p-3">Ubicación</th></tr>
                </thead>
                <tbody class="divide-y divide-slate-100 bg-white">
                    <tr><td class="p-3 font-bold">2° "A"</td><td class="p-3">Mañana</td><td class="p-3">Formación General</td><td class="p-3">Pabellón Central</td></tr>
                    <tr><td class="p-3 font-bold">2° "B"</td><td class="p-3">Mañana</td><td class="p-3">Formación General</td><td class="p-3">Pabellón Central</td></tr>
                    <tr><td class="p-3 font-bold">2° "C"</td><td class="p-3">Mañana</td><td class="p-3">Formación General</td><td class="p-3">Pabellón Central</td></tr>
                    <tr><td class="p-3 font-bold">2° "D"</td><td class="p-3">Tarde</td><td class="p-3">Formación General</td><td class="p-3">Pabellón Central</td></tr>
                    <tr><td class="p-3 font-bold">2° "E"</td><td class="p-3">Tarde</td><td class="p-3">Formación General</td><td class="p-3">Pabellón Central</td></tr>
                </tbody>
            </table>
        </div>
        """
    },
    {
        "path": "grados/tercer-grado.html",
        "title": "3° Año de Secundaria",
        "category": "Grados y Secciones",
        "desc": "Inicio del Ciclo VII: mayor exigencia en ciencias, historia y matemáticas avanzadas.",
        "icon": "fa-user",
        "content": """
        <h3>3° de Secundaria: El Ingreso al Ciclo VII</h3>
        <p>En el tercer año de secundaria, los alumnos inician el Ciclo VII del CNEB. Se profundiza el estudio del álgebra, la física elemental, la historia universal y la química.</p>
        <h4>Desafíos Formativos:</h4>
        <p class="text-xs text-slate-600">Promoción del liderazgo juvenil en el Municipio Escolar y formación de brigadas especializadas de primeros auxilios y cultura cívica.</p>
        """
    },
    {
        "path": "grados/tercer-grado-secciones.html",
        "title": "3° Año - Cuadro de Secciones",
        "category": "Grados y Secciones",
        "desc": "Distribución de secciones de 3° año en ambos turnos escolares.",
        "icon": "fa-chalkboard",
        "content": """
        <h3>Secciones de 3° de Secundaria</h3>
        <p>El tercer año agrupa a estudiantes con alto compromiso en talleres artísticos y deportivos:</p>
        <div class="overflow-x-auto my-6">
            <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden">
                <thead class="bg-dmcNavy-900 text-white font-bold">
                    <tr><th class="p-3">Sección</th><th class="p-3">Turno</th><th class="p-3">Orientación</th></tr>
                </thead>
                <tbody class="divide-y divide-slate-100 bg-white">
                    <tr><td class="p-3 font-bold">3° "A"</td><td class="p-3">Mañana</td><td class="p-3">Científico - Humanista</td></tr>
                    <tr><td class="p-3 font-bold">3° "B"</td><td class="p-3">Mañana</td><td class="p-3">Científico - Humanista</td></tr>
                    <tr><td class="p-3 font-bold">3° "C"</td><td class="p-3">Mañana</td><td class="p-3">Científico - Humanista</td></tr>
                    <tr><td class="p-3 font-bold">3° "D"</td><td class="p-3">Tarde</td><td class="p-3">Científico - Humanista</td></tr>
                    <tr><td class="p-3 font-bold">3° "E"</td><td class="p-3">Tarde</td><td class="p-3">Científico - Humanista</td></tr>
                </tbody>
            </table>
        </div>
        """
    },
    {
        "path": "grados/cuarto-grado.html",
        "title": "4° Año de Secundaria",
        "category": "Grados y Secciones",
        "desc": "Orientación vocacional, preparación preuniversitaria y proyectos de emprendimiento.",
        "icon": "fa-user",
        "content": """
        <h3>4° de Secundaria: Proyección Vocacional y Futuro</h3>
        <p>El cuarto grado orienta a los estudiantes hacia la definición de sus metas post-secundarias mediante test vocacionales, visitas formativas y proyectos de Educación para el Trabajo.</p>
        """
    },
    {
        "path": "grados/cuarto-grado-secciones.html",
        "title": "4° Año - Cuadro de Secciones",
        "category": "Grados y Secciones",
        "desc": "Detalle de aulas y secciones del 4° grado de secundaria.",
        "icon": "fa-chalkboard",
        "content": """
        <h3>Secciones de 4° de Secundaria</h3>
        <p>Distribución de secciones de 4° grado en la I.E. Dionisio Manco Campos:</p>
        <div class="overflow-x-auto my-6">
            <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden">
                <thead class="bg-dmcNavy-900 text-white font-bold">
                    <tr><th class="p-3">Sección</th><th class="p-3">Turno</th><th class="p-3">Proyectos</th></tr>
                </thead>
                <tbody class="divide-y divide-slate-100 bg-white">
                    <tr><td class="p-3 font-bold">4° "A"</td><td class="p-3">Mañana</td><td class="p-3">Emprendimiento EPT</td></tr>
                    <tr><td class="p-3 font-bold">4° "B"</td><td class="p-3">Mañana</td><td class="p-3">Emprendimiento EPT</td></tr>
                    <tr><td class="p-3 font-bold">4° "C"</td><td class="p-3">Mañana</td><td class="p-3">Emprendimiento EPT</td></tr>
                    <tr><td class="p-3 font-bold">4° "D"</td><td class="p-3">Tarde</td><td class="p-3">Emprendimiento EPT</td></tr>
                    <tr><td class="p-3 font-bold">4° "E"</td><td class="p-3">Tarde</td><td class="p-3">Emprendimiento EPT</td></tr>
                </tbody>
            </table>
        </div>
        """
    },
    {
        "path": "grados/quinto-grado.html",
        "title": "5° Año de Secundaria",
        "category": "Grados y Secciones",
        "desc": "Promoción de egreso, perfil de salida escolar y preparación para la educación superior.",
        "icon": "fa-user-graduate",
        "content": """
        <h3>5° de Secundaria: La Promoción y el Perfil de Egreso</h3>
        <p>El quinto grado corona el esfuerzo escolar. Los estudiantes consolidan las 31 competencias del Currículo Nacional, preparándose para postular a universidades públicas y privadas, institutos tecnológicos o las Fuerzas Armadas.</p>
        <h4>Tradición de la Promoción Manco Campina:</h4>
        <p class="text-xs text-slate-600">Nuestros egresados representan a Mala en las principales casas superiores de estudio del país (UNMSM, UNI, UNAC, PUCP, Faustino Sánchez Carrión de Huacho y Cañete).</p>
        """
    },
    {
        "path": "grados/quinto-grado-secciones.html",
        "title": "5° Año - Cuadro de Secciones",
        "category": "Grados y Secciones",
        "desc": "Aulas de la promoción saliente de la I.E. Dionisio Manco Campos.",
        "icon": "fa-chalkboard",
        "content": """
        <h3>Secciones de 5° de Secundaria (Promoción)</h3>
        <p>Cuadro de secciones del último año de secundaria:</p>
        <div class="overflow-x-auto my-6">
            <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden">
                <thead class="bg-dmcNavy-900 text-white font-bold">
                    <tr><th class="p-3">Sección</th><th class="p-3">Turno</th><th class="p-3">Culminación</th></tr>
                </thead>
                <tbody class="divide-y divide-slate-100 bg-white">
                    <tr><td class="p-3 font-bold">5° "A"</td><td class="p-3">Mañana</td><td class="p-3">Certificación Oficial MINEDU</td></tr>
                    <tr><td class="p-3 font-bold">5° "B"</td><td class="p-3">Mañana</td><td class="p-3">Certificación Oficial MINEDU</td></tr>
                    <tr><td class="p-3 font-bold">5° "C"</td><td class="p-3">Mañana</td><td class="p-3">Certificación Oficial MINEDU</td></tr>
                    <tr><td class="p-3 font-bold">5° "D"</td><td class="p-3">Tarde</td><td class="p-3">Certificación Oficial MINEDU</td></tr>
                    <tr><td class="p-3 font-bold">5° "E"</td><td class="p-3">Tarde</td><td class="p-3">Certificación Oficial MINEDU</td></tr>
                </tbody>
            </table>
        </div>
        """
    },
    {
        "path": "grados/cuadro-merito.html",
        "title": "Cuadro de Honor y Mérito Estudiantil",
        "category": "Grados y Secciones",
        "desc": "Reconocimiento a la excelencia académica, primer y segundo puesto de cada grado.",
        "icon": "fa-award",
        "content": """
        <h3>Cuadro de Honor Manco Campino</h3>
        <p>La I.E. Dionisio Manco Campos premia el esfuerzo, la constancia y el rendimiento académico de sus alumnos en los actos cívicos y la clausura anual del año escolar.</p>
        <h4>Criterios del Cuadro de Mérito:</h4>
        <p class="text-xs text-slate-600">Basado en el promedio ponderado oficial del sistema SIAGIE, reconociendo el logro destacado (AD) en todas las competencias curriculares.</p>
        """
    },
    {
        "path": "grados/evaluacion.html",
        "title": "Sistema de Calificación CNEB",
        "category": "Grados y Secciones",
        "desc": "Escala de calificación cualitativa (AD, A, B, C) según la RVM N° 094-2020-MINEDU.",
        "icon": "fa-check-double",
        "content": """
        <h3>Evaluación Formativa por Competencias</h3>
        <p>Conforme a la normativa oficial del Ministerio de Educación, la evaluación en secundaria es cualitativa y formativa:</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 my-6">
            <div class="bg-blue-50 p-4 rounded-xl border border-blue-200 text-center">
                <span class="text-2xl font-black text-blue-700">AD</span>
                <h4 class="font-bold text-xs mt-1 text-slate-900">Logro Destacado</h4>
                <p class="text-[11px] text-slate-600 mt-1">Supera el nivel esperado para el grado.</p>
            </div>
            <div class="bg-emerald-50 p-4 rounded-xl border border-emerald-200 text-center">
                <span class="text-2xl font-black text-emerald-700">A</span>
                <h4 class="font-bold text-xs mt-1 text-slate-900">Logro Esperado</h4>
                <p class="text-[11px] text-slate-600 mt-1">Alcanza el nivel de competencia previsto.</p>
            </div>
            <div class="bg-yellow-50 p-4 rounded-xl border border-yellow-200 text-center">
                <span class="text-2xl font-black text-yellow-700">B</span>
                <h4 class="font-bold text-xs mt-1 text-slate-900">En Proceso</h4>
                <p class="text-[11px] text-slate-600 mt-1">Está cerca de lograr la competencia.</p>
            </div>
            <div class="bg-red-50 p-4 rounded-xl border border-red-200 text-center">
                <span class="text-2xl font-black text-red-700">C</span>
                <h4 class="font-bold text-xs mt-1 text-slate-900">En Inicio</h4>
                <p class="text-[11px] text-slate-600 mt-1">Muestra avances mínimos y requiere refuerzo.</p>
            </div>
        </div>
        """
    },
    {
        "path": "grados/horarios-turnos.html",
        "title": "Horarios: Turno Mañana y Tarde",
        "category": "Grados y Secciones",
        "desc": "Distribución horaria, horas pedagógicas y recreos de secundaria.",
        "icon": "fa-clock",
        "content": """
        <h3>Horarios de Clases en Secundaria EBR</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-6">
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
                <h4 class="font-bold text-dmcNavy-900 text-base mb-2"><i class="fas fa-sun text-yellow-500 mr-2"></i>Turno Mañana</h4>
                <ul class="text-xs text-slate-600 space-y-1.5">
                    <li><strong>Ingreso:</strong> 7:30 a.m.</li>
                    <li><strong>Primer Bloque:</strong> 7:45 a.m. - 10:00 a.m.</li>
                    <li><strong>Recreo:</strong> 10:00 a.m. - 10:30 a.m.</li>
                    <li><strong>Segundo Bloque:</strong> 10:30 a.m. - 1:00 p.m.</li>
                    <li><strong>Salida:</strong> 1:00 p.m.</li>
                </ul>
            </div>
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
                <h4 class="font-bold text-dmcNavy-900 text-base mb-2"><i class="fas fa-cloud-sun text-amber-500 mr-2"></i>Turno Tarde</h4>
                <ul class="text-xs text-slate-600 space-y-1.5">
                    <li><strong>Ingreso:</strong> 1:15 p.m.</li>
                    <li><strong>Primer Bloque:</strong> 1:30 p.m. - 3:45 p.m.</li>
                    <li><strong>Recreo:</strong> 3:45 p.m. - 4:15 p.m.</li>
                    <li><strong>Segundo Bloque:</strong> 4:15 p.m. - 6:30 p.m.</li>
                    <li><strong>Salida:</strong> 6:30 p.m.</li>
                </ul>
            </div>
        </div>
        """
    },
    {
        "path": "grados/normas-convivencia-aula.html",
        "title": "Normas de Convivencia en el Aula",
        "category": "Grados y Secciones",
        "desc": "Acuerdos democráticos elaborados por los propios estudiantes y tutores.",
        "icon": "fa-users",
        "content": """
        <h3>Convivencia Armónica en el Salón de Clases</h3>
        <p>Al inicio de cada año escolar, cada sección elabora en asamblea de aula sus normas de convivencia:</p>
        <ol class="list-decimal list-inside text-xs text-slate-600 space-y-2 my-4">
            <li>Escuchar atentamente la participación de compañeros y docentes respetando las opiniones distintas.</li>
            <li>Mantener limpia el aula depositando la basura en los tachos de reciclaje.</li>
            <li>Cuidar el mobiliario escolar, carpetas y pizarras.</li>
            <li>Evitar el uso de teléfonos celulares u otros dispositivos durante el dictado de clases salvo indicación pedagógica.</li>
            <li>Resolver cualquier desacuerdo mediante el diálogo pacífico y la tutoría.</li>
        </ol>
        """
    },

    # 3. ÁREAS CURRICULARES (12 páginas)
    {
        "path": "areas-curriculares/index.html",
        "title": "Plan Curricular Oficial CNEB",
        "category": "Áreas Curriculares",
        "desc": "Las 11 áreas curriculares impartidas en la I.E. Dionisio Manco Campos según el MINEDU.",
        "icon": "fa-book",
        "content": """
        <h3>Plan Curricular de Secundaria</h3>
        <p>La formación en secundaria abarca 35 horas pedagógicas semanales distribuidas equilibradamente en 11 áreas:</p>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 my-6 text-xs text-center">
            <a href="matematica.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Matemática</a>
            <a href="comunicacion.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Comunicación</a>
            <a href="ciencia-tecnologia.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Ciencia y Tecnología</a>
            <a href="ciencias-sociales.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Ciencias Sociales</a>
            <a href="dpcc.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">DPCC</a>
            <a href="ingles.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Inglés</a>
            <a href="arte-cultura.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Arte y Cultura</a>
            <a href="educacion-fisica.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Educación Física</a>
            <a href="educacion-para-el-trabajo.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">EPT</a>
            <a href="educacion-religiosa.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Educación Religiosa</a>
            <a href="tutoria.html" class="p-3 bg-white rounded-xl border hover:border-yellow-500 font-bold text-slate-800 shadow-2xs">Tutoría (TOE)</a>
        </div>
        """
    },
    {
        "path": "areas-curriculares/matematica.html",
        "title": "Área de Matemática",
        "category": "Áreas Curriculares",
        "desc": "Resolución de problemas de cantidad, regularidad, equivalencia, cambio y geometría.",
        "icon": "fa-calculator",
        "content": """
        <h3>Área de Matemática</h3>
        <p>Desarrolla 4 competencias fundamentales: Resolución de problemas de cantidad, regularidad, forma y gestión de datos. Fomentamos la participación en la Olimpiada Nacional Escolar de Matemática (ONEM).</p>
        """
    },
    {
        "path": "areas-curriculares/comunicacion.html",
        "title": "Área de Comunicación",
        "category": "Áreas Curriculares",
        "desc": "Lectura crítica, redacción de ensayos y expresión oral efectiva.",
        "icon": "fa-pencil-alt",
        "content": """
        <h3>Área de Comunicación</h3>
        <p>Fortalece las competencias de comprensión lectora, producción de textos y oratoria para que el estudiante comunique sus ideas con claridad y convicción.</p>
        """
    },
    {
        "path": "areas-curriculares/ciencia-tecnologia.html",
        "title": "Área de Ciencia y Tecnología",
        "category": "Áreas Curriculares",
        "desc": "Método científico, experimentación en laboratorio y feria escolar Eureka.",
        "icon": "fa-flask",
        "content": """
        <h3>Área de Ciencia y Tecnología</h3>
        <p>Promueve la indagación experimental, la comprensión del mundo natural y el diseño de soluciones tecnológicas sustentables para Mala.</p>
        """
    },
    {
        "path": "areas-curriculares/ciencias-sociales.html",
        "title": "Área de Ciencias Sociales",
        "category": "Áreas Curriculares",
        "desc": "Historia del Perú y del mundo, geografía del valle de Mala y economía ciudadana.",
        "icon": "fa-globe",
        "content": """
        <h3>Área de Ciencias Sociales</h3>
        <p>Forma la conciencia histórica del alumno, el conocimiento geográfico de la cuenca del río Mala y la gestión responsable de los recursos financieros.</p>
        """
    },
    {
        "path": "areas-curriculares/dpcc.html",
        "title": "Desarrollo Personal, Ciudadanía y Cívica",
        "category": "Áreas Curriculares",
        "desc": "Autoestima, identidad, derechos humanos y convivencia democrática.",
        "icon": "fa-balance-scale",
        "content": """
        <h3>Desarrollo Personal, Ciudadanía y Cívica (DPCC)</h3>
        <p>Espacio clave para la construcción de la identidad adolescente, la ética personal y la participación democrática informada.</p>
        """
    },
    {
        "path": "areas-curriculares/ingles.html",
        "title": "Idioma Extranjero - Inglés",
        "category": "Áreas Curriculares",
        "desc": "Competencias comunicativas en inglés para la interacción y apertura global.",
        "icon": "fa-language",
        "content": """
        <h3>Área de Inglés como Lengua Extranjera</h3>
        <p>Desarrolla habilidades de comprensión auditiva, lectura y conversación en la lengua internacional de la ciencia y los negocios.</p>
        """
    },
    {
        "path": "areas-curriculares/arte-cultura.html",
        "title": "Área de Arte y Cultura",
        "category": "Áreas Curriculares",
        "desc": "Danza folclórica, música, artes plásticas y apreciación cultural en Mala.",
        "icon": "fa-palette",
        "content": """
        <h3>Área de Arte y Cultura</h3>
        <p>Estimula la sensibilidad estética mediante el dibujo, la pintura, la música y las tradicionales danzas folclóricas de la costa peruana.</p>
        """
    },
    {
        "path": "areas-curriculares/educacion-fisica.html",
        "title": "Educación Física y Deportes",
        "category": "Áreas Curriculares",
        "desc": "Salud corporal, desarrollo motriz, gimnasia y deportes de equipo.",
        "icon": "fa-running",
        "content": """
        <h3>Área de Educación Física</h3>
        <p>Promueve un estilo de vida activo y saludable a través del deporte formativo, atletismo y juegos predeportivos en las losas de la I.E. DMC.</p>
        """
    },
    {
        "path": "areas-curriculares/educacion-para-el-trabajo.html",
        "title": "Educación para el Trabajo (EPT)",
        "category": "Áreas Curriculares",
        "desc": "Emprendimiento económico y social, habilidades técnicas y ofimática.",
        "icon": "fa-tools",
        "content": """
        <h3>Educación para el Trabajo (EPT)</h3>
        <p>Capacita en modelos de negocio Canvas, diseño de proyectos productivos vinculados a la agricultura y el turismo de Mala.</p>
        """
    },
    {
        "path": "areas-curriculares/educacion-religiosa.html",
        "title": "Área de Educación Religiosa",
        "category": "Áreas Curriculares",
        "desc": "Formación espiritual, moral, respeto ecuménico y compromiso solidario.",
        "icon": "fa-hands",
        "content": """
        <h3>Área de Educación Religiosa</h3>
        <p>Promueve valores de amor al prójimo, reconciliación, esperanza y solidaridad en armonía con las tradiciones cristianas de Mala.</p>
        """
    },
    {
        "path": "areas-curriculares/tutoria.html",
        "title": "Tutoría y Orientación Educativa (TOE)",
        "category": "Áreas Curriculares",
        "desc": "Acompañamiento socioafectivo, prevención de adicciones y escuela de líderes.",
        "icon": "fa-heart",
        "content": """
        <h3>Tutoría y Orientación Educativa (TOE)</h3>
        <p>Acompaña el desarrollo emocional de los estudiantes mediante sesiones grupales, consejería individual y articulación con los padres de familia.</p>
        """
    },

    # 4. CEBA (8 páginas)
    {
        "path": "ceba/index.html",
        "title": "CEBA Dionisio Manco Campos",
        "category": "Educación Básica Alternativa",
        "desc": "Modalidad de educación para jóvenes y adultos con Código Modular 0285676.",
        "icon": "fa-graduation-cap",
        "content": """
        <h3>Educación Básica Alternativa (CEBA) DMC</h3>
        <p>El <strong>CEBA Dionisio Manco Campos</strong> ofrece educación gratuita con validez oficial del MINEDU a jóvenes y adultos que no concluyeron sus estudios escolares regulares.</p>
        <p>Con horarios nocturnos y semipresenciales adaptados a personas que trabajan, el CEBA permite culminar la secundaria y obtener el Certificado Oficial de Estudios.</p>
        """
    },
    {
        "path": "ceba/ciclo-inicial.html",
        "title": "CEBA - Ciclo Inicial",
        "category": "Educación Básica Alternativa",
        "desc": "Alfabetización funcional y primeros aprendizajes en la modalidad alternativa.",
        "icon": "fa-book",
        "content": """
        <h3>Ciclo Inicial del CEBA</h3>
        <p>Dirigido a personas que desean aprender a leer, escribir y realizar cálculos matemáticos elementales en un ambiente cálido y de respeto mutuo.</p>
        """
    },
    {
        "path": "ceba/ciclo-intermedio.html",
        "title": "CEBA - Ciclo Intermedio",
        "category": "Educación Básica Alternativa",
        "desc": "Consolidación de competencias correspondientes a la educación primaria.",
        "icon": "fa-book-open",
        "content": """
        <h3>Ciclo Intermedio del CEBA</h3>
        <p>Equivalente a los últimos grados de primaria. Afianza la lectoescritura, las operaciones matemáticas y nociones de ciencia y sociedad.</p>
        """
    },
    {
        "path": "ceba/ciclo-avanzado.html",
        "title": "CEBA - Ciclo Avanzado (Secundaria)",
        "category": "Educación Básica Alternativa",
        "desc": "Equivalente completo a la Educación Secundaria en cuatro periodos promocionales.",
        "icon": "fa-user-graduate",
        "content": """
        <h3>Ciclo Avanzado: Secundaria para Adultos</h3>
        <p>Estructurado en cuatro grados o periodos promocionales. Permite al egresado postular a cualquier universidad o instituto técnico superior del Perú.</p>
        """
    },
    {
        "path": "ceba/matricula-ceba.html",
        "title": "Matrícula y Requisitos en CEBA",
        "category": "Educación Básica Alternativa",
        "desc": "Documentación para matricularse en el turno nocturno o modalidad semipresencial.",
        "icon": "fa-clipboard-list",
        "content": """
        <h3>Requisitos de Matrícula en el CEBA</h3>
        <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li>Tener 14 años o más para ingresar a la modalidad alternativa.</li>
            <li>Copia simple del DNI o documento de identidad.</li>
            <li>Certificado de estudios de los últimos grados cursados (o prueba de ubicación gratuita).</li>
            <li>Ficha de matrícula gratuita en secretaría del CEBA.</li>
        </ul>
        """
    },
    {
        "path": "ceba/horarios-ceba.html",
        "title": "Horarios de Clases del CEBA",
        "category": "Educación Básica Alternativa",
        "desc": "Turno vespertino y nocturno adaptado a las responsabilidades laborales.",
        "icon": "fa-clock",
        "content": """
        <h3>Horarios de Atención del CEBA</h3>
        <p>Las clases presenciales se desarrollan de lunes a viernes de <strong>6:30 p.m. a 10:00 p.m.</strong> en las aulas de la I.E. Dionisio Manco Campos.</p>
        """
    },
    {
        "path": "ceba/docentes-ceba.html",
        "title": "Plana Docente del CEBA",
        "category": "Educación Básica Alternativa",
        "desc": "Profesores especializados en educación andragógica y formación de adultos.",
        "icon": "fa-chalkboard-teacher",
        "content": """
        <h3>Cuerpo Docente del CEBA DMC</h3>
        <p>Profesores con amplia experiencia en metodologías activas y formativas orientadas al público adulto, con paciencia y calidez humana.</p>
        """
    },
    {
        "path": "ceba/certificacion-ceba.html",
        "title": "Certificación y Convalidación en CEBA",
        "category": "Educación Básica Alternativa",
        "desc": "Emisión de certificados oficiales reconocidos por el MINEDU para estudios superiores.",
        "icon": "fa-certificate",
        "content": """
        <h3>Certificado Oficial de Educación Básica</h3>
        <p>El certificado de estudios emitido por el CEBA Dionisio Manco Campos tiene exactamente el mismo valor legal que el de la Educación Básica Regular para postular a empleos y universidades.</p>
        """
    },

    # 5. TALLERES Y ACTIVIDADES (12 páginas)
    {
        "path": "talleres-actividades/index.html",
        "title": "Talleres y Formación Complementaria",
        "category": "Talleres y Actividades",
        "desc": "Espacios extracurriculares artísticos, deportivos y científicos de la I.E. DMC.",
        "icon": "fa-palette",
        "content": """
        <h3>Formación Integral Fuera del Aula</h3>
        <p>La I.E. Dionisio Manco Campos fomenta el desarrollo de los talentos individuales mediante talleres sabatinos y en contraturno escolar.</p>
        """
    },
    {
        "path": "talleres-actividades/banda-guerra.html",
        "title": "Banda de Guerra y Escolta Escolar",
        "category": "Talleres y Actividades",
        "desc": "Orgullo cívico en desfiles patrios de Mala y Cañete.",
        "icon": "fa-drum",
        "content": """
        <h3>Banda de Guerra Escolar DMC</h3>
        <p>Integrada por destacados estudiantes con rigurosa disciplina marcial en tarolas, bombos, platillos y liras. Encabeza los desfiles del 28 de Julio y Aniversario Distrital de Mala.</p>
        """
    },
    {
        "path": "talleres-actividades/banda-musica.html",
        "title": "Banda de Música Instrumental",
        "category": "Talleres y Actividades",
        "desc": "Ejecución de marchas, himnos y piezas musicales clásicas y peruanas.",
        "icon": "fa-music",
        "content": """
        <h3>Banda de Música de la I.E. DMC</h3>
        <p>Espacio donde los jóvenes aprenden lectura de partituras, solfeo e instrumentos de viento y percusión.</p>
        """
    },
    {
        "path": "talleres-actividades/club-ciencias-eureka.html",
        "title": "Club de Ciencias y Proyecto Eureka",
        "category": "Talleres y Actividades",
        "desc": "Semillero de investigadores escolares para la feria nacional FENCYT Eureka.",
        "icon": "fa-microscope",
        "content": """
        <h3>Club de Ciencias 'Dionisio Manco Campos'</h3>
        <p>Fomenta proyectos de indagación científica orientados al tratamiento de aguas en Mala, agricultura orgánica y energías renovables.</p>
        """
    },
    {
        "path": "talleres-actividades/robotica-computo.html",
        "title": "Taller de Robótica y Programación",
        "category": "Talleres y Actividades",
        "desc": "Aprendizaje de robótica educativa, circuitos Arduino y pensamiento computacional.",
        "icon": "fa-robot",
        "content": """
        <h3>Taller de Robótica Educativa</h3>
        <p>En el Aula de Innovación, los alumnos programan sensores, motores y prototipos automatizados que resuelven retos cotidianos.</p>
        """
    },
    {
        "path": "talleres-actividades/danzas-folclor.html",
        "title": "Elenco de Danzas Folclóricas",
        "category": "Talleres y Actividades",
        "desc": "Revaloración de la marinera, festejo cañetano y danzas tradicionales del Perú.",
        "icon": "fa-shoe-prints",
        "content": """
        <h3>Elenco de Danzas Manco Campino</h3>
        <p>Cuna de talento dancístico que representa a Cañete en encuentros de festidanza regional e intercolegial.</p>
        """
    },
    {
        "path": "talleres-actividades/futbol.html",
        "title": "Selección Escolar de Fútbol",
        "category": "Talleres y Actividades",
        "desc": "Entrenamiento formativo y participación en los Juegos Escolares Deportivos (JEDPA).",
        "icon": "fa-futbol",
        "content": """
        <h3>Selección de Fútbol Masculino y Femenino</h3>
        <p>Formación deportiva en táctica, resistencia y juego limpio en las categorías Sub-14 y Sub-17 de la UGEL 08 Cañete.</p>
        """
    },
    {
        "path": "talleres-actividades/voleibol.html",
        "title": "Selección Escolar de Voleibol",
        "category": "Talleres y Actividades",
        "desc": "Pasión por el vóley en categorías formativas de menores y juveniles.",
        "icon": "fa-volleyball-ball",
        "content": """
        <h3>Selección de Voleibol DMC</h3>
        <p>Entrenamiento continuo en las losas deportivas del colegio con destacados puestos en los torneos provinciales de Cañete.</p>
        """
    },
    {
        "path": "talleres-actividades/atletismo.html",
        "title": "Taller de Atletismo y Resistencia",
        "category": "Talleres y Actividades",
        "desc": "Carreras de velocidad, posta, salto y resistencia.",
        "icon": "fa-running",
        "content": """
        <h3>Equipo de Atletismo DMC</h3>
        <p>Desarrollo de velocidad, potencia y disciplina aeróbica para las competencias atléticas anuales.</p>
        """
    },
    {
        "path": "talleres-actividades/ajedrez.html",
        "title": "Círculo de Ajedrez Escolar",
        "category": "Talleres y Actividades",
        "desc": "Desarrollo del pensamiento lógico y la estrategia a través del deporte ciencia.",
        "icon": "fa-chess",
        "content": """
        <h3>Club de Ajedrez Manco Campino</h3>
        <p>Clases y torneos internos semanales que estimulan la concentración y el cálculo analítico en los estudiantes.</p>
        """
    },
    {
        "path": "talleres-actividades/teatro-oratoria.html",
        "title": "Taller de Teatro y Oratoria",
        "category": "Talleres y Actividades",
        "desc": "Expresión corporal, dicción, liderazgo y declamación poética.",
        "icon": "fa-theater-masks",
        "content": """
        <h3>Taller de Expresión Teatral y Oratoria</h3>
        <p>Vence el pánico escénico y cultiva la elocuencia y el dominio del discurso público en debates juveniles.</p>
        """
    },
    {
        "path": "talleres-actividades/medio-ambiente.html",
        "title": "Brigada Ecológica y Huerto Escolar",
        "category": "Talleres y Actividades",
        "desc": "Cuidado de áreas verdes, reciclaje y biohuerto institucional en Mala.",
        "icon": "fa-seedling",
        "content": """
        <h3>Brigada Ambiental y Biohuerto DMC</h3>
        <p>Sensibilización activa sobre el cambio climático, clasificación de residuos sólidos y cultivo de hortalizas nativas.</p>
        """
    },

    # 6. COMUNIDAD ESTUDIANTIL (10 páginas)
    {
        "path": "comunidad-estudiantil/index.html",
        "title": "Comunidad y Vida Estudiantil",
        "category": "Comunidad Estudiantil",
        "desc": "Organizaciones estudiantiles, participación democrática y eventos cívicos.",
        "icon": "fa-users",
        "content": """
        <h3>Participación y Liderazgo Estudiantil</h3>
        <p>Los estudiantes mancocampinos ejercen ciudadanía activa a través del Municipio Escolar, la Policía Escolar y las brigadas cívicas.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/municipio-escolar.html",
        "title": "Municipio Escolar DMC",
        "category": "Comunidad Estudiantil",
        "desc": "Elecciones democráticas, alcalde escolar y regidurías temáticas.",
        "icon": "fa-vote-yea",
        "content": """
        <h3>Municipio Escolar: Voz de los Estudiantes</h3>
        <p>Elegido mediante sufragio universal supervisado por el comité electoral escolar, gestiona proyectos de recreación, cultura y apoyo entre pares.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/policia-escolar.html",
        "title": "Policía Escolar y Brigadieres",
        "category": "Comunidad Estudiantil",
        "desc": "Orden, disciplina cívica y apoyo a la convivencia en ingresos y recreos.",
        "icon": "fa-user-shield",
        "content": """
        <h3>Cuerpo de Policía Escolar DMC</h3>
        <p>Brigadieres generales, brigadieres de aula y policías escolares juramentados con apoyo de la Comisaría de Mala.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/brigada-defensa-civil.html",
        "title": "Brigada de Defensa Civil",
        "category": "Comunidad Estudiantil",
        "desc": "Simulacros sísmicos nacionales, rutas de evacuación y primeros auxilios.",
        "icon": "fa-first-aid",
        "content": """
        <h3>Gestión del Riesgo de Desastres</h3>
        <p>Capacitación en evacuación ordenada ante sismos y tsunamis en coordinación con INDECI y el centro de salud de Mala.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/brigada-ecologica.html",
        "title": "Brigada de Cuidado Ecológico",
        "category": "Comunidad Estudiantil",
        "desc": "Vigilancia ambiental y promoción del reciclaje en los patios escolares.",
        "icon": "fa-recycle",
        "content": """
        <h3>Brigadistas Ecológicos Escolares</h3>
        <p>Líderes de aula dedicados a supervisar el ahorro de agua y la segregación de residuos plásticos y papeles en el colegio.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/defensoria-escolar.html",
        "title": "Defensoría Escolar (DESNA)",
        "category": "Comunidad Estudiantil",
        "desc": "Protección de los derechos de niños, niñas y adolescentes en el ámbito escolar.",
        "icon": "fa-hands-helping",
        "content": """
        <h3>DESNA: Defensoría Escolar Manco Campina</h3>
        <p>Canal confidencial y seguro para prevenir el acoso escolar (bullying) y proteger la integridad física y moral de los alumnos.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/juegos-florales.html",
        "title": "Juegos Florales Escolares",
        "category": "Comunidad Estudiantil",
        "desc": "Concurso nacional de pintura, fotografía, poesía y teatro del MINEDU.",
        "icon": "fa-award",
        "content": """
        <h3>Juegos Florales Nacionales</h3>
        <p>Nuestros estudiantes compiten cada año con creaciones poéticas y artísticas que celebran el Bicentenario y el orgullo maleño.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/jedpa.html",
        "title": "Juegos Escolares Deportivos (JEDPA)",
        "category": "Comunidad Estudiantil",
        "desc": "Competencias atléticas y de deportes colectivos organizadas por UGEL 08.",
        "icon": "fa-medal",
        "content": """
        <h3>JEDPA UGEL 08 Cañete</h3>
        <p>La máxima fiesta deportiva escolar donde nuestros atletas mancocampinos defienden con honor los colores de la institución.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/aniversario.html",
        "title": "Semana Jubilar del Aniversario",
        "category": "Comunidad Estudiantil",
        "desc": "Celebraciones del 15 de abril: pasacalle, serenata, desfile y festival cívico.",
        "icon": "fa-birthday-cake",
        "content": """
        <h3>15 de Abril: Aniversario de la I.E. Dionisio Manco Campos</h3>
        <p>Cada año celebramos la fundación de nuestro colegio con comparsas de danzas, feria gastronómica de Mala, concurso de escoltas y sesión solemne.</p>
        """
    },
    {
        "path": "comunidad-estudiantil/periodico-mural.html",
        "title": "Periódico Mural y Boletín Escolar",
        "category": "Comunidad Estudiantil",
        "desc": "Comunicación estudiantil, efemérides y artículos de opinión.",
        "icon": "fa-newspaper",
        "content": """
        <h3>Voz Manco Campina: Periódico Mural</h3>
        <p>Espacio informativo renovado mensualmente con investigaciones históricas, dibujos estudiantiles y fechas cívicas del calendario escolar.</p>
        """
    },

    # 7. PADRES Y APAFA (8 páginas)
    {
        "path": "padres-apafa/index.html",
        "title": "Asociación de Padres de Familia (APAFA)",
        "category": "Padres y APAFA",
        "desc": "Comunidad de familias comprometidas con la educación de sus hijos.",
        "icon": "fa-user-friends",
        "content": """
        <h3>La Familia Manco Campina Unida por el Progreso</h3>
        <p>La <strong>APAFA</strong> de la I.E. Dionisio Manco Campos colabora estrechamente con la dirección y la plana docente para el mantenimiento de la infraestructura y el bienestar de los estudiantes.</p>
        """
    },
    {
        "path": "padres-apafa/directiva-apafa.html",
        "title": "Consejo Directivo de la APAFA",
        "category": "Padres y APAFA",
        "desc": "Representantes elegidos por los padres de familia conforme a la Ley N° 28628.",
        "icon": "fa-users-cog",
        "content": """
        <h3>Directiva General de la APAFA</h3>
        <p>Presidente, vicepresidente, tesorero, secretario y vocales elegidos en asamblea general ordinaria.</p>
        """
    },
    {
        "path": "padres-apafa/escuela-padres.html",
        "title": "Escuela para Padres",
        "category": "Padres y APAFA",
        "desc": "Talleres formativos en crianza positiva, comunicación y prevención de riesgos.",
        "icon": "fa-chalkboard-teacher",
        "content": """
        <h3>Talleres de Escuela para Padres</h3>
        <p>Espacios mensuales con psicólogos invitados para orientar a las familias en la etapa de la adolescencia y el uso responsable de redes sociales.</p>
        """
    },
    {
        "path": "padres-apafa/comites-aula.html",
        "title": "Red de Comités de Aula",
        "category": "Padres y APAFA",
        "desc": "Organización de delegados de padres por cada grado y sección.",
        "icon": "fa-network-wired",
        "content": """
        <h3>Comités de Aula por Sección</h3>
        <p>Apoyo directo al docente tutor en actividades pedagógicas, mejoras del salón de clases y acompañamiento de excursiones de estudio.</p>
        """
    },
    {
        "path": "padres-apafa/reuniones-entrevistas.html",
        "title": "Horarios de Atención a Familias",
        "category": "Padres y APAFA",
        "desc": "Horas pedagógicas reservadas para dialogar con los docentes tutores.",
        "icon": "fa-handshake",
        "content": """
        <h3>Atención Personalizada a Padres de Familia</h3>
        <p>Cada docente cuenta con horas de atención semanal para informar sobre el rendimiento académico y conducta de los hijos.</p>
        """
    },
    {
        "path": "padres-apafa/convivencia-familiar.html",
        "title": "Guía de Convivencia Familiar",
        "category": "Padres y APAFA",
        "desc": "Recomendaciones para el acompañamiento emocional en el hogar.",
        "icon": "fa-home",
        "content": """
        <h3>Fortaleciendo el Vínculo Hogar - Escuela</h3>
        <p>Pautas para establecer límites con afecto, dialogar en familia y supervisar las tareas escolares con respeto.</p>
        """
    },
    {
        "path": "padres-apafa/comunicados-apafa.html",
        "title": "Comunicados Oficiales APAFA",
        "category": "Padres y APAFA",
        "desc": "Convocatorias a asambleas generales y faenas de mantenimiento comunal.",
        "icon": "fa-bullhorn",
        "content": """
        <h3>Avisos y Citaciones de la APAFA</h3>
        <p>Canal informativo sobre acuerdos de asamblea, mantenimiento de toldos y mejoras en las losas recreativas.</p>
        """
    },
    {
        "path": "padres-apafa/rendicion-cuentas.html",
        "title": "Rendición de Cuentas y Transparencia",
        "category": "Padres y APAFA",
        "desc": "Informes económicos auditados presentados a la asamblea de padres.",
        "icon": "fa-file-invoice-dollar",
        "content": """
        <h3>Transparencia Financiera en la APAFA</h3>
        <p>Publicación periódica del balance de ingresos y egresos de los aportes voluntarios de los asociados.</p>
        """
    },

    # 8. INFRAESTRUCTURA (8 páginas)
    {
        "path": "infraestructura/index.html",
        "title": "Instalaciones y Ambientes Escolares",
        "category": "Infraestructura",
        "desc": "Espacios educativos, laboratorios y áreas deportivas en Mala.",
        "icon": "fa-building",
        "content": """
        <h3>Infraestructura Educativa de la I.E. DMC</h3>
        <p>Ubicada en el Jr. Enrique Swayne s/n en Mala, la institución cuenta con pabellones de aulas, laboratorios, biblioteca y losas deportivas.</p>
        """
    },
    {
        "path": "infraestructura/aulas-ordinarias.html",
        "title": "Pabellones de Aulas Pedagógicas",
        "category": "Infraestructura",
        "desc": "Aulas ventiladas e iluminadas para el dictado de clases en ambos turnos.",
        "icon": "fa-door-open",
        "content": """
        <h3>Aulas de Clase</h3>
        <p>Espacios equipados con carpetas bipersonales, pizarras acrílicas y mobiliario adaptado para secundaria.</p>
        """
    },
    {
        "path": "infraestructura/aip-computo.html",
        "title": "Aula de Innovación Pedagógica (AIP)",
        "category": "Infraestructura",
        "desc": "Centro tecnológico con computadoras, proyector e internet de alta velocidad.",
        "icon": "fa-laptop",
        "content": """
        <h3>Aula de Innovación Pedagógica (AIP)</h3>
        <p>Laboratorio informático donde los estudiantes desarrollan proyectos de investigación y competencias digitales CNEB.</p>
        """
    },
    {
        "path": "infraestructura/laboratorios-ciencias.html",
        "title": "Laboratorio Multifuncional de Ciencias",
        "category": "Infraestructura",
        "desc": "Equipos de microscopía, reactivos y mecheros para física, química y biología.",
        "icon": "fa-vial",
        "content": """
        <h3>Laboratorio de Ciencias</h3>
        <p>Ambiente implementado con instrumental de precisión para la experimentación en Ciencias Naturales y proyectos Eureka.</p>
        """
    },
    {
        "path": "infraestructura/biblioteca.html",
        "title": "Biblioteca Escolar Dionisio Manco Campos",
        "category": "Infraestructura",
        "desc": "Colección bibliográfica de literatura, textos escolares MINEDU y sala de lectura.",
        "icon": "fa-book-reader",
        "content": """
        <h3>Biblioteca y Sala de Lectura</h3>
        <p>Espacio silencioso para la investigación bibliográfica y el fomento de la lectura recreativa de estudiantes y profesores.</p>
        """
    },
    {
        "path": "infraestructura/losas-deportivas.html",
        "title": "Losas Polideportivas y Patios",
        "category": "Infraestructura",
        "desc": "Canchas múltiples para fútbol sala, básquetbol, vóley y recreo.",
        "icon": "fa-basketball-ball",
        "content": """
        <h3>Espacios Deportivos y Recreativos</h3>
        <p>Losas con arcos y tableros reglamentarios donde se disputan los campeonatos inter-secciones y entrenan las selecciones.</p>
        """
    },
    {
        "path": "infraestructura/auditorio-civico.html",
        "title": "Patio de Honor y Estrado Cívico",
        "category": "Infraestructura",
        "desc": "Escenario central de las formaciones de los días lunes y actuaciones cívicas.",
        "icon": "fa-flag",
        "content": """
        <h3>Patio de Honor Central</h3>
        <p>Centro de los honores a los símbolos patrios, izamiento del Pabellón Nacional y premiaciones estudiantiles.</p>
        """
    },
    {
        "path": "infraestructura/reconstruccion-gestion.html",
        "title": "Proyecto de Reconstrucción y Modernización",
        "category": "Infraestructura",
        "desc": "Gestiones institucionales ante el PRONIED, el GORE Lima y el MINEDU.",
        "icon": "fa-hard-hat",
        "content": """
        <h3>Hacia la Nueva Infraestructura Emblemática</h3>
        <p>Directivos, docentes y la comunidad de Mala continúan las gestiones ante el Gobierno Regional de Lima y el PRONIED para la construcción del nuevo y moderno complejo educativo que merece el alma máter de Mala.</p>
        """
    },

    # 9. ADMISIÓN Y MATRÍCULA (8 páginas)
    {
        "path": "admision-matricula/index.html",
        "title": "Portal de Admisión y Matrícula",
        "category": "Admisión y Matrícula",
        "desc": "Información centralizada del proceso de matrícula escolar y vacantes.",
        "icon": "fa-user-plus",
        "content": """
        <h3>Matrícula Gratuita en la I.E. Dionisio Manco Campos</h3>
        <p>Garantizamos el acceso universal y gratuito a la educación secundaria pública en estricto cumplimiento de las normas del MINEDU.</p>
        """
    },
    {
        "path": "admision-matricula/cronograma.html",
        "title": "Cronograma Oficial de Matrícula",
        "category": "Admisión y Matrícula",
        "desc": "Fechas clave de publicación de vacantes, registro y ratificación.",
        "icon": "fa-calendar-alt",
        "content": """
        <h3>Calendario del Proceso de Matrícula</h3>
        <p>Publicación de vacantes en diciembre, recepción de solicitudes en enero y emisión de actas de matrícula en febrero y marzo.</p>
        """
    },
    {
        "path": "admision-matricula/requisitos.html",
        "title": "Requisitos Documentarios MINEDU",
        "category": "Admisión y Matrícula",
        "desc": "Ficha SIAGIE, copias de DNI y certificados oficiales necesarios.",
        "icon": "fa-folder-open",
        "content": """
        <h3>Documentación Requerida para Matrícula</h3>
        <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li>Ficha Única de Matrícula (FUM) expedida por el sistema SIAGIE.</li>
            <li>Copia legible del DNI del estudiante y del apoderado legal.</li>
            <li>Certificado oficial de estudios que acredite haber culminado el grado previo.</li>
            <li>Partida de nacimiento (para nuevos ingresos a la institución).</li>
        </ul>
        """
    },
    {
        "path": "admision-matricula/vacantes.html",
        "title": "Disponibilidad de Vacantes",
        "category": "Admisión y Matrícula",
        "desc": "Distribución de vacantes por grado para el 1° a 5° de secundaria.",
        "icon": "fa-chair",
        "content": """
        <h3>Cuadro de Vacantes Disponibles</h3>
        <p>Las vacantes se asignan priorizando a estudiantes con necesidades educativas especiales (NEE), hermanos en la institución y cercanía domiciliaria.</p>
        """
    },
    {
        "path": "admision-matricula/traslados.html",
        "title": "Procedimiento de Traslados",
        "category": "Admisión y Matrícula",
        "desc": "Pasos para trasladar a un estudiante desde otra escuela pública o privada.",
        "icon": "fa-exchange-alt",
        "content": """
        <h3>Traslados de Matrícula a la I.E. DMC</h3>
        <p>El apoderado solicita la constancia de vacante en nuestra mesa de partes, presenta la resolución de traslado del colegio de origen y actualiza la matrícula en SIAGIE.</p>
        """
    },
    {
        "path": "admision-matricula/siagie.html",
        "title": "Guía de la Plataforma SIAGIE",
        "category": "Admisión y Matrícula",
        "desc": "Acceso al Sistema de Información de Apoyo a la Gestión de la Institución Educativa.",
        "icon": "fa-server",
        "content": """
        <h3>SIAGIE: Sistema Oficial de Matrícula y Notas</h3>
        <p>Todas las notas, actas oficiales y certificados son registrados en la plataforma centralizada del Ministerio de Educación.</p>
        """
    },
    {
        "path": "admision-matricula/preguntas-frecuentes.html",
        "title": "Preguntas Frecuentes de Familias (FAQ)",
        "category": "Admisión y Matrícula",
        "desc": "Respuestas directas a las dudas comunes sobre el proceso educativo.",
        "icon": "fa-question-circle",
        "content": """
        <h3>Dudas Frecuentes sobre Matrícula</h3>
        <p>Encuentra respuestas inmediatas sobre costos (matrícula 100% gratuita), uniformes, útiles escolares y turnos de clase.</p>
        """
    },
    {
        "path": "admision-matricula/formulario-prematricula.html",
        "title": "Formulario de Pre-Matrícula en Línea",
        "category": "Admisión y Matrícula",
        "desc": "Registro virtual de solicitudes para agilizar la atención en secretaría.",
        "icon": "fa-file-signature",
        "content": """
        <h3>Registro de Solicitud de Vacante</h3>
        <p>Completa el formulario en línea para pre-registrar los datos del estudiante. La secretaría revisará la documentación y se comunicará vía WhatsApp o llamada telefónica.</p>
        """
    },

    # 10. TRÁMITES Y SERVICIOS (8 páginas)
    {
        "path": "tramites-servicios/index.html",
        "title": "Servicios al Ciudadano y Mesa de Partes",
        "category": "Trámites y Servicios",
        "desc": "Gestión de expedientes administrativos, certificados y constancias.",
        "icon": "fa-concierge-bell",
        "content": """
        <h3>Atención al Usuario en la I.E. DMC</h3>
        <p>Ponemos a disposición de la comunidad maleña nuestra Mesa de Partes Virtual y presencial para facilitar la tramitación de documentos escolares.</p>
        """
    },
    {
        "path": "tramites-servicios/mesa-de-partes.html",
        "title": "Mesa de Partes Virtual",
        "category": "Trámites y Servicios",
        "desc": "Ingreso digital de solicitudes, cartas y expedientes las 24 horas del día.",
        "icon": "fa-file-invoice",
        "content": """
        <h3>Mesa de Partes Virtual Oficial</h3>
        <p>Registra tus solicitudes con código de seguimiento instantáneo para emisión de documentos oficiales o peticiones a la Dirección.</p>
        """
    },
    {
        "path": "tramites-servicios/certificados-estudio.html",
        "title": "Certificados Oficiales de Estudios",
        "category": "Trámites y Servicios",
        "desc": "Requisitos y plazos para la emisión de certificados de secundaria y egresados.",
        "icon": "fa-certificate",
        "content": """
        <h3>Certificado Oficial de Estudios</h3>
        <p>Documento oficial emitido mediante la plataforma de certificados del MINEDU con firma digital y código de verificación QR.</p>
        """
    },
    {
        "path": "tramites-servicios/constancias-matricula.html",
        "title": "Constancias de Matrícula y Estudios",
        "category": "Trámites y Servicios",
        "desc": "Documento acreditativo de condición de estudiante activo en el año lectivo.",
        "icon": "fa-file-contract",
        "content": """
        <h3>Constancia de Matrícula Escolar</h3>
        <p>Emisión rápida de constancias para trámites de programas sociales (Pensión 65, Juntos), seguro médico o convenios laborales.</p>
        """
    },
    {
        "path": "tramites-servicios/rectificacion-datos.html",
        "title": "Rectificación de Nombres y Apellidos",
        "category": "Trámites y Servicios",
        "desc": "Procedimiento de rectificación en actas oficiales por mandato de RENIEC.",
        "icon": "fa-user-edit",
        "content": """
        <h3>Rectificación de Datos en Actas</h3>
        <p>Procedimiento administrativo para corregir errores ortográficos en actas consolidadas históricas conforme a partida rectificada.</p>
        """
    },
    {
        "path": "tramites-servicios/horarios-atencion.html",
        "title": "Horarios de Secretaría y Dirección",
        "category": "Trámites y Servicios",
        "desc": "Horarios de atención presencial al público en Jr. Enrique Swayne s/n.",
        "icon": "fa-business-time",
        "content": """
        <h3>Atención al Público en Secretaría</h3>
        <p>Lunes a Viernes de <strong>8:00 a.m. a 3:00 p.m.</strong> en las oficinas administrativas del colegio en Mala.</p>
        """
    },
    {
        "path": "tramites-servicios/tupa.html",
        "title": "Texto Único de Procedimientos (TUPA)",
        "category": "Trámites y Servicios",
        "desc": "Relación de trámites, plazos y requisitos conforme a la normativa de UGEL 08.",
        "icon": "fa-list-ol",
        "content": """
        <h3>TUPA Institucional</h3>
        <p>Catálogo transparente de todos los procedimientos administrativos, bases legales y tiempos máximos de respuesta de la institución.</p>
        """
    },
    {
        "path": "tramites-servicios/libro-reclamaciones.html",
        "title": "Libro de Reclamaciones Virtual",
        "category": "Trámites y Servicios",
        "desc": "Canal oficial para la formulación de quejas o reclamos ciudadanos.",
        "icon": "fa-book-open",
        "content": """
        <h3>Libro de Reclamaciones Virtual</h3>
        <p>Mecanismo de atención y resolución de quejas ciudadanas en cumplimiento del D.S. N° 042-2011-PCM para garantizar la calidad del servicio educativo.</p>
        """
    },

    # 11. NOTICIAS Y EVENTOS (7 páginas)
    {
        "path": "noticias-eventos/index.html",
        "title": "Centro de Noticias y Comunicados",
        "category": "Noticias y Eventos",
        "desc": "Información de actualidad, circulares directivas y actividades de la I.E. DMC.",
        "icon": "fa-newspaper",
        "content": """
        <h3>Actualidad Manco Campina</h3>
        <p>Mantente informado sobre las últimas novedades escolares, directivas de UGEL 08, celebraciones y comunicados de la I.E. Dionisio Manco Campos.</p>
        """
    },
    {
        "path": "noticias-eventos/calendario-civico.html",
        "title": "Calendario Cívico Escolar",
        "category": "Noticias y Eventos",
        "desc": "Fechas cívicas nacionales, aniversarios maleños y efemérides patrias.",
        "icon": "fa-calendar",
        "content": """
        <h3>Calendario Cívico Anual</h3>
        <p>Conmemoración de las grandes gestas del Perú: Día de la Bandera, Fiestas Patrias, Batalla de Junín, Combate de Angamos y Aniversario de Mala.</p>
        """
    },
    {
        "path": "noticias-eventos/comunicados-direccion.html",
        "title": "Comunicados de la Dirección",
        "category": "Noticias y Eventos",
        "desc": "Disposiciones oficiales sobre jornadas pedagógicas, feriados y evaluaciones.",
        "icon": "fa-scroll",
        "content": """
        <h3>Circulares y Comunicados Oficiales</h3>
        <p>Avisos dirigidos a toda la comunidad educativa de Mala con disposiciones emanadas por el MINEDU y la Dirección del plantel.</p>
        """
    },
    {
        "path": "noticias-eventos/galeria-aniversario.html",
        "title": "Galería de Aniversario Institucional",
        "category": "Noticias y Eventos",
        "desc": "Registros gráficos de las celebraciones del 15 de abril en Mala.",
        "icon": "fa-images",
        "content": """
        <h3>Recuerdos de Nuestro Aniversario</h3>
        <p>Fotografías y semblanzas de las festividades por los 60+ años de fundación de la I.E. Dionisio Manco Campos con pasacalles y comparsas.</p>
        """
    },
    {
        "path": "noticias-eventos/galeria-desfiles.html",
        "title": "Galería de Desfiles y Honores Patrios",
        "category": "Noticias y Eventos",
        "desc": "Participación de la escolta, batallones y banda en la Plaza de Mala.",
        "icon": "fa-camera",
        "content": """
        <h3>Civismo Manco Campino en la Plaza de Mala</h3>
        <p>Imágenes del gallardo paso de nuestros batallones escolares y banda de guerra en los desfiles de fiestas patrias en Cañete.</p>
        """
    },
    {
        "path": "noticias-eventos/convenios-alianzas.html",
        "title": "Convenios y Alianzas Estratégicas",
        "category": "Noticias y Eventos",
        "desc": "Cooperación interinstitucional con la Municipalidad de Mala, Policía y Salud.",
        "icon": "fa-handshake",
        "content": """
        <h3>Alianzas por la Juventud de Mala</h3>
        <p>Convenios con la Municipalidad Distrital de Mala, el Centro de Salud, la PNP y empresas del valle para programas de salud preventiva y becas.</p>
        """
    },
    {
        "path": "noticias-eventos/exalumnos.html",
        "title": "Asociación de Exalumnos Manco Campinos",
        "category": "Noticias y Eventos",
        "desc": "Red de egresados de promociones de 1962 al presente en Mala y el mundo.",
        "icon": "fa-user-tie",
        "content": """
        <h3>Egresados DMC: Orgullo de Nuestra Tierra</h3>
        <p>Espacio de reencuentro de las promociones egresadas que hoy destacan como ingenieros, médicos, educadores, empresarios y líderes cívicos de Mala.</p>
        """
    }
]

def get_depth_prefix(path):
    parts = path.split('/')
    depth = len(parts) - 1
    return "../" * depth if depth > 0 else "./"

def generate_header(prefix, current_path):
    return f"""
  <!-- TOP BAR INFORMATIVA -->
  <div class="top-announcement text-white py-2 px-4 sm:px-8 text-xs sm:text-sm font-medium">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-2">
      <div class="flex flex-wrap items-center justify-center md:justify-start gap-4">
        <span><i class="fas fa-school text-yellow-400 mr-1.5"></i> UGEL N° 08 Cañete &bull; Cód. Modular: <strong>0286385</strong></span>
        <span class="hidden sm:inline text-slate-300">|</span>
        <span><i class="fas fa-map-marker-alt text-yellow-400 mr-1.5"></i> Jr. Enrique Swayne s/n, Mala - Cañete</span>
      </div>
      <div class="flex items-center gap-4">
        <a href="tel:013396215" class="hover:text-yellow-300 transition-colors"><i class="fas fa-phone-alt text-yellow-400 mr-1"></i> (01) 339-6215</a>
        <span class="text-slate-300">|</span>
        <a href="https://www.facebook.com/iepdmc" target="_blank" rel="noopener noreferrer" class="hover:text-yellow-300 transition-colors">
          <i class="fab fa-facebook-f text-yellow-400"></i> Facebook Oficial
        </a>
      </div>
    </div>
  </div>

  <!-- HEADER NAVEGACIÓN PRINCIPAL -->
  <header id="main-header" class="sticky top-0 z-50 glass-nav transition-all duration-300 py-3 px-4 sm:px-8 shadow-md">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      
      <!-- LOGO INSTITUCIONAL -->
      <a href="{prefix}index.html" class="flex items-center gap-3 group">
        <img src="{prefix}img/escudo-dmc.svg" alt="Escudo DMC" class="h-11 sm:h-12 w-auto drop-shadow-md group-hover:scale-105 transition-transform">
        <div class="flex flex-col">
          <span class="font-heading font-black text-base sm:text-lg text-white tracking-wide leading-tight">
            I.E. DIONISIO MANCO CAMPOS
          </span>
          <span class="text-[10px] sm:text-xs font-semibold text-yellow-400 tracking-wider uppercase">
            Nivel Secundaria &bull; Mala, Cañete
          </span>
        </div>
      </a>

      <!-- ENLACES DESKTOP CON MEGA-DROPDOWNS -->
      <nav class="hidden lg:flex items-center gap-5 xl:gap-6 font-medium text-xs xl:text-sm text-slate-200">
        <a href="{prefix}index.html" class="nav-link hover:text-yellow-400 py-1">Inicio</a>
        <a href="{prefix}institucional/index.html" class="nav-link hover:text-yellow-400 py-1">Institucional</a>
        <a href="{prefix}grados/index.html" class="nav-link hover:text-yellow-400 py-1">Grados</a>
        <a href="{prefix}areas-curriculares/index.html" class="nav-link hover:text-yellow-400 py-1">Áreas</a>
        <a href="{prefix}ceba/index.html" class="nav-link hover:text-yellow-400 py-1">CEBA</a>
        <a href="{prefix}talleres-actividades/index.html" class="nav-link hover:text-yellow-400 py-1">Talleres</a>
        <a href="{prefix}admision-matricula/index.html" class="nav-link hover:text-yellow-400 py-1">Admisión</a>
        <a href="{prefix}tramites-servicios/index.html" class="nav-link hover:text-yellow-400 py-1">Trámites</a>
      </nav>

      <!-- BOTÓN CTA -->
      <div class="hidden lg:flex items-center gap-3">
        <a href="{prefix}tramites-servicios/mesa-de-partes.html" class="inline-flex items-center gap-1.5 bg-gradient-to-r from-yellow-500 to-yellow-600 hover:from-yellow-400 hover:to-yellow-500 text-slate-950 font-bold px-3.5 py-2 rounded-lg text-xs uppercase tracking-wider shadow-lg transition-all hover:-translate-y-0.5">
          <i class="fas fa-file-invoice"></i> Mesa de Partes
        </a>
      </div>

      <!-- BOTÓN HAMBURGUESA MÓVIL -->
      <button id="mobile-menu-btn" class="lg:hidden text-white hover:text-yellow-400 text-2xl p-2 focus:outline-none" aria-label="Abrir Menú">
        <i class="fas fa-bars"></i>
      </button>

    </div>
  </header>

  <!-- MENÚ LATERAL MÓVIL (DRAWER) -->
  <div id="mobile-backdrop" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 hidden transition-opacity"></div>
  <div id="mobile-menu" class="fixed top-0 right-0 h-full w-4/5 max-w-sm bg-dmcNavy-900 border-l border-yellow-500/30 z-50 transform translate-x-full transition-transform duration-300 p-6 flex flex-col justify-between overflow-y-auto">
    <div>
      <div class="flex items-center justify-between pb-5 border-b border-slate-700">
        <div class="flex items-center gap-2">
          <img src="{prefix}img/escudo-dmc.svg" alt="Escudo DMC" class="h-9 w-auto">
          <span class="font-heading font-black text-white text-sm">I.E. DMC MALA</span>
        </div>
        <button id="mobile-menu-close" class="text-slate-400 hover:text-white text-2xl p-1" aria-label="Cerrar Menú">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <nav class="flex flex-col gap-2.5 mt-5 text-slate-200 text-xs font-semibold">
        <a href="{prefix}index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-home w-5 text-yellow-400"></i> Inicio</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}institucional/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-landmark w-5 text-yellow-400"></i> Institucional</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}grados/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-chalkboard-teacher w-5 text-yellow-400"></i> Grados y Secciones</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}areas-curriculares/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-book w-5 text-yellow-400"></i> Áreas Curriculares</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}ceba/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-user-graduate w-5 text-yellow-400"></i> Modalidad CEBA</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}talleres-actividades/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-palette w-5 text-yellow-400"></i> Talleres & Deportes</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}comunidad-estudiantil/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-users w-5 text-yellow-400"></i> Vida Estudiantil</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}padres-apafa/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-user-friends w-5 text-yellow-400"></i> Familias & APAFA</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}infraestructura/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-building w-5 text-yellow-400"></i> Infraestructura</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}admision-matricula/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-user-plus w-5 text-yellow-400"></i> Admisión & Matrícula</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}tramites-servicios/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-concierge-bell w-5 text-yellow-400"></i> Trámites & Servicios</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
        <a href="{prefix}noticias-eventos/index.html" class="hover:text-yellow-400 py-2 border-b border-slate-800 flex items-center justify-between">
          <span><i class="fas fa-newspaper w-5 text-yellow-400"></i> Noticias & Eventos</span>
          <i class="fas fa-chevron-right text-[10px]"></i>
        </a>
      </nav>
    </div>
    <div class="pt-5 border-t border-slate-800 text-center">
      <a href="{prefix}tramites-servicios/mesa-de-partes.html" class="block w-full bg-yellow-500 text-slate-950 font-bold py-2.5 rounded-lg text-xs uppercase shadow-md">
        <i class="fas fa-file-invoice mr-1"></i> Mesa de Partes Virtual
      </a>
    </div>
  </div>
    """

def generate_footer(prefix):
    return f"""
  <!-- FOOTER COMPLETO INSTITUCIONAL -->
  <footer class="bg-dmcNavy-900 text-slate-300 border-t border-yellow-500/20 pt-16 pb-8 px-4 sm:px-8 mt-auto">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 pb-12 border-b border-slate-800">
      
      <!-- Columna 1 -->
      <div class="lg:col-span-4 space-y-4">
        <div class="flex items-center gap-3">
          <img src="{prefix}img/escudo-dmc.svg" alt="Escudo DMC" class="h-12 w-auto">
          <div>
            <span class="font-heading font-black text-base text-white block leading-tight">I.E. DIONISIO MANCO CAMPOS</span>
            <span class="text-[11px] text-yellow-400 font-semibold uppercase">Alma Máter de Mala &bull; Fundado en 1962</span>
          </div>
        </div>
        <p class="text-xs text-slate-400 leading-relaxed">
          Institución educativa pública de educación secundaria (EBR y CEBA) en Mala, Cañete. Más de 60 años formando con honor bajo el lema <em>"Patria, Estudio y Disciplina"</em>.
        </p>
        <div class="text-xs text-slate-400 space-y-1">
          <p><strong class="text-slate-300">Cód. Modular Secundaria:</strong> 0286385</p>
          <p><strong class="text-slate-300">Cód. Modular CEBA:</strong> 0285676</p>
          <p><strong class="text-slate-300">Cód. Local:</strong> 353596 &bull; UGEL N° 08 Cañete</p>
        </div>
      </div>

      <!-- Columna 2: Ecosistema de Navegación -->
      <div class="lg:col-span-3 space-y-3">
        <h4 class="font-heading font-bold text-white text-xs uppercase tracking-wider border-l-2 border-yellow-400 pl-2">
          Ecosistema Institucional
        </h4>
        <ul class="text-xs space-y-1.5 text-slate-400">
          <li><a href="{prefix}institucional/index.html" class="hover:text-yellow-400">&bull; Portal Institucional & Historia</a></li>
          <li><a href="{prefix}grados/index.html" class="hover:text-yellow-400">&bull; Grados y Secciones de Secundaria</a></li>
          <li><a href="{prefix}areas-curriculares/index.html" class="hover:text-yellow-400">&bull; Plan Curricular CNEB MINEDU</a></li>
          <li><a href="{prefix}ceba/index.html" class="hover:text-yellow-400">&bull; Modalidad CEBA para Adultos</a></li>
          <li><a href="{prefix}talleres-actividades/index.html" class="hover:text-yellow-400">&bull; Talleres, Deportes y Banda</a></li>
          <li><a href="{prefix}comunidad-estudiantil/index.html" class="hover:text-yellow-400">&bull; Municipio Escolar y Brigadas</a></li>
        </ul>
      </div>

      <!-- Columna 3: Servicios y Trámites -->
      <div class="lg:col-span-2 space-y-3">
        <h4 class="font-heading font-bold text-white text-xs uppercase tracking-wider border-l-2 border-yellow-400 pl-2">
          Servicios y Gestión
        </h4>
        <ul class="text-xs space-y-1.5 text-slate-400">
          <li><a href="{prefix}admision-matricula/index.html" class="hover:text-yellow-400">&bull; Admisión & Vacantes</a></li>
          <li><a href="{prefix}tramites-servicios/mesa-de-partes.html" class="hover:text-yellow-400">&bull; Mesa de Partes Virtual</a></li>
          <li><a href="{prefix}tramites-servicios/certificados-estudio.html" class="hover:text-yellow-400">&bull; Certificados de Estudio</a></li>
          <li><a href="{prefix}padres-apafa/index.html" class="hover:text-yellow-400">&bull; Asociación APAFA</a></li>
          <li><a href="{prefix}infraestructura/index.html" class="hover:text-yellow-400">&bull; Ambientes y Aulas</a></li>
          <li><a href="{prefix}noticias-eventos/index.html" class="hover:text-yellow-400">&bull; Noticias & Calendario</a></li>
        </ul>
      </div>

      <!-- Columna 4: Ubicación y Contacto -->
      <div class="lg:col-span-3 space-y-3">
        <h4 class="font-heading font-bold text-white text-xs uppercase tracking-wider border-l-2 border-yellow-400 pl-2">
          Atención al Ciudadano
        </h4>
        <p class="text-xs text-slate-400"><i class="fas fa-map-marker-alt text-yellow-400 mr-1.5"></i> Jr. Enrique Swayne s/n, Mala, Cañete, Lima.</p>
        <p class="text-xs text-slate-400"><i class="fas fa-phone-alt text-yellow-400 mr-1.5"></i> Central: (01) 339-6215 / (01) 301-7765</p>
        <p class="text-xs text-slate-400"><i class="fas fa-clock text-yellow-400 mr-1.5"></i> Horario: Lun - Vie: 8:00 a.m. - 3:00 p.m.</p>
        <div class="pt-2 flex items-center gap-3">
          <a href="https://www.facebook.com/iepdmc" target="_blank" rel="noopener noreferrer" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-blue-600 text-white flex items-center justify-center transition-colors">
            <i class="fab fa-facebook-f text-xs"></i>
          </a>
          <a href="https://wa.me/51939621500" target="_blank" rel="noopener noreferrer" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-emerald-600 text-white flex items-center justify-center transition-colors">
            <i class="fab fa-whatsapp text-xs"></i>
          </a>
          <a href="{prefix}tramites-servicios/mesa-de-partes.html" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-yellow-500 hover:text-slate-950 text-white flex items-center justify-center transition-colors">
            <i class="fas fa-envelope text-xs"></i>
          </a>
        </div>
      </div>

    </div>

    <!-- Sub-footer copyright -->
    <div class="max-w-7xl mx-auto pt-6 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
      <p>&copy; 2026 I.E. Dionisio Manco Campos - Mala, Cañete. Alma Máter de la Secundaria.</p>
      <div class="flex items-center gap-3">
        <a href="{prefix}institucional/himno.html" class="hover:text-slate-300">Himno Oficial</a>
        <span>&bull;</span>
        <a href="{prefix}tramites-servicios/libro-reclamaciones.html" class="hover:text-slate-300">Libro de Reclamaciones</a>
        <span>&bull;</span>
        <a href="{prefix}README.md" class="hover:text-slate-300">Repositorio</a>
      </div>
    </div>
  </footer>

  <!-- BOTÓN FLOTANTE WHATSAPP -->
  <a href="https://wa.me/51939621500?text=Hola,%20solicito%20información%20sobre%20la%20I.E.%20Dionisio%20Manco%20Campos%20de%20Mala" 
     target="_blank" 
     rel="noopener noreferrer" 
     class="fixed bottom-6 right-6 z-40 btn-whatsapp text-white w-14 h-14 rounded-full flex items-center justify-center text-3xl shadow-2xl" 
     aria-label="WhatsApp Institucional">
    <i class="fab fa-whatsapp"></i>
  </a>

  <!-- BOTÓN VOLVER ARRIBA -->
  <button id="btn-scroll-top" 
          class="fixed bottom-24 right-7 z-40 btn-scroll-top text-yellow-400 w-11 h-11 rounded-full flex items-center justify-center text-lg shadow-xl opacity-0 pointer-events-none transition-all duration-300"
          aria-label="Volver arriba">
    <i class="fas fa-chevron-up"></i>
  </button>
    """

def build_page(page_def):
    target_rel = page_def["path"]
    target_abs = os.path.join(BASE_DIR, target_rel.replace('/', os.sep))
    os.makedirs(os.path.dirname(target_abs), exist_ok=True)
    
    prefix = get_depth_prefix(target_rel)
    title = page_def["title"]
    category = page_def["category"]
    desc = page_def["desc"]
    icon = page_def["icon"]
    content = page_def["content"]

    header_html = generate_header(prefix, target_rel)
    footer_html = generate_footer(prefix)

    html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | I.E. Dionisio Manco Campos - Mala, Cañete</title>
  <meta name="description" content="{desc}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{title} | I.E. Dionisio Manco Campos">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{prefix}img/escudo-dmc.svg">
  <meta property="og:type" content="article">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="{prefix}img/favicon.svg">
  <link rel="shortcut icon" href="{prefix}img/favicon.svg" type="image/x-icon">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            dmcNavy: {{ 900: '#091929', 800: '#0f2942', 700: '#173d63', 600: '#1e4b7a' }},
            dmcGold: {{ 300: '#fef08a', 400: '#fde047', 500: '#eab308', 600: '#ca8a04', 700: '#a16207' }},
          }},
          fontFamily: {{
            heading: ['Outfit', 'Montserrat', 'sans-serif'],
            sans: ['Inter', 'Segoe UI', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>

  <!-- Font Awesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <link rel="stylesheet" href="{prefix}styles/colegio.css">
</head>

<body class="bg-slate-50 text-slate-800 antialiased flex flex-col min-h-screen">

{header_html}

  <!-- SUBPAGE HERO BANNER -->
  <section class="hero-subpage text-white py-14 sm:py-20 px-4 sm:px-8 relative text-center">
    <div class="max-w-4xl mx-auto space-y-3">
      <div class="inline-flex items-center gap-2 bg-yellow-500/20 text-yellow-300 px-3.5 py-1 rounded-full text-xs font-bold uppercase tracking-widest border border-yellow-500/30">
        <i class="fas {icon}"></i> {category} &bull; I.E. Dionisio Manco Campos
      </div>
      <h1 class="font-heading font-black text-2xl sm:text-4xl text-white">{title}</h1>
      <p class="text-slate-300 text-xs sm:text-sm max-w-2xl mx-auto">{desc}</p>
    </div>
  </section>

  <!-- BREADCRUMBS -->
  <div class="bg-white border-b border-slate-200 py-2.5 px-4 sm:px-8 text-xs text-slate-500 font-medium">
    <div class="max-w-7xl mx-auto flex items-center gap-2 flex-wrap">
      <a href="{prefix}index.html" class="hover:text-yellow-600"><i class="fas fa-home"></i> Inicio</a>
      <span>/</span>
      <span class="text-slate-400">{category}</span>
      <span>/</span>
      <span class="text-dmcNavy-900 font-bold">{title}</span>
    </div>
  </div>

  <!-- MAIN CONTENT CONTAINER -->
  <main class="py-12 px-4 sm:px-8 max-w-7xl mx-auto w-full flex-1">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
      
      <!-- ARTÍCULO PRINCIPAL -->
      <article class="lg:col-span-8 bg-white p-6 sm:p-10 rounded-3xl border border-slate-200 shadow-sm space-y-6 text-sm leading-relaxed text-slate-700">
        {content}
        
        <div class="pt-6 border-t border-slate-100 flex flex-wrap items-center justify-between gap-4 text-xs">
          <div class="flex items-center gap-2 text-slate-400">
            <i class="fas fa-shield-alt text-yellow-500"></i>
            <span>Información Institucional Oficial &bull; Mala, Cañete</span>
          </div>
          <a href="{prefix}tramites-servicios/mesa-de-partes.html" class="font-bold text-dmcNavy-900 hover:text-yellow-600 transition-colors">
            ¿Consultas sobre este tema? Ir a Mesa de Partes &rarr;
          </a>
        </div>
      </article>

      <!-- SIDEBAR COMPLEMENTARIO -->
      <aside class="lg:col-span-4 space-y-6">
        
        <!-- Tarjeta Rápida -->
        <div class="bg-dmcNavy-900 text-white p-6 rounded-3xl border border-yellow-500/30 shadow-lg text-center space-y-4">
          <img src="{prefix}img/escudo-dmc.svg" alt="Escudo DMC" class="h-20 mx-auto drop-shadow-md">
          <div>
            <h4 class="font-heading font-black text-sm text-yellow-400">I.E. DIONISIO MANCO CAMPOS</h4>
            <p class="text-[11px] text-slate-300">Alma Máter de Mala &bull; UGEL 08 Cañete</p>
          </div>
          <div class="text-[11px] bg-slate-950 p-2.5 rounded-xl font-bold tracking-wider text-slate-200">
            "PATRIA &bull; ESTUDIO &bull; DISCIPLINA"
          </div>
          <a href="{prefix}admision-matricula/index.html" class="block w-full bg-yellow-500 hover:bg-yellow-400 text-slate-950 font-bold py-2 rounded-xl text-xs uppercase transition-colors">
            Matrícula y Vacantes
          </a>
        </div>

        <!-- Enlaces Rápidos de la Categoría -->
        <div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-3">
          <h4 class="font-heading font-bold text-dmcNavy-900 text-xs uppercase tracking-wider border-l-2 border-yellow-500 pl-2">
            Módulos Relacionados
          </h4>
          <ul class="text-xs space-y-2 text-slate-600">
            <li><a href="{prefix}institucional/historia.html" class="hover:text-yellow-600 flex items-center justify-between"><span>&bull; Historia desde 1962</span> <i class="fas fa-chevron-right text-[10px]"></i></a></li>
            <li><a href="{prefix}grados/index.html" class="hover:text-yellow-600 flex items-center justify-between"><span>&bull; Grados de 1° a 5°</span> <i class="fas fa-chevron-right text-[10px]"></i></a></li>
            <li><a href="{prefix}areas-curriculares/index.html" class="hover:text-yellow-600 flex items-center justify-between"><span>&bull; Áreas Curriculares</span> <i class="fas fa-chevron-right text-[10px]"></i></a></li>
            <li><a href="{prefix}talleres-actividades/index.html" class="hover:text-yellow-600 flex items-center justify-between"><span>&bull; Talleres y Deportes</span> <i class="fas fa-chevron-right text-[10px]"></i></a></li>
            <li><a href="{prefix}ceba/index.html" class="hover:text-yellow-600 flex items-center justify-between"><span>&bull; Modalidad CEBA</span> <i class="fas fa-chevron-right text-[10px]"></i></a></li>
            <li><a href="{prefix}tramites-servicios/mesa-de-partes.html" class="hover:text-yellow-600 flex items-center justify-between"><span>&bull; Trámite Documentario</span> <i class="fas fa-chevron-right text-[10px]"></i></a></li>
          </ul>
        </div>

        <!-- Contacto Directo -->
        <div class="bg-yellow-50 border border-yellow-200 p-5 rounded-2xl text-xs text-yellow-950 space-y-2">
          <h4 class="font-bold font-heading text-sm text-yellow-900"><i class="fas fa-phone-alt text-yellow-700 mr-1.5"></i> Contáctanos en Mala</h4>
          <p>Jr. Enrique Swayne s/n, Mala, Cañete.</p>
          <p><strong>Teléfono:</strong> (01) 339-6215 / (01) 301-7765</p>
        </div>

      </aside>

    </div>
  </main>

{footer_html}

  <script src="{prefix}js/app.js"></script>
</body>
</html>
"""
    with open(target_abs, "w", encoding="utf-8") as f:
        f.write(html)
    return target_rel

def main():
    count = 0
    for p in pages_data:
        res = build_page(p)
        count += 1
        print(f"[{count}] Generada: {res}")
    print(f"\n¡Éxito! Se han generado {count} páginas .html estructuradas en subcarpetas temáticas.")

if __name__ == "__main__":
    main()
