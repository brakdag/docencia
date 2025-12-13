# .latexmkrc - Configuración local del proyecto

# 1. Definir el compilador (1 = pdflatex, 4 = lualatex, 5 = xelatex)
# Usamos pdflatex por defecto, si usas muchas fuentes ttf cambia a 5.
$pdf_mode = 1;

# 2. Opciones de compilación (Flags)
# -synctex=1: Permite saltar del PDF al código en Vim (reverse search).
# -interaction=nonstopmode: No se detiene en errores leves, sigue compilando.
# -file-line-error: Muestra errores formato archivo:linea (vital para quickfix de Vim).
$pdflatex = 'pdflatex -file-line-error -synctex=1 -interaction=nonstopmode %O %S';

# 3. Limpieza automática de archivos basura (además de los estándar)
$clean_ext = "synctex.gz xdv nav snm toc aux log out bbl blg";

# 4. (Opcional) Si usas glosarios o índices, descomenta:
# @custom_dependency_list = ( ... ); 
# (latexmk suele detectar makeindex automáticamente)
