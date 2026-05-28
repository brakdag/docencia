# Workflow.

## Objetivo.

Producir 3 documentos por curso (ver cursos.md) en LaTeX.
La información está en

- formato.md
- planificacion.md , diagnostico.md y programa.md

El cada archivo latex debe respetar el formato. definido en esta carpeta.
/home/gustavo/sandbox/repositorio_docente/planificaciones/distritos/4239

Los archivos tex deben grabarse en esta ruta.
/home/gustavo/sandbox/repositorio_docente/planificaciones/core_content/4239

Para completar los datos faltantes puede obtenerse información desde las guias
de trabajos prácticos de cada curso y de los DCP.

/home/gustavo/sandbox/repositorio_docente/planificaciones/docs

/home/gustavo/sandbox/repositorio_docente/dt (dibujo tecnico )
/home/gustavo/sandbox/repositorio_docente/mant (mantenimiento)

# compilación

Para compilar usamos el archivo
/home/gustavo/sandbox/repositorio_docente/planificaciones/Makefile

- deberían compilarse estos 6 documentos con el siguiente comando "make 4239"
- Luego también debería compilarse con "make all"

* Cualquier información faltante se puede buscar y ver en internet.
* No dejar instrucciones de llanado sino que llenar con la documentación.

### Salida

- Sos archivos pdf deben grabarse en la carpeta
  /home/gustavo/sandbox/repositorio_docente/planificaciones/build
