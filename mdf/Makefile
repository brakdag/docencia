PROJECT = main
OUT_DIR = out
FINAL_NAME = Guia-tp-mecanica-de-los-fluidos

# Encuentra todas las subcarpetas que contienen archivos .tex
# Esto replicará la estructura (ej: capitulos, secciones, etc.)
SUBDIRS = $(shell find . -maxdepth 2 -not -path '*/.*' -type d)
OUT_SUBDIRS = $(addprefix $(OUT_DIR)/, $(SUBDIRS))

LATEXMK_OPTS = -pdf -outdir=$(OUT_DIR) -interaction=nonstopmode

.PHONY: all build release clean view

all: build

build:
	@mkdir -p $(OUT_SUBDIRS) # Crea out/ y out/capitulos/ etc.
	latexmk $(LATEXMK_OPTS) $(PROJECT).tex

release: build
	cp $(OUT_DIR)/$(PROJECT).pdf ./$(FINAL_NAME).pdf

clean:
	latexmk -C -outdir=$(OUT_DIR)
	rm -rf $(OUT_DIR)
	rm -f $(FINAL_NAME).pdf
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
