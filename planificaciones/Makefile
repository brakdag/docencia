# Makefile para el Sistema de Planificaciones Docentes

# Configuración
PDFLATEX = pdflatex
# Definimos la ruta absoluta de build para que el comando 'mv' no falle tras el 'cd'
BUILD_DIR = $(shell pwd)/build

# Buscar todos los archivos .tex ÚNICAMENTE en subcarpetas de core_content
SOURCES = $(shell find core_content -mindepth 2 -name "*.tex")

# Convertir la lista de .tex a .pdf
TARGETS = $(SOURCES:.tex=.pdf)

# Objetivo por defecto: compilar todo
all: $(TARGETS)
	@echo "\n[Scribe] Todas las planificaciones han sido compiladas con éxito en la carpeta $(BUILD_DIR)."

# Regla de compilación
%.pdf: %.tex
	@dir=$$(dirname $<); base=$$(basename $< .tex); dest_dir=$$(echo $$dir | sed 's|^core_content/||'); \
	mkdir -p $(BUILD_DIR)/$$dest_dir && \
	cd $$dir && $(PDFLATEX) -interaction=nonstopmode $$base.tex && $(PDFLATEX) -interaction=nonstopmode $$base.tex && \
	mv $$base.pdf $(BUILD_DIR)/$$dest_dir/$$base.pdf && \
	rm -f *.aux *.log

# Limpiar archivos auxiliares y PDFs
clean:
	rm -rf $(BUILD_DIR)/*
	find core_content -name "*.pdf" -type f -delete
	@echo "[Scribe] Entorno de build limpiado."

.PHONY: all clean