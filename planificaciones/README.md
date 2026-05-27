# 🏛️ Sistema de Planificaciones Docentes - Manual de Arquitectura

Este repositorio contiene la infraestructura para la generación de planificaciones anuales, programas y diagnósticos. El sistema está diseñado bajo un flujo de **aislamiento y producción**, asegurando que los documentos finales sean autónomos y estén libres de referencias a plantillas temporales.

## 📂 Mapa de Directorios

```text
planificaciones/
├── docs/                # 📜 CÓDICE NORMATIVO: Manuales, reglamentos y requerimientos provinciales.
├── distritos/           # 🎨 SANTUARIO DE PLANTILLAS: Moldes institucionales (logos, formatos, ejemplos).
│   └── [ESCUELA_ID]/    # Plantillas específicas por institución.
├── core_content/        # ⚙️ NÚCLEO DE PRODUCCIÓN: El corazón del sistema.
│   ├── [materia].tex     # CONTENIDO MAESTRO: Esencia técnica genérica de la materia.
│   └── [ESCUELA_ID]/     # DOCUMENTOS FINALES: Versiones limpias y adaptadas para 2026.
├── Makefile             # 🛠️ ORQUESTADOR: Automatiza la compilación de todo el núcleo.
└── README.md            # 📖 ESTE MANIFIESTO.

build/                   # 🖼️ GALERÍA DE FINALES: (En la raíz) Destino de todos los PDFs compilados.
```

## 🔄 Flujo de Trabajo (Pipeline)

Para crear una planificación, se debe seguir estrictamente este orden:

1.  **Consulta Normativa:** Revisar `/docs` para asegurar el cumplimiento legal.
2.  **Extracción de Esencia:** Definir el contenido técnico en `/core_content/[materia].tex`.
3.  **Aplicación de Molde:** Utilizar los formatos y logos de `/distritos/[ESCUELA_ID]`.
4.  **Producción Final:** Generar los archivos `.tex` finales en `/core_content/[ESCUELA_ID]/`.

## 🛠️ Protocolo de Compilación

El sistema utiliza un `Makefile` para procesar todos los documentos de forma masiva.

- **Comando:** `make all` (ejecutado desde la carpeta `./planificaciones`).
- **Acción:** Busca todos los archivos `.tex` dentro de `core_content`, los compila mediante `pdflatex` y deposita los resultados en la carpeta `/build` de la raíz.
- **Limpieza:** `make clean` elimina los archivos auxiliares y los PDFs generados.

## 🚫 Leyes Inviolables (Scribe's Commandments)

Para mantener la integridad del sistema, se prohíbe:

1.  **Cero Referencias a Distritos:** Ningún archivo `.tex` en `core_content` debe contener rutas que apunten a la carpeta `distritos`. 
2.  **Autonomía de Recursos:** Si un documento necesita un recurso (ej. `logoDGE.jpeg`), este **DEBE** ser copiado localmente a la carpeta de la escuela en `core_content`. No se permiten enlaces externos a las plantillas.
3.  **Compilación Selectiva:** Solo se compila lo que reside en `core_content`. La carpeta `distritos` es estrictamente de lectura y referencia.
4.  **Ubicación de Salida:** Los PDFs finales deben converger siempre en la carpeta `/build` de la raíz.

---
*Documento redactado por el Escriba Técnico. Cualquier desviación de este plano se considera un fallo sistémico.*