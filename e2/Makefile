# Nombres de los archivos (sin extensión)
MAIN_DOC = main
INTRO_DOC = intro

# Objetivo por defecto: crea el PDF final
all: $(MAIN_DOC).pdf

# --- REGLAS DE DEPENDENCIA ---

# 1. Regla para main.pdf
# Dice: "Para crear main.pdf, necesito main.tex Y TAMBIÉN intro.pdf"
$(MAIN_DOC).pdf: $(MAIN_DOC).tex $(INTRO_DOC).pdf
	latexmk -pdf $(MAIN_DOC).tex

# 2. Regla para intro.pdf
# Dice: "Para crear intro.pdf, necesito intro.tex"
$(INTRO_DOC).pdf: $(INTRO_DOC).tex
	latexmk -pdf $(INTRO_DOC).tex

# --- UTILIDADES ---

# Limpieza profunda (-C borra los PDF también)
# Debemos decirle que limpie AMBOS proyectos explícitamente
clean:
	latexmk -C $(MAIN_DOC).tex
	latexmk -C $(INTRO_DOC).tex

# Abrir el PDF final (asegurándose primero de que esté compilado)
view: all
	xdg-open $(MAIN_DOC).pdf &

# Regla extra por si quieres compilar SOLO la intro
intro: $(INTRO_DOC).pdf