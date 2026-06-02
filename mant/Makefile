# Makefile para el Proyecto de Mantenimiento

# Configuración
PDFLATEX = pdflatex
BUILD_DIR = build

# Archivo principal
MAIN = main

# Dependencias
# Se incluyen los archivos de configuración y estilo para que cualquier cambio en ellos
# dispare la reconstrucción del PDF
DEPS = config.tex setup.sty toolsgf.sty $(shell find capitulos -name "*.tex")

# Objetivo por defecto
all: $(BUILD_DIR)/$(MAIN).pdf
	@echo "\n[Scribe] Compilación completada. PDF generado en $(BUILD_DIR)/$(MAIN).pdf"

# Regla de compilación
$(BUILD_DIR)/$(MAIN).pdf: $(MAIN).tex $(DEPS)
	@mkdir -p $(BUILD_DIR)
	$(PDFLATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) $(MAIN).tex
	$(PDFLATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) $(MAIN).tex

clean:
	rm -rf $(BUILD_DIR)
	@echo "[Scribe] Entorno de build limpiado."

.PHONY: all clean