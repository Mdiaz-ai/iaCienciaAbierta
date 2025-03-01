import os
import xml.etree.ElementTree as ET

# Función para buscar carpetas
def buscar_carpeta(nombre_carpeta):
    for root, dirs, files in os.walk(os.path.expanduser('~')):
        if nombre_carpeta in dirs:
            return os.path.join(root, nombre_carpeta)
    return None

# Definir directamente los directorios o buscar en lugares específicos
current_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = buscar_carpeta('salida')
links_file = os.path.join(output_folder, 'links.txt')

# Verificar si existe la carpeta de salida
if not os.path.exists(output_folder):
    # Intentar buscar en el directorio padre
    parent_dir = os.path.dirname(current_dir)
    output_folder = os.path.join(parent_dir, 'salida')
    if not os.path.exists(output_folder):
        print(f"No se encontró la carpeta 'salida'. Por favor, especifica la ruta manualmente.")
        exit(1)

print(f"Usando carpeta de salida: {output_folder}")
print(f"Los enlaces se guardarán en: {links_file}")

all_links = []

# Namespace de TEI (necesario para buscar elementos correctamente)
tei_ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Procesar archivos XML
xml_count = 0
for xml_file in os.listdir(output_folder):
    if xml_file.endswith(".xml"):
        xml_count += 1
        xml_path = os.path.join(output_folder, xml_file)
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
            
            # Buscar todos los elementos que contengan un atributo "target"
            elements = root.findall(".//*[@target]", namespaces=tei_ns)
            
            file_links = 0
            for element in elements:
                if 'target' in element.attrib:
                    link = element.attrib['target']
                    # Filtrar solo enlaces que sean URLs externas
                    if link.startswith(("http://", "https://")):
                        all_links.append(link)
                        file_links += 1
            
            print(f"Procesado {xml_file}: {file_links} enlaces encontrados")
        except Exception as e:
            print(f"Error al procesar {xml_file}: {e}")

# Guardar los enlaces válidos
try:
    with open(links_file, 'w') as f:
        f.write("\n".join(all_links))
    print(f"\nResumen:")
    print(f"Archivos XML procesados: {xml_count}")
    print(f"Enlaces únicos extraídos: {len(set(all_links))}")
    print(f"Total enlaces extraídos: {len(all_links)}")
    print(f"Enlaces guardados en: {links_file}")
except Exception as e:
    print(f"Error al guardar los enlaces: {e}")
