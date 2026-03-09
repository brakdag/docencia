# Makefile simple para proyecto LaTeX
PROJECT=main
# Si quieres compilar la planificación descomenta abajo
# PROJECT=planificacion 

all:
	latexmk -pdfxe $(PROJECT).tex

clean:
	latexmk -C

view:
	xdg-open $(PROJECT).pdf &
