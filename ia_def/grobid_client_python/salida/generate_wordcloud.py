import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import glob
import os

# Configuración de namespaces para Grobid
namespaces = {
    'tei': 'http://www.tei-c.org/ns/1.0',
    'xml': 'http://www.w3.org/XML/1998/namespace'
}
# Función para buscar carpetas
def buscar_carpeta(nombre_carpeta):
    for root, dirs, files in os.walk(os.path.expanduser('~')):
        if nombre_carpeta in dirs:
            return os.path.join(root, nombre_carpeta)
    return None



def extract_abstract_text(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Buscar el abstract usando XPath
        abstract = root.find('.//tei:profileDesc/tei:abstract', namespaces)
        
        if abstract is None:
            print(f"[!] No se encontró el abstract en: {xml_path}")
            return ""
            
        # Extraer todo el texto incluyendo elementos anidados
        abstract_text = ''.join(abstract.itertext()).strip()
        
        if not abstract_text:
            print(f"[!] El abstract en {xml_path} está vacío.")
        
        return abstract_text
        
    except Exception as e:
        print(f"[X] Error procesando {xml_path}: {str(e)}")
        return ""

# Carpeta de salida donde están los XML procesados
output_folder = buscar_carpeta('salida')

# Buscar todos los archivos XML en la carpeta de salida
xml_files = glob.glob(os.path.join(output_folder, '*.xml'))

if not xml_files:
    print("No se encontraron archivos XML en la carpeta de salida.")
else:
    for xml_path in xml_files:
        print(f"\nProcesando: {xml_path}")

        # Extraer texto del abstract
        text = extract_abstract_text(xml_path)

        if text:
            print(f"Texto extraído ({len(text)} caracteres). Generando nube de palabras...")

            # Generar wordcloud con parámetros de centrado
            wordcloud = WordCloud(
                width=1200,
                height=600,
                background_color='white',
                collocations=False,
                prefer_horizontal=0.5,
                relative_scaling=0.3,
                stopwords=set(['et', 'al']),
                normalize_plurals=False,
                margin=10
            ).generate(text)

            # Configurar figura
            plt.figure(figsize=(15, 8), facecolor='white', dpi=100)
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.tight_layout(pad=0)
            plt.title(f"Nube de palabras para {os.path.basename(xml_path)}", pad=20)
            plt.show()

        else:
            print(f"[!] No se generó nube de palabras para {xml_path} (sin texto válido).")
