# Manual para la Creación de Evaluaciones en Formato 4-en-1

Este manual describe el procedimiento para crear evaluaciones en LaTeX que permitan imprimir 4 temas diferentes en una sola hoja A4, diseñadas para ser cortadas en forma de cruz (2x2).

## 1. Características del Formato
- **Distribución**: 4 evaluaciones por página.
- **Corte**: División en cruz (cuadrantes).
- **Contenido**: Cada tema es una variación del mismo examen (mismos problemas, distintos valores numéricos y orden intercambiado).
- **Puntaje**: Cada problema indica su valor; la suma total debe ser 10 puntos.
- **Encabezado**: Cada cuadrante contiene el título de la materia y el número de tema.

## 2. Configuración Técnica (LaTeX)

### Paquetes Necesarios
Para lograr este formato, se deben incluir los siguientes paquetes:
- `geometry`: Para reducir los márgenes y aprovechar el espacio de la hoja.
- `enumitem`: Para controlar el espaciado de las listas de problemas (`nosep`).
- `amsmath`: Para fórmulas matemáticas.
- `babel` y `inputenc`: Para soporte de idioma español y caracteres especiales.

### Comando Personalizado
Para facilitar la inserción de problemas y sus puntajes, se recomienda definir el siguiente comando en el preámbulo:

```latex
\newcommand{\prob}[2]{\item #1 \textbf{(#2 pts)}}
```
*   `#1`: Texto del problema.
*   `#2`: Puntaje asignado.

## 3. Estructura del Documento

### Diseño de la Página
Se utiliza una combinación de `\noindent`, `minipage` y `\hfill` para crear la cuadrícula 2x2.

- **Ancho de minipage**: Aproximadamente `0.48\textwidth` para dejar un pequeño espacio central.
- **Alto de minipage**: Aproximadamente `0.47\textheight` para evitar que el contenido salte a la segunda página.

### Organización de los Temas
1. **Tema 1**: Cuadrante superior izquierdo.
2. **Tema 2**: Cuadrante superior derecho.
3. **Tema 3**: Cuadrante inferior izquierdo.
4. **Tema 4**: Cuadrante inferior derecho.

## 4. Estrategia de Creación de Temas

Para garantizar que los exámenes sean equivalentes pero distintos:
1. **Definir Problemas Base**: Crear 7 problemas fundamentales.
2. **Asignar Puntajes**: Distribuir los 10 puntos según la dificultad (ej. 3 de 1pt, 2 de 1.5pts, 2 de 2pts).
3. **Variar Valores**: Crear 4 sets de datos numéricos diferentes para cada problema.
4. **Intercambiar Orden**: Cambiar la posición de los problemas en cada tema para evitar copias.

## 5. Plantilla Base (MWE)

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[margin=1cm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{amsmath}
\usepackage{enumitem}

\pagestyle{empty}
\setlist[enumerate]{nosep, leftmargin=1.5em}
\newcommand{\prob}[2]{\item #1 \textbf{(#2 pts)}}

\begin{document}
\noindent
% --- FILA 1 ---
\begin{minipage}[t][0.47\textheight][t]{0.48\textwidth}
  \begin{center}
    \textbf{\large Título de la Materia}\\
    \textbf{\Large Evaluación - Tema 1}
  \end{center}
  \begin{enumerate}
    \prob{Problema 1...}{1}
    \prob{Problema 2...}{2}
    % ... completar 7 problemas
  \end{enumerate}
\end{minipage}
\hfill
\begin{minipage}[t][0.47\textheight][t]{0.48\textwidth}
  \begin{center}
    \textbf{\large Título de la Materia}\\
    \textbf{\Large Evaluación - Tema 2}
  \end{center}
  \begin{enumerate}
    \prob{Problema 1 (variado)...}{1}
    \prob{Problema 2 (variado)...}{2}
    % ... completar 7 problemas
  \end{enumerate}
\end{minipage}

\vspace{0.2cm}

\noindent
% --- FILA 2 ---
\begin{minipage}[t][0.47\textheight][t]{0.48\textwidth}
  \begin{center}
    \textbf{\large Título de la Materia}\\
    \textbf{\Large Evaluación - Tema 3}
  \end{center}
  \begin{enumerate}
    % ... problemas en orden distinto
  \end{enumerate}
\end{minipage}
\hfill
\begin{minipage}[t][0.47\textheight][t]{0.48\textwidth}
  \begin{center}
    \textbf{\large Título de la Materia}\\
    \textbf{\Large Evaluación - Tema 4}
  \end{center}
  \begin{enumerate}
    % ... problemas en orden distinto
  \end{enumerate}
\end{minipage}

\end{document}
```