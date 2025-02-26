import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


# Función para buscar carpetas
def buscar_carpeta(nombre_carpeta):
    for root, dirs, files in os.walk(os.path.expanduser('~')):
        if nombre_carpeta in dirs:
            return os.path.join(root, nombre_carpeta)
    return None

# Define la carpeta de salida donde están los XML procesados
output_folder = buscar_carpeta('salida')

# Inicializa una lista para almacenar el número de figuras por documento
figure_counts = []
document_names = []

# Analiza cada archivo XML en la carpeta
for xml_file in os.listdir(output_folder):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(output_folder, xml_file)

        # Parsear el archivo XML
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Contar las etiquetas de figuras
        figures = root.findall(".//tei:figure", namespaces={'tei': 'http://www.tei-c.org/ns/1.0'})
        figure_counts.append(len(figures))
        document_names.append(xml_file)

# Graficar el número de figuras por archivo
plt.bar(document_names, figure_counts)
plt.xlabel('Documento')
plt.ylabel('Número de figuras')
plt.title('Número de figuras por artículo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

