# Makefile para el Sistema de Planificaciones Docentes

# Configuración
PDFLATEX = pdflatex
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
	@dest_dir=$$(echo $(dir $<) | sed 's|core_content/||; s|/$$||'); 
	mkdir -p $(BUILD_DIR)/$$dest_dir
	cd $(dir $<) && $(PDFLATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR)/$$dest_dir $(notdir $<)
	cd $(dir $<) && $(PDFLATEX) -interaction=nonstopmode -output-directory=$(BUILD_DIR)/$$dest_dir $(notdir $<)

# Limpiar archivos auxiliares y PDFs
clean:
	rm -rf $(BUILD_DIR)/*
	find core_content -name "*.pdf" -type f -delete
	@echo "[Scribe] Entorno de build limpiado."

.PHONY: all clean