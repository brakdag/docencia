import re

latex_file = 'e2/capitulos/10_maquina_rotativa.tex'
with open(latex_file, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'\\actividad\{Resolver los siguientes problemas\.\}(.*?)\\end\{enumerate\}', content, re.DOTALL)
if match:
    ejercicios_raw = match.group(1)
    items = re.split(r'\\item\s+', ejercicios_raw)
    preguntas = [item.strip() for item in items if item.strip()]
else:
    preguntas = []

xml_builder = ['<?xml version="1.0" encoding="UTF-8"?>']
xml_builder.append('<quiz>')
xml_builder.append('<!-- question: 0 -->')
xml_builder.append('  <question type="category">')
xml_builder.append('    <category>')
xml_builder.append('      <text>$course$/top/Predeterminado para Máquina Rotativa/Cuestionario Máquina Rotativa</text>')
xml_builder.append('    </category>')
xml_builder.append('  </question>')

for i, p in enumerate(preguntas, 1):
    p_clean = p.replace('\\', '<br>')
    p_clean = re.sub(r'\\textbf\{(.*?)\}', r'<b>\1</b>', p_clean)
    p_clean = re.sub(r'\\emph\{(.*?)\}', r'<em>\1</em>', p_clean)
    
    xml_builder.append('  <question type="essay">')
    xml_builder.append(f'    <name><text>Pregunta {i} - Máquina Rotativa</text></name>')
    xml_builder.append(f'    <questiontext format="html">')
    xml_builder.append(f'      <text><![CDATA[<p><b>Problema {i}:</b></p><p>{p_clean}</p>]]></text>')
    xml_builder.append('    </questiontext>')
    xml_builder.append('    <generalfeedback format="html"><text><![CDATA[]]></text></generalfeedback>')
    xml_builder.append('    <defaultgrade>1.0000000</defaultgrade>')
    xml_builder.append('    <penalty>0.3333333</penalty>')
    xml_builder.append('    <hidden>0</hidden>')
    xml_builder.append('    <idnumber></idnumber>')
    xml_builder.append('    <responseformat>editor</responseformat>')
    xml_builder.append('    <responserequired>1</responserequired>')
    xml_builder.append('    <responsefieldlines>15</responsefieldlines>')
    xml_builder.append('    <attachments>1</attachments>')
    xml_builder.append('    <attachmentsrequired>0</attachmentsrequired>')
    xml_builder.append('    <graderinfo format="html"><text><![CDATA[]]></text></graderinfo>')
    xml_builder.append('    <responsetemplate format="html"><text><![CDATA[]]></text></responsetemplate>')
    xml_builder.append('  </question>')

xml_builder.append('</quiz>')

output_xml = '\n'.join(xml_builder)
with open('e2/cuestionario_maquina_rotativa.xml', 'w', encoding='utf-8') as f:
    f.write(output_xml)

print('XML generado exitosamente con', len(preguntas), 'preguntas.')
