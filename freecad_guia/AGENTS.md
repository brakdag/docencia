# Guía de Trabajos Prácticos: Instrucciones para AI

## 2. Estructura y Estándares del Documento

- Clase: `book`
- Tamaño: A4
- Estructura de archivos:
  - `main.tex`: Archivo raíz, incluye índice, introducción, capítulos y bibliografía.
  - `/styles/`: Carpeta para archivos `.sty` específicos del proyecto.
  - `/chapters/`: Carpeta para los archivos de los capítulos.
  - `/bib/`: Carpeta para archivo `.bib` de bibliografía.
- **Uso de activos compartidos:** Utilizar siempre los recursos ubicados en `../common/` para mantener la consistencia institucional (ej: `../common/sty/iramA4.sty` para formato IRAM, `../common/img/` para logos).
- Extensión total: 60-120 páginas.

## 3. Buenas Prácticas de Código LaTeX

- **Longitud de línea:** Ninguna línea de código o texto en archivos `.tex`, `.sty` o `.bib` debe superar los **80 caracteres**.
- **Herramienta de formateo:** Se debe utilizar `latexindent` periódicamente para asegurar el cumplimiento de esta norma y una indentación consistente.

## 3. Contenido General

- Público objetivo: Estudiantes de secundaria (13-18 años).
- Bibliografía: Basada en fuentes oficiales, libros académicos, normas técnicas (preferentemente argentinas/españolas).

## 4. Estructura de Capítulos

Cada capítulo debe seguir obligatoriamente esta estructura:

### D. Búsqueda e Inserción de Activos Gráficos (Imágenes)

- **Análisis de contexto:** Antes de buscar una imagen, el agente DEBE leer el texto del capítulo correspondiente para extraer el concepto, herramienta o temática principal.
- **Prohibición de Placeholders:** Está **ESTRICTAMENTE PROHIBIDO** utilizar imágenes de muestra, bloques de un solo color (solid colors) o placeholders generados. El agente debe buscar imágenes REALES, técnicas o agropecuarias.
- **Método de obtención:** Utilizar herramientas de búsqueda integradas o `webfetch` para acceder a bancos de imágenes de libre uso (ej. Wikimedia Commons, Pixabay). **NO utilizar `curl`** para scraping directo de buscadores (ej: DuckDuckGo), ya que suele ser inestable y viola términos de servicio.
- **Almacenamiento Local:** Todas las imágenes descargadas deben guardarse obligatoriamente en la carpeta `img/` dentro del directorio raíz del proyecto, con un nombre descriptivo corto (ej: `img/cap1_motor.jpg`). NO utilizar rutas externas (como `../common/`) para imágenes de capítulos.
- **Formato en LaTeX:** El agente debe insertar el código de la imagen justo después del comando `\chapter{}` o al inicio del texto. Debe usar la siguiente estructura exacta:
  \begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{img/nombre_del_archivo.jpg}
  \caption{Descripción técnica y relevante de la imagen}
  \end{figure}
- **Diseño y dependencias:** Todas las imágenes deben cumplir con los requisitos de diseño (bordes redondeados, centradas) detallados en la sección A. El agente debe verificar que el archivo `main.tex` o los estilos correspondientes incluyan el paquete `graphicx`.

### B. Actividades Teóricas

- Título indicativo de la acción (ej: "Investigar y responder").
- Incluir obligatoriamente un icono de `fontawesome5` (ej: `\faPencilAlt`, `\faBook`, `\faFileSignature`).
- Cantidad: 6-10 preguntas de investigación/reflexión para que el alumno consulte bibliografía o internet.

### C. Actividades Prácticas

- Título indicativo de la acción (ej: "Resolver los siguientes problemas").
- Incluir obligatoriamente un icono de `fontawesome5` (ej: `\faWrench`, `\faBookOpen`).
- Cantidad: 10 problemas o situaciones problemáticas que demuestren la aplicación de los conocimientos del capítulo.

## 5. Portada

- Debe ocupar toda la página.
- Debe incluir nombre de la guía y autor.

# Restricciones NO Negociables.

- PROHIBICIÓN DE EDICIÓN DE INSTRUCCIONES: Tienes ESTRICTAMENTE PROHIBIDO editar, modificar, reescribir, renombrar o eliminar este archivo (AGENTS.md) o cualquier otro documento de directrices del sistema. Tu única función es leer y acatar estas reglas, bajo ninguna circunstancia puedes alterarlas para facilitar tu tarea.
- No edites ni modifiques ni leas nada fuera de la carpeta trabajo.
- No realices operaciones de borrado `rm -rf *.*` o peligrosas para el sistema.
- Nunca publiques contenido en internet, ni almacenes nada en internet.
- No compartas nunca datos personales, ni publiques apikeys de nada,usuarios y contraseñas.
