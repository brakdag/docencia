# 📐 Protocolo de Inspección de Geometría Documental (PAGD)

**Versión:** 1.0  
**Responsable:** Technical Scribe  
**Objetivo:** Extraer las constantes espaciales y visuales de un documento origen (Word/PDF) para su replicación exacta y optimizada en $\text{\LaTeX}$.

---

## 📋 Instrucciones de Uso
Este protocolo debe completarse **antes** de iniciar la codificación del documento. La omisión de cualquier punto en este análisis resultará en ajustes iterativos ineficientes durante la fase de compilación.

---

## 🟦 Módulo 1: Definición del Lienzo (Canvas)
*Análisis del espacio físico y límites del documento.*

- [ ] **Orientación:**
    - [ ] Vertical (Portrait) $\rightarrow$ `geometry{portrait}`
    - [ ] Apaisado (Landscape) $\rightarrow$ `geometry{landscape}`
- [ ] **Formato de Papel:**
    - [ ] A4 (Estándar)
    - [ ] Carta (Letter)
    - [ ] Otro: ____________________
- [ ] **Márgenes (Medición precisa en mm):**
    - Superior: `____ mm` | Inferior: `____ mm`
    - Izquierdo: `____ mm` | Derecho: `____ mm`
    - [ ] ¿Existe margen de encuadernación (gutter)? $\rightarrow$ `____ mm`

---

## 🟩 Módulo 2: Periferia y Marcos (Headers & Footers)
*Análisis de los elementos recurrentes en los bordes de la página.*

### 2.1 Encabezado (Header)
- [ ] **Estado:** [ ] Ausente | [ ] Presente
- [ ] **Contenido:** ________________________________________________
- [ ] **Alineación:** [ ] Izquierda | [ ] Centro | [ ] Derecha | [ ] Distribuido
- [ ] **Línea Divisoria:** [ ] No | [ ] Sí $\rightarrow$ Grosor: `____ pt`

### 2.2 Pie de Página (Footer)
- [ ] **Estado:** [ ] Ausente | [ ] Presente
- [ ] **Contenido:** ________________________________________________
- [ ] **Alineación:** [ ] Izquierda | [ ] Centro | [ ] Derecha
- [ ] **Línea Divisoria:** [ ] No | [ ] Sí $\rightarrow$ Grosor: `____ pt`

---

## 🟧 Módulo 3: Inventario de Activos Visuales (Assets)
*Identificación de elementos no textuales para extracción y optimización.*

- [ ] **Imágenes en Periferia:**
    - [ ] Logo Institucional $\rightarrow$ Posición: ____________________
    - [ ] Escudo/Sello $\rightarrow$ Posición: ____________________
    - [ ] Firma/Sello de Agua $\rightarrow$ Posición: ____________________
- [ ] **Análisis de Calidad:**
    - [ ] Vectorial (PDF/SVG) $\rightarrow$ *Uso directo.*
    - [ ] Rasterizada (PNG/JPG) $\rightarrow$ *Requiere recorte/vectorización.*
- [ ] **Elementos Gráficos Repetitivos:**
    - [ ] Bordes de página decorativos.
    - [ ] Iconos de check/opciones ($\checkmark$, $\square$).

---

## 🟨 Módulo 4: Análisis de Estructura Interna (Grid)
*Análisis de la organización de la información en el cuerpo del documento.*

- [ ] **Distribución de Columnas:**
    - [ ] Una sola columna.
    - [ ] Multicolumna $\rightarrow$ Cantidad: `____`
- [ ] **Uso de Tablas/Cuadros:**
    - [ ] Tablas simples (Filas/Columnas estándar).
    - [ ] Tablas anidadas (Celdas complejas).
    - [ ] Cuadros de texto con fondo coloreado $\rightarrow$ `tcolorbox`.
- [ ] **Tipografía Detectada:**
    - Fuente Principal: ____________________
    - Fuente de Títulos: ____________________
    - Tamaño de Cuerpo: `____ pt` | Tamaño de Títulos: `____ pt`

---

## 🛠️ Guía de Traducción Técnica (Quick Reference)

| Hallazgo en Protocolo | Paquete/Comando $\text{\LaTeX}$ Sugerido |
| :--- | :--- |
| Márgenes/Papel | `\usepackage[...]{geometry}` |
| Encabezados/Pies | `\usepackage{fancyhdr}` |
| Fuentes del Sistema | `\usepackage{fontspec}` (XeLaTeX/LuaLaTeX) |
| Tablas Flexibles | `\usepackage{tabularx}` o `\usepackage{nicematrix}` |
| Cuadros Estéticos | `\usepackage{tcolorbox}` |
| Listas Personalizadas | `\usepackage{enumitem}` |
| Imágenes | `\usepackage{graphicx}` |
