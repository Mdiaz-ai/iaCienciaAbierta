import requests

# Ruta al archivo PDF
pdf_path = '/home/upm/Escritorio/OAS_Spanish_web.pdf'

# URL del servidor Grobid
grobid_url = 'http://localhost:8070/api/processFulltextDocument'

# Abrir el archivo PDF en modo binario
with open(pdf_path, 'rb') as pdf_file:
    # Enviar el archivo al servidor Grobid
    response = requests.post(grobid_url, files={'input': pdf_file})

# Verificar la respuesta del servidor
if response.status_code == 200:
    # Guardar la respuesta en un archivo XML
    with open('/home/upm/Escritorio/OAS_Spanish_web.xml', 'wb') as xml_file:
        xml_file.write(response.content)
    print("El archivo XML se ha guardado correctamente.")
else:
    print(f"Error al procesar el PDF: {response.status_code} - {response.text}")

