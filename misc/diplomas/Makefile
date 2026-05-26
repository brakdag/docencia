# Nombre del archivo principal (sin la extensión .tex)
DOCNAME = test

# Compilador
COMPILER = xelatex

# Opciones: 
# -interaction=nonstopmode: Para que no se frene ante errores (evita el "?")
# -synctex=1: Habilita la sincronización entre el PDF y el código (útil si usas editores gráficos)
FLAGS = -interaction=nonstopmode -synctex=1

# Regla por defecto (se ejecuta al escribir 'make')
all: $(DOCNAME).pdf

# Regla para generar el PDF
$(DOCNAME).pdf: $(DOCNAME).tex
	$(COMPILER) $(FLAGS) $(DOCNAME).tex
	# Descomenta la siguiente línea si usas referencias cruzadas o índices (compila dos veces)
	# $(COMPILER) $(FLAGS) $(DOCNAME).tex

# Regla para limpiar archivos auxiliares (log, aux, out, etc.)
clean:
	rm -f *.aux *.log *.out *.synctex.gz *.toc *.fls *.fdb_latexmk

# Regla para limpiar todo, incluyendo el PDF final
distclean: clean
	rm -f $(DOCNAME).pdf

.PHONY: all clean distclean