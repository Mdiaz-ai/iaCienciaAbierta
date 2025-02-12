import requests
import os

# URL del servidor Grobid
grobid_url = 'http://localhost:8070/api/processFulltextDocument'

# Ruta de las carpetas
pdf_folder = '/home/upm/Escritorio/pdfs'  # Ruta correcta a tus archivos PDF
output_folder = '/home/upm/Escritorio/salida'  # Ruta donde guardar los resultados procesados

# Asegurarse de que la carpeta de salida exista, si no, crearla
os.makedirs(output_folder, exist_ok=True)

# Procesar los archivos PDF en la carpeta
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        
        # Realizar la solicitud POST para procesar el archivo PDF
        try:
            with open(pdf_path, 'rb') as pdf_file:
                response = requests.post(grobid_url, files={'input': pdf_file})
            
            # Verificar la respuesta del servidor
            if response.status_code == 200:
                # Obtener solo el nombre del archivo sin la ruta
                output_filename = f"procesado_{os.path.basename(pdf_file.name)}.xml"
                output_path = os.path.join(output_folder, output_filename)
                
                # Guardar la respuesta en un archivo XML
                with open(output_path, 'wb') as xml_file:
                    xml_file.write(response.content)
                print(f"Archivo procesado y guardado en {output_path}")
            else:
                print(f"Error al procesar el PDF: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"Error procesando el archivo {pdf_file.name}: {e}")

