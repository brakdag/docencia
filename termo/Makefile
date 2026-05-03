# Makefile para corrección ortográfica

# Directorios a analizar
DIRS = capitulos actividades evaluaciones

# Ruta absoluta al JAR de LanguageTool
LT_JAR = /mnt/DataSD/sandbox/human_out_the_loop/LanguageTool/languagetool-commandline.jar

# Comando para ejecutar LanguageTool
LT = java -jar $(LT_JAR)

# Idioma
LANG = es

# Archivo de reporte
REPORT = spelling_report.json

.PHONY: spell

spell:
	@echo "Ejecutando corrección ortográfica en formato JSON..."
	@rm -f $(REPORT)
	@find $(DIRS) -name "*.tex" | while read file; do \
		$(LT) -l $(LANG) --json "$$file" >> $(REPORT); \
	done
	@echo "Análisis completado. El reporte se ha guardado en $(REPORT)."