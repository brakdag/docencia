# Makefile para el Sistema de Planificaciones Docentes

# Configuración
PDFLATEX = pdflatex
BUILD_DIR = build

# Buscar todos los archivos .tex en las carpetas de escuelas, ignorando los templates
SOURCES = $(shell find distritos -name "*.tex" | grep -v "templates")

# Convertir la lista de .tex a .pdf
TARGETS = $(SOURCES:.tex=.pdf)

# Objetivo por defecto: compilar todo
all: $(TARGETS)
	@echo "\n[Scribe] Todas las planificaciones han sido compiladas con éxito."

# Regla de compilación
# Se ejecuta pdflatex dos veces para asegurar que las referencias sean correctas
%.pdf: %.tex
	@mkdir -p $(BUILD_DIR)
	@echo "Compilando: $<"
	$(PDFLATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) $<
	$(PDFLATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR) $<
	@# Mover el PDF resultante desde build/ a la carpeta del archivo .tex
	@cp $(BUILD_DIR)/$(notdir $*).pdf $(dir $<)

# Limpiar archivos auxiliares y PDFs
clean:
	rm -rf $(BUILD_DIR)/*
	find distritos -name "*.pdf" -type f -delete
	@echo "[Scribe] Entorno de build limpiado."

.PHONY: all clean