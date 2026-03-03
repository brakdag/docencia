# Nombres de los archivos (sin extensión)
MAIN_DOC = main

# Objetivo por defecto: crea el PDF final
all: $(MAIN_DOC).pdf

# --- REGLAS DE DEPENDENCIA ---

# 1. Regla para main.pdf
# Dice: "Para crear main.pdf, necesito main.tex Y TAMBIÉN intro.pdf"
$(MAIN_DOC).pdf: $(MAIN_DOC).tex
	latexmk -pdfxe $(MAIN_DOC).tex

# --- UTILIDADES ---

# Limpieza profunda (-C borra los PDF también)
# Debemos decirle que limpie AMBOS proyectos explícitamente
clean:
	latexmk -C $(MAIN_DOC).tex

# Abrir el PDF final (asegurándose primero de que esté compilado)
view: all
	xdg-open $(MAIN_DOC).pdf &

