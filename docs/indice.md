# Índice de Proyecto: Prisma Técnico

Este documento es el mapa operativo de la misión definida en el [README.md](./README.md). Aquí se detalla dónde reside cada recurso para transformar el rigor técnico en accesibilidad pedagógica.

## 🛠️ Base Técnica
- [Entorno de Desarrollo (`tech_data.md`)](./tech_data.md): Especificaciones del stack de LaTeX, OS y herramientas de edición (Neovim/VimTeX).

## 📚 Áreas Técnicas (Materias/Módulos)

### ⚡ Electricidad y Electromagnetismo
- `/e2`: Electromagnetismo y Circuitos (Resistencias, Inductores, Capacitores, Corriente Alterna).
- `/maquinas2`: Máquinas Eléctricas (Motores Stepper, Servo, Brushless, Alternadores).

### 🌡️ Termodinámica y Fluidos
- `/termo`: Termodinámica (Transmisión de calor, Gases perfectos, Ciclos de Carnot, Entropía).
- `/mdf`: Mecánica de Fluidos (Principios de Pascal, Arquímedes, Bernoulli, Reynolds).

### 📐 Dibujo Técnico y Diseño
- `/dt`: Dibujo Técnico (Escalas, Líneas, Figuras, Acotación, Cortes).
- `/dta`: Material complementario y evaluaciones de Dibujo Técnico.
- `/freecad_guia`: Guía de aprendizaje para FreeCAD (Modelado 2D/3D).
- `/calcado`: Materiales específicos de calcado y dibujo técnico asistido.

### 🛠️ Mantenimiento y Prácticas
- `/mant`: Mantenimiento Industrial (Codificación, Lubricación, Predictivo).
- `/mantIA`: Mantenimiento asistido por Inteligencia Artificial.
- `/pp`: Prácticas Profesionalizantes (Gestión de proyectos, Gantt, Kanban, Costos, Marco Jurídico).

## ⚙️ Recursos Transversales y Soporte

### 🛠️ Plantillas y Estilos (LaTeX)
- `/common`: Fuentes, imágenes y estilos `.sty` compartidos.
- `/hojaA4`: Configuración de página A4 estándar.
- `/generic`: Capítulos y estilos genéricos para guías.

### 🎓 Gestión Académica
- `/diplomas`: Sistema de generación de certificados y diplomas para egresados.
- `/varios`: Calendarios, planillas de alumnos, recibos y problemas diversos.

### 📖 Documentación Interna
- `/docs`: Políticas de staff, definiciones de roles y flujos de trabajo.
  - `/docs/staff`: Perfiles detallados (Arquitecto Pedagógico, Curador, Escriba).

## 🗺️ Mapa de Flujo de Trabajo Sugerido
1. **Cosecha** $\rightarrow$ `/common` o carpetas de materia $\rightarrow$ `images/`
2. **Proceso** $\rightarrow$ `/capitulos/` (Diseño instruccional)
3. **Insight** $\rightarrow$ `main.tex` $\rightarrow$ PDF final

---
*Actualizado por el Arquitecto Pedagógico.*