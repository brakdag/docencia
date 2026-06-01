# Makefile para el Sistema de Planificaciones Docentes

# Configuración
PDFLATEX = pdflatex
BUILD_DIR = build

# Buscar todos los archivos .tex
SOURCES = $(shell find core_content -name "*.tex")
# Convertir core_content/school/file.tex -> build/school/file.pdf
TARGETS = $(patsubst core_content/%,$(BUILD_DIR)/%,$(SOURCES:.tex=.pdf))

# Fuentes específicas por escuela
SOURCES_4117 = $(shell find core_content/4117 -name "*.tex")
TARGETS_4117 = $(patsubst core_content/%,$(BUILD_DIR)/%,$(SOURCES_4117:.tex=.pdf))

SOURCES_4124 = $(shell find core_content/4124 -name "*.tex")
TARGETS_4124 = $(patsubst core_content/%,$(BUILD_DIR)/%,$(SOURCES_4124:.tex=.pdf))

SOURCES_4239 = $(shell find core_content/4239 -name "*.tex")
TARGETS_4239 = $(patsubst core_content/%,$(BUILD_DIR)/%,$(SOURCES_4239:.tex=.pdf))

# Objetivo por defecto
all: $(TARGETS)
	@echo "\n[Scribe] Todas las planificaciones han sido compiladas en $(BUILD_DIR)."

# Objetivos específicos
4117: $(TARGETS_4117)
	@echo "\n[Scribe] Escuela 4117 compilada en $(BUILD_DIR)/4117."

4124: $(TARGETS_4124)
	@echo "\n[Scribe] Escuela 4124 compilada en $(BUILD_DIR)/4124."

4239: $(TARGETS_4239)
	@echo "\n[Scribe] Escuela 4239 compilada en $(BUILD_DIR)/4239."

# Regla de compilación robusta
# Target: build/school/file.pdf
# Source: core_content/school/file.tex
$(BUILD_DIR)/%.pdf: core_content/%.tex
	@mkdir -p $(dir $@)
	$(PDFLATEX) -interaction=nonstopmode -output-directory=$(dir $@) $<
	$(PDFLATEX) -interaction=nonstopmode -output-directory=$(dir $@) $<

clean:
	rm -rf $(BUILD_DIR)
	@echo "[Scribe] Entorno de build limpiado."

.PHONY: all clean 4117 4124 4239