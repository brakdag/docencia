# Makefile para el Sistema de Planificaciones Docentes

# Configuración
PDFLATEX = pdflatex
BUILD_DIR = ../build

# Buscar todos los archivos .tex ÚNICAMENTE en subcarpetas de core_content
SOURCES = $(shell find core_content -mindepth 2 -name "*.tex")

# Convertir la lista de .tex a .pdf
TARGETS = $(SOURCES:.tex=.pdf)

# Objetivo por defecto: compilar todo
all: $(TARGETS)
	@echo "\n[Scribe] Todas las planificaciones han sido compiladas con éxito en la carpeta $(BUILD_DIR)."

# Regla de compilación
%.pdf: %.tex
	@mkdir -p $(BUILD_DIR)
	@echo "Compilando: $<">
	@dir=$$(dirname $<);
	@base=$$(basename $< .tex);
	@cd $$dir && $(PDFLATEX) -interaction=nonstopmode $$base.tex
	@cd $$dir && $(PDFLATEX) -interaction=nonstopmode $$base.tex
	@cp $(dir $<)/$$base.pdf $(BUILD_DIR)/$$base.pdf
	@rm -f $(dir $<)/*.aux $(dir $<)/*.log

# Limpiar archivos auxiliares y PDFs
clean:
	rm -rf $(BUILD_DIR)/*
	find core_content -name "*.pdf" -type f -delete
	@echo "[Scribe] Entorno de build limpiado."

.PHONY: all clean