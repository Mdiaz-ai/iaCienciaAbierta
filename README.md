# Proyecto de Análisis de Artículos Científicos con Grobid 🧠📊


![Python](https://img.shields.io/badge/Python-3.8%2B-red)

![Docker](https://img.shields.io/badge/Docker-Requiere-2496ED)

![Licencia](https://img.shields.io/badge/Licencia-Apache%202.0-green)

[![DOI](https://zenodo.org/badge/927880683.svg)](https://doi.org/10.5281/zenodo.14894307)


## Configuración del Entorno 🐍

### Opción 1: Con Conda (recomendado)


# Crear entorno
conda create -n cienciaabierta python=3.9


# Activar entorno
conda activate cienciaabierta


# Instalar dependencias
conda install -c conda-forge wordcloud matplotlib numpy pillow requests


# Verificar instalación
conda list


### Opción 2: Con venv (Python nativo)

# Crear entorno
python -m venv .venv


# Activar entorno (Linux/Mac)
source .venv/bin/activate


# Activar entorno (Windows)
.venv\Scripts\activate


# Instalar dependencias
pip install -r requirements.txt



Herramienta automatizada para extraer y visualizar datos de artículos académicos en PDF. Genera:

- 🌥️ **Nubes de palabras** de resúmenes

- 📈 **Gráficos de figuras** por artículo

- 🔗 **Listados de enlaces** externos



## Requisitos Previos ⚙️
-**Docker** ([Guía de instalación](https://docs.docker.com/get-docker/))

- **Python 3.8+** y `pip`

- Memoria RAM recomendada: 4GB+ (para procesamiento simultáneo)



## Instalación 🛠️

 # Clonar el repositorio:**

**git clone https://github.com/Mdiaz-ai/iaCienciaAbierta.git**

**cd iaCienciaAbierta**

**Instalar dependencias:**

**pip install -r requirements.txt**

**Contenido de requirements.txt:**

**wordcloud==1.8.2**

**matplotlib==3.7.1**

**numpy==1.24.3**

**pillow==8.3.2**

**requests==2.31.0**



# Configuración Inicial🐳

Iniciar el servidor Grobid en Docker:

**docker run -d --rm -p 8070:8070 --name grobid lfoppiano/grobid:0.7.2**


Verificar que el servidor esté activo:

**curl http://localhost:8070/api/isalive**  # Debe responder "true"


Uso 🚀

Preparar archivos PDF:

Descomprimir la carpeta de pdfs.(En el caso de que se quieran añadir más o cambiar los documentos, simplemente, una vez descomprimida la carpeta, cambie el contenido y listo).

Procesar los documentos:

**python procesar_pdfs.py**  # Genera XML en la carpeta 'salida'

Generar resultados:

# Nubes de palabras (ventanas emergentes)
**python generate_wordcloud.py**

# Gráfico de figuras por artículo
**python graficar.py**

# Extraer enlaces a 'links.txt'
**python links.py**

Resultados Esperados 📂
Carpeta/Archivo	Descripción	Ejemplo
salida/*.xml	Metadatos estructurados en XML	procesado_articulo1.xml
WordCloud_*.png	Nubes de palabras interactivas	WordCloud
figure_chart.png	Gráfico de barras de figuras por artículo	Figuras
links.txt	Enlaces externos detectados	Enlaces

Solución de Problemas 🔧

Error: **"Conexión rechazada al servidor Grobid"**

Verifica que Docker esté en ejecución: **docker ps**

Reinicia el contenedor: **docker restart grobid**

Dependencias faltantes:

# Instalar manualmente:
**pip install wordcloud matplotlib numpy pillow**

Estructura del Proyecto 🌳


├── pdfs/                   # PDFs originales

├── salida/                 # XML procesados y resultados

├── procesar_pdfs.py        # Procesamiento con Grobid

├── generate_wordcloud.py   # Generador de nubes de palabras

├── graficar.py             # Visualización de figuras

├── links.py                # Extracción de enlaces

  └── requirements.txt        # Dependencias de Python

Contribuciones 👥

¡Bienvenidas las contribuciones! Sigue estos pasos:

Abre un issue describiendo la mejora.

Haz un fork del repositorio.

Crea una rama: git checkout -b mi-mejora.

Envía un Pull Request con tus cambios.

Licencia 📜
Distribuido bajo la licencia Apache-2.0 . Consulta el archivo **LICENSE** para más detalles.

**Nota:** Para procesar más de 10 artículos, se recomienda aumentar los recursos de Docker (RAM y CPU).
