# Guía de Uso de `run_instance` para el Orquestador

Este documento detalla el procedimiento correcto para invocar instancias de colaboradores especializados utilizando la herramienta `run_instance`.

## Configuración Técnica

Para abrir una nueva instancia de un agente con un rol específico, se deben seguir estos parámetros:

- **Target**: Debe ser siempre `paser-mini`.
- **Argumentos (`args`)**: Se debe utilizar el flag `-fsi` seguido de la ruta al archivo `.md` que contiene las instrucciones del sistema (System Instructions) del rol deseado.

## Ejemplo de Implementación

Si el Profesor de Electromecánica (Orquestador) necesita comunicarse con el Editor de Contenido Técnico, la llamada a la herramienta debe ser:

```json
{
  "name": "run_instance",
  "args": {
    "target": "paser-mini",
    "message": "[Mensaje detallando la tarea a realizar]",
    "args": ["-fsi", "docs/staff/technical_content_editor.md"]
  }
}
```

## Flujo de Trabajo de Colaboración

1. **Identificación del Rol**: El Orquestador determina qué especialista es necesario (Técnico, Pedagógico o LaTeX).
2. **Invocación**: Se ejecuta `run_instance` con el archivo de rol correspondiente ubicado en `docs/staff/`.
3. **Delegación**: Se envía una instrucción clara y concisa en el campo `message`.
4. **Síntesis**: El Orquestador recibe la respuesta de la instancia, la analiza y la integra en la visión global del proyecto.

## Notas Importantes
- No utilizar `instance` como target, ya que no es un módulo reconocido.
- Asegurarse de que la ruta al archivo `.md` sea correcta y relativa a la raíz del proyecto.