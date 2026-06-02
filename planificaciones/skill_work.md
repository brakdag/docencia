# Flujo de trabajo en latex.

para las funciones que no hay tools usar child_process.exec

1 Siempre que se modificó un archivo verificar que se ha modificado. (sino intentar de otra forma y no avanzar hasta que se modifique satisfactoriamente sino no avanzar de este punto )
2 Compilar el archivo (make )
3 Convertir el archivo usando (convert) (verificar que no tenga transparencia la salida, para documentos pdf de varias páginas hay que especificar la página.)
4 Ver el archivo de salida con seeImage.
