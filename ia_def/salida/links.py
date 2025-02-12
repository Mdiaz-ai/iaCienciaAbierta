import os
import xml.etree.ElementTree as ET

output_folder = "/home/upm/Escritorio/salida"
all_links = []

# Namespace de TEI (necesario para buscar elementos correctamente)
tei_ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

for xml_file in os.listdir(output_folder):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(output_folder, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Buscar todos los elementos que contengan un atributo "target"
        elements = root.findall(".//*[@target]", namespaces=tei_ns)
        
        for element in elements:
            link = element.attrib['target']
            # Filtrar solo enlaces que sean URLs externas
            if link.startswith(("http://", "https://")):
                all_links.append(link)

# Guardar solo los enlaces válidos
with open("/home/upm/Escritorio/salida/enlaces.txt", 'w') as f:
    f.write("\n".join(all_links))

print(f"Enlaces extraídos: {len(all_links)}")