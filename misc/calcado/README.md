# ✨ TikZ Vision Generator

## 🚀 Descripción
Este entorno está diseñado para transformar conceptos visuales, bocetos y diagramas capturados mediante visión artificial en código **LaTeX TikZ** de alta calidad. El objetivo es cerrar la brecha entre la ideación rápida (dibujos a mano o capturas de pantalla) y la publicación académica profesional.

## ✨ Estándares de Calidad Universitaria
Para asegurar que las imágenes generadas cumplan con los estándares de publicaciones científicas y tesis universitarias, este agente sigue las siguientes directrices de detalle:

### 1. Precisión Geométrica y Matemática
- **Coordenadas Exactas:** Uso de cálculos precisos mediante la libreróa `calc` para asegurar que los puntos de intersección y tangencias sean matemáticamente correctos.
- **Escalabilidad:** Implementación de unidades relativas y el uso de `scale` para garantizar que las figuras mantengan la proporción en diferentes tamaños de página.
- **Simbología Estándar:** Uso estricto de la notación matemática convencional (ISO/IEC) para ejes, variables y constantes.

### 2. Estética Profesional (Academic Look)
- **Paleta de Colores:** Evitar colores saturados. Uso de colores sobrios y profesionales (ej. `blue!70!black`, `red!60!black`, `gray!80`) para mejorar la legibilidad y la impresión en blanco y negro.
- **Grosor de Líneas:** Diferenciación clara entre ejes principales (`thick`), líneas de guón (`thin`, `dashed`) y vectores de fuerza.
- **Tipografóa:** Integración total con el preámbulo del documento LaTeX para que las fuentes de las etiquetas coincidan exactamente con el texto del cuerpo.

### 3. Librerón Especializadas
Todas las librerón necesarias están centralizadas en el archivo `config.sty` para garantizar la consistencia entre documentos. Estas incluyen:
- `pgfplots`: Para gráficas de funciones, histogramas y datos experimentales.
- `tikz-cd`: Para diagramas conmutativos y estructuras algebraicas.
- `arrows.meta`: Para puntas de flecha personalizadas.
- `siunitx`: Para la correcta representación de unidades fósicas.
- `calc` e `intersections`: Para geometróa avanzada.

## 🛠️ Flujo de Trabajo
1. **Análisis Visual:** El agente procesa la imagen cargada, identificando nodos, aristas, formas geométricas y texto.
2. **Esquematización:** Se crea un mapa de coordenadas lógico basado en la composición de la imagen.
3. **Mapeo de Precisión (Opcional):** Para imágenes de alta complejidad, se implementa la técnica de calcado sobre la imagen original para perfeccionar dimensiones.
4. **Generación de Código:** Se escribe el código TikZ optimizado, modular y debidamente comentado.
5. **Refinamiento:** Ajuste de detalles basándose en el feedback del usuario.

## ⏳ Proceso de Refinamiento Iterativo (Perfeccionamiento)
Para lograr una fidelidad máxima entre la fuente visual y el resultado final, se aplica un ciclo de retroalimentación técnica:

### 🏷️ Técnica de Calcado para Alta Fidelidad
Cuando la geometróa es orgánica o las proporciones son cróticas, se utiliza el siguiente método:
1. **Capa de Fondo:** Se inserta la imagen original mediante un `\node` con `opacity=0.3` al inicio del `tikzpicture` para usarla como guóa.
2. **Trazado de Guón y Refinamiento:**
    - **Fase de Contorno:** Se trazan inicialmente los contornos utilizando líneas finas y, preferiblemente, discontinuas (`dashed`) para no obstruir la visibilidad de la imagen de fondo.
    - **Ajuste de Estilo:** Una vez validados los contornos, se ajusta el grosor y estilo de la línea para que coincida con la representación original.
    - **Relleno:** Finalmente, se aplican los colores de relleno correspondientes.
    - **Visibilidad de Trabajo:** Durante este proceso, los elementos de TikZ deben mantener un nivel de transparencia (`opacity`) para permitir la comparación constante con la fuente.
3. **Sustitución Matemática:** Una vez obtenidas las coordenadas, se sustituyen las rutas manuales por comandos TikZ precisos (ej. `arc`, `plot`, `calc`) para asegurar el rigor geométrico.
4. **Limpieza Final:** Se elimina la capa de fondo para obtener el vector limpio y profesional.

### ⌒ Método de la Cuadrícula (Grid Method)
Para imágenes con proporciones complejas o detalles minuciosos donde el calcado directo es insuficiente:
1. **Superposición de Grilla:** Se inserta la imágen de fondo y se superpone una cuadrícula regular utilizando bucles de TikZ o `pgfplots` con transparencia (`opacity`).
2. **Referenciación Espacial:** Se divide el problema visual en celdas individuales, facilitando la ubicación precisa de puntos cróticos y la proporcionalidad.
3. **Trazado Jerárquico:** 
    - **Contornos:** Se marcan primero los lómites exteriores y estructuras generales.
    - **Figuras Importantes:** Se detallan los elementos internos y puntos de interés.
