$pdf_mode = 1; # Usar pdflatex
$pdflatex = 'pdflatex -file-line-error -synctex=1 -interaction=nonstopmode %O %S';

# ESTO ES NUEVO: Si hay errores, intentar forzar la salida igual
$force_mode = 1; 

# Si usas biblatex/biber (estándar moderno) en vez de bibtex clásico:
# Descomenta la siguiente línea:
# $pdf_mode = 1; $bibtex_use = 1.5;
