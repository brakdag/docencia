# Nombres de los archivos (sin extensión)
MAIN_DOC = main
EVAL_DOC = evaluaciones/evaluacion_1

# Objetivos que no son archivos reales
.PHONY: all clean view view_eval evals

# Objetivo por defecto: crea el PDF final de la guón
all: $(MAIN_DOC).pdf

# --- REGLAS DE DEPENDENCIA ---

# 1. Regla para main.pdf
$(MAIN_DOC).pdf: $(MAIN_DOC).tex
	latexmk -pdfxe $(MAIN_DOC).tex

# 2. Regla para la evaluación 1 (dependencia de archivo)
$(EVAL_DOC).pdf: $(EVAL_DOC).tex
	latexmk -pdfxe $(EVAL_DOC).tex

# Comando para forzar la compilación de las evaluaciones
evals:
	latexmk -pdfxe $(EVAL_DOC).tex

# --- UTILIDADES ---

# Limpieza profunda
clean:
	latexmk -C $(MAIN_DOC).tex
	latexmk -C $(EVAL_DOC).tex

# Abrir el PDF final de la guía
view: all
	xdg-open $(MAIN_DOC).pdf &

# Abrir el PDF de la evaluación
view_eval: evals
	xdg-open $(EVAL_DOC).pdf &
