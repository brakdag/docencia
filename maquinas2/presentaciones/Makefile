# Makefile para Presentaciones de Máquinas Eléctricas II

# Nombre del archivo principal
TARGET = main_pres
SRC = $(TARGET).tex

# Comando de compilación
# -pdfxe: usa xelatex para generar el PDF
# -interaction=nonstopmode: evita que el proceso se detenga en errores (no entra en modo REPL)
LATEXMK = latexmk -pdfxe -interaction=nonstopmode

# Visor de PDF (según tech_data.md)
VIEWER = zathura

.PHONY: all clean view

# Objetivo por defecto: compilar el PDF
all: $(TARGET).pdf

$(TARGET).pdf: $(SRC)
	@echo "Compilando presentación..."
	$(LATEXMK) $(SRC)
	@echo "Compilación finalizada."

# Limpiar archivos auxiliares y el PDF
clean:
	@echo "Limpiando archivos temporales..."
	latexmk -C
	rm -f *.pdf
	@echo "Limpieza completa."

# Compilar y abrir el visor
view:
	$(MAKE) all
	$(VIEWER) $(TARGET).pdf &