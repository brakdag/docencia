# --- Configuración del Escriba Técnico ---
# Nombre del archivo por defecto (sin extensión .tex)
target ?= tex_diploma_promedio_2025

# Compilador y Banderas
COMPILER = xelatex
FLAGS = -interaction=nonstopmode -synctex=1
OUT_DIR = out

# Detección de todas las fuentes de diplomas
SOURCES = $(wildcard tex_*.tex)
# Corrección: Usamos addprefix para construir la lista de PDFs en la carpeta out/
PDFS = $(addprefix $(OUT_DIR)/, $(SOURCES:.tex=.pdf))

# Regla principal: Genera el PDF del target especificado en la carpeta out/
all: $(OUT_DIR)/$(target).pdf

# Regla masiva: Genera los PDFs de TODOS los archivos tex_ en la carpeta out/
all_tex: $(PDFS)

# Regla genérica de compilación con redirección de salida
$(OUT_DIR)/%.pdf: %.tex
	mkdir -p $(OUT_DIR)
	$(COMPILER) $(FLAGS) -output-directory=$(OUT_DIR) $<

# Limpieza de artefactos: Borra la carpeta de salida completa
clean:
	rm -rf $(OUT_DIR)

# Limpieza total
distclean: clean

.PHONY: all all_tex clean distclean
