import os
import re

def parsear_evaluacion(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        return []
    
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    preguntas = []
    patron_problemas = re.split(r'\\textbf{Problema|Problema', contenido)
    
    for i, bloque in enumerate(patron_problemas[1:], 1):
        enunciado = "Problema " + bloque.strip()
        preguntas.append({
            'nombre': f'Pregunta {i} - Máquina Rotatoria',
            'enunciado': enunciado
        })
        
    return preguntas

def generar_moodle_xml(preguntas, ruta_salida):
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<quiz>
<!-- question: 0 -->
  <question type="category">
    <category>
      <text>$course$/top/Predeterminado para Máquina Rotatoria/Cuestionario Máquina Rotatoria</text>
    </category>
  </question>
'''

    for p in preguntas:
        xml_content += f'''  <question type="multichoice">
    <name><text>{p['nombre']}</text></name>
    <questiontext format="html">
      <text><![CDATA[<p>{p['enunciado']}</p>]]></text>
    </questiontext>
    <generalfeedback format="html"><text><![CDATA[]]></text></generalfeedback>
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <single>true</single>
    <shuffleanswers>true</shuffleanswers>
    <answernumbering>abc</answernumbering>
    <answer fraction="100" format="html">
      <text><![CDATA[Respuesta correcta predeterminada]]></text>
      <feedback format="html"><text><![CDATA[]]></text></feedback>
    </answer>
  </question>
'''

    xml_content += '</quiz>'

    with open(ruta_salida, 'w', encoding='utf-8') as f:
        f.write(xml_content)

if __name__ == '__main__':
    ruta_eval = 'e2/evaluacion_1.tex'
    if os.path.exists(ruta_eval):
        parsed_qs = parsear_evaluacion(ruta_eval)
        generar_moodle_xml(parsed_qs, 'e2/cuestionario_maquina_rotativa_riguroso.xml')
        print("XML generado con exito.")
