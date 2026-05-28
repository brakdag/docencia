# Makefile para el Sistema de Planificaciones Docentes

# Configuración
PDFLATEX = pdflatex
BUILD_DIR = $(shell pwd)/build

# Buscar todos los archivos .tex ÚNICAMENTE en subcarpetas de core_content
SOURCES = $(shell find core_content -mindepth 2 -name "*.tex")
TARGETS = $(SOURCES:.tex=.pdf)

# Fuentes específicas por escuela
SOURCES_4117 = $(shell find core_content/4117 -name "*.tex")
TARGETS_4117 = $(SOURCES_4117:.tex=.pdf)

SOURCES_4124 = $(shell find core_content/4124 -name "*.tex")
TARGETS_4124 = $(SOURCES_4124:.tex=.pdf)

# Objetivo por defecto: compilar todo
all: $(TARGETS)
	@echo "\n[Scribe] Todas las planificaciones han sido compiladas con éxito en la carpeta $(BUILD_DIR)."

# Objetivos específicos por escuela
4117: $(TARGETS_4117)
	@echo "\n[Scribe] Planificaciones de la escuela 4117 compiladas con éxito en la carpeta $(BUILD_DIR)."

4124: $(TARGETS_4124)
	@echo "\n[Scribe] Planificaciones de la escuela 4124 compiladas con éxito en la carpeta $(BUILD_DIR)."

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

.PHONY: all clean 4117 4124