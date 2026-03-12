PROJECT = main
OUT_DIR = out
FINAL_NAME = Guia-tp-mecanica-de-los-fluidos

# 1. Configuración para precompilar figuras TikZ
TIKZ_DIR = fig/tikz
TIKZ_SRCS = $(shell find $(TIKZ_DIR) -type f -name '*.tex')
TIKZ_PDFS = $(TIKZ_SRCS:.tex=.pdf)

# Encuentra todas las subcarpetas que contienen archivos .tex
SUBDIRS = $(shell find . -maxdepth 2 -not -path '*/.*' -type d)
OUT_SUBDIRS = $(addprefix $(OUT_DIR)/, $(SUBDIRS))

LATEXMK_OPTS = -pdfxe -outdir=$(OUT_DIR) -interaction=nonstopmode
# Opciones para TikZ: usamos -cd para que latexmk compile en el directorio de cada figura
LATEXMK_TIKZ_OPTS = -pdfxe -interaction=nonstopmode

.PHONY: all build release clean view tikz

all: build

# 2. Target para generar todos los PDFs de las figuras
tikz: $(TIKZ_PDFS)

# 3. Regla patrón para compilar cada .tex de la carpeta de figuras a .pdf
%.pdf: %.tex
	latexmk $(LATEXMK_TIKZ_OPTS) -cd $<

# 4. Modificamos 'build' para que dependa de 'tikz'
build: tikz
	@mkdir -p $(OUT_SUBDIRS)
	latexmk $(LATEXMK_OPTS) $(PROJECT).tex

release: build
	cp $(OUT_DIR)/$(PROJECT).pdf ./$(FINAL_NAME).pdf

clean:
	latexmk -C -outdir=$(OUT_DIR)
	rm -rf $(OUT_DIR)
	rm -f $(FINAL_NAME).pdf
	@echo "Limpiando archivos auxiliares de TikZ..."
	@for f in $(TIKZ_SRCS); do latexmk -C -cd $$f; done

view:
	@if [ -f $(OUT_DIR)/$(PROJECT).pdf ]; then \
		echo "Abriendo $(OUT_DIR)/$(PROJECT).pdf..."; \
		xdg-open $(OUT_DIR)/$(PROJECT).pdf & \
	elif [ -f ./$(FINAL_NAME).pdf ]; then \
		echo "Abriendo versión release: $(FINAL_NAME).pdf..."; \
		xdg-open ./$(FINAL_NAME).pdf & \
	else \
		echo "Error: No se encontró el PDF en $(OUT_DIR)/ ni en la raíz."; \
		echo "Ejecuta 'make build' o 'make release' primero."; \
	fi