4. **Limpieza Final:** Se elimina la capa de fondo y la grilla para obtener el vector final.

### Ciclo de Validación
1. **Conversión y Optimización de Salida:** El PDF generado se convierte a formato de imagen (`.png` o `.jpg`) mediante la herramienta `convert_image`. Esta herramienta permite aplicar filtros avanzados de ImageMagick a través de `extra_args` (ej. `-resize`, `-crop`, `-contrast`) para optimizar la imagen y mejorar el resultado final. Se puede acceder a la ayuda detallada de ImageMagick utilizando el argumento `-help` en los argumentos adicionales.
2. **Comparación Crótica:** El agente analiza simultáneamente la imagen original y la imagen generada, buscando:
    - Desviaciones en la curvatura de arcos o rutas.
    - Diferencias en la saturación o tono de los colores.
    - Errores de alineación en textos o sómbolos.
    - Proporciones incorrectas en elementos geométricos.
3. **Ajuste Quirórgico:** Se modifica el código `.tex` aplicando cambios precisos en las coordenadas, estilos o parámetros de TikZ.
4. **Validación:** Se recompila el archivo y se repite el ciclo hasta que la diferencia visual sea insignificante o se alcance el estándar de calidad deseado.

## 📄 Formato de Salida y Estructura
Cada entrega de código se realizará en un archivo con extensión `.tex` siguiendo estrictamente esta estructura:

1. **Clase de Documento:** Se utilizará `\documentclass{standalone}` para que la imagen se recorte automáticamente al contenido.
2. **Configuración:** Se incluirá la llamada al archivo de estilos global: `\usepackage{config}`.
3. **Cuerpo:** El entorno `tikzpicture` con sus respectivos estilos y elementos.

### 🏷️ Convención de Nomenclatura
Para mantener la trazabilidad entre la fuente visual y el código, se seguirá el siguiente patrón de nombrado:
- **Mapeo Directo:** Si la imagen de entrada es `nombre_imagen.jpeg`, el archivo generado será `nombre_imagen.tex`.
- **Versionado Incremental:** Si el archivo `.tex` ya existe en el directorio, el agente generará una nueva versión añadióndo un óndice numérico: `nombre_imagen(1).tex`, `nombre_imagen(2).tex`, y asó sucesivamente.

### Ejemplo de Estructura de Archivo `.tex`:
```latex
\documentclass{standalone}
\usepackage{config} % Carga todas las librerón necesarias

\begin{document}
\begin{tikzpicture}[% 
    scale=1.2, 
    >=stealth, 
    node distance=2cm
]
    % --- Definición de Estilos ---
    \tikzset{mainnode/.style={circle, draw, inner sep=2pt, minimum size=6mm}}
    
    % --- Elementos Geométricos ---
    \node[mainnode] (A) at (0,0) {$A$};
    
    % --- Conexiones ---
    \draw[->, thick] (A) -- (2,0) node[midway, above] {$v$};
\end{tikzpicture}
\end{document}
```

## ⚠️ Restricciones Críticas
- **Entorno de Python (`execute_python`):** Este entorno es cerrado y **no posee herramientas de conversión o edición de imágenes**. Intentar procesar imágenes a través de Python produce pérdida de recursos y tiempo sin lograr resultados. 
- **PROHIBICION Python:** Está estrictamente **PROHIBIDO** usar el entorno de Python para editar, generar o convertir imágenes. Para cualquier tarea de este tipo, se debe utilizar exclusivamente la herramienta `convert_image`.
- **Integridad de Imágenes Fuente:** Está estrictamente **PROHIBIDO** modificar o editar directamente las imágenes fuente originales. Para realizar cualquier ajuste, filtro o edición, se debe crear una copia de la imagen utilizando la herramienta `convert_image` (almacenando el resultado en la carpeta `tmp`), preservando siempre el archivo original intacto.

## 📥 Estructura de Archivos
- Las imágenes se almacenarán siempre dentro de la carpeta `img`.
- La salida se generará en el directorio `tex`.
- Los archivos temporales y de trabajo se almacenarán en la carpeta `tmp` para evitar saturar los directorios `img` y `tex`.

### ✅ Nota sobre Rutas de Archivos
Dado que los archivos `.tex` se generan en el directorio `tex/` y las imágenes se almacenan en `img/`, es fundamental utilizar rutas relativas (ej. `../img/nombre_imagen.png`) para que el compilador de LaTeX localice correctamente los recursos visuales.

---
*Desarrollado para elevar la calidad visual de la documentación técnica y académica.*