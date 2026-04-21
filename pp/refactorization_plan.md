# Plan de Refactorización de la Guía de Prácticas

## Objetivo
Separar el contenido individual (teoría y cuestionarios) del contenido grupal (aplicación al proyecto) para mejorar la organización pedagógica.

## Nueva Estructura de Directorios
- `capitulos/comun/`: Archivos generales (portada, intro, acuerdos).
- `capitulos/individual/`: Teoría y actividades individuales por tema.
- `capitulos/proyecto/`: Actividades aplicadas al proyecto por tema.

## Mapeo de Archivos
| Archivo Original | Destino Individual | Destino Proyecto | Notas |
| :--- | :--- | :--- | :--- |
| `00_a_portada.tex` | `comun/00_a_portada.tex` | - | General |
| `00_b_introduccion.tex` | `comun/00_b_introduccion.tex` | - | General |
| `00_d_acuerdo.tex` | `comun/00_d_acuerdo.tex` | - | General |
| `01_gantt.tex` | `individual/01_gantt.tex` | `proyecto/01_gantt.tex` | Crear consigna de proyecto si no existe |
| `04_costos.tex` | `individual/04_costos.tex` | `proyecto/04_costos.tex` | Split claro detectado |
| ... | ... | ... | ... |

## Pasos de Ejecución
1. Crear carpetas `comun`, `individual` y `proyecto` dentro de `capitulos/`.
2. Mover archivos de `comun`.
3. Procesar cada capítulo: leer $ightarrow$ dividir $ightarrow$ escribir en las dos nuevas carpetas.
4. Actualizar `main.tex` con la nueva jerarquía.
5. Verificar que el `Makefile` o el proceso de compilación siga funcionando.