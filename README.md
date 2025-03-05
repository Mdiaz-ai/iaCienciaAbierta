# Proyecto de Análisis de Artículos Científicos con Grobid 🧠📊


[![Python](https://img.shields.io/badge/Python-3.8%2B-red)](https://www.python.org/)

[![Docker](https://img.shields.io/badge/Docker-Requiere-2496ED)](https://www.docker.com/)

[![Licencia](https://img.shields.io/badge/Licencia-Apache%202.0-green)](https://www.apache.org/licenses/LICENSE-2.0)

[![DOI](https://zenodo.org/badge/927880683.svg)](https://doi.org/10.5281/zenodo.14894307)

[![Automated Release Notes by Mdíaz](https://img.shields.io/badge/%F0%9F%A4%96-release%20notes-00B2EE.svg)](https://github.com/Mdiaz-ai/iaCienciaAbierta/releases)

# Herramienta automatizada para extraer y visualizar datos de artículos académicos en PDF. Genera:

- 🌥️ **Nubes de palabras** de resúmenes

- 📈 **Gráficos de figuras** por artículo

- 🔗 **Listados de enlaces** externos



# Configuración del Entorno 🐍

### Opción 1: Con Conda (recomendado)


## Crear entorno
```bash
conda create -n cienciaabierta python=3.9
```

## Activar entorno
```bash
conda activate cienciaabierta
```

## Instalar dependencias
```bash
conda install -c conda-forge wordcloud matplotlib numpy pillow requests
```
### También se como se menciona más abajo se puede hacer pip install -r requirements.txt

## Verificar instalación
```bash
conda list
```

### Opción 2: Con venv (Python nativo)

## Crear entorno
```bash
python -m venv .venv
```

## Activar entorno (Linux/Mac)
```bash
source .venv/bin/activate
```

## Activar entorno (Windows)
```bash
.venv\Scripts\activate
```

## Instalar dependencias
```bash
pip install -r requirements.txt
```


# Requisitos Previos ⚙️
-**Docker** ([Guía de instalación](https://docs.docker.com/get-docker/))

- **Python 3.8+** y `pip`

- Memoria RAM recomendada: 4GB+ (para procesamiento simultáneo)



# Instalación 🛠️

 ## Clonar el repositorio:
```bash
git clone https://github.com/Mdiaz-ai/iaCienciaAbierta.git iaCienciaAbierta
```

```bash
cd iaCienciaAbierta
```

## Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Contenido de requirements.txt:

**wordcloud==1.8.2**

**matplotlib==3.7.1**

**numpy==1.24.3**

**pillow==8.3.2**

**requests==2.31.0**

**pytest**

**coverage**


# Configuración Inicial🐳

Iniciar el servidor Grobid en Docker:
```bash
docker run -d --rm -p 8070:8070 --name grobid lfoppiano/grobid:0.7.2
```

Verificar que el servidor esté activo:
```bash
curl http://localhost:8070/api/isalive  # Debe responder "true"
```

# Uso 🚀

Preparar archivos PDF:

Descomprimir la carpeta de pdfs.(En el caso de que se quieran añadir más o cambiar los documentos, simplemente, una vez descomprimida la carpeta, cambie el contenido y listo).

Procesar los documentos:
```bash
python procesar_pdfs.py    # Genera XML en la carpeta 'salida'
```
Generar resultados:

# Nubes de palabras (ventanas emergentes)
```bash
python generate_wordcloud.py
```
# Gráfico de figuras por artículo
```bash
python graficar.py
```
# Extraer enlaces a 'links.txt'
```bash
python links.py
```

Resultados Esperados 📂
Carpeta/Archivo	Descripción	Ejemplo
salida/*.xml	Metadatos estructurados en XML	procesado_articulo1.xml
WordCloud_*.png	Nubes de palabras interactivas	WordCloud
figure_chart.png	Gráfico de barras de figuras por artículo	Figuras
links.txt	Enlaces externos detectados	Enlaces

# Tests Unitarios 🧪

El proyecto incluye una suite completa de tests unitarios para verificar el correcto funcionamiento de cada componente sin necesidad de contar con archivos reales o una instalación de Grobid.

## Requisitos para Testing

Para ejecutar los tests, asegúrate de tener instaladas las dependencias adicionales:

```bash
pip install pytest coverage
```

O simplemente actualiza tu entorno usando el requirements.txt que ya incluye estas dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de Tests

### Usando unittest (método estándar)

```bash
# Ejecutar todos los tests desde el directorio raíz ia_def
python -m unittest discover -s tests

# Desde la carpeta principal del proyecto para ejecutar algún test en concreto
python -m unittest discover -s tests -p "test_procesar_pdfs.py"
python -m unittest discover -s tests -p "test_links.py"
python -m unittest discover -s tests -p "test_graficar.py"
python -m unittest discover -s tests -p "test_wordcloud.py"
```

### Usando pytest (alternativa recomendada)

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con información detallada
pytest -v

# Ejecutar un archivo de tests específico
pytest test_procesar_pdfs.py
```

### Análisis de Cobertura

Para evaluar qué porcentaje del código está cubierto por los tests:

```bash
# Ejecutar tests con análisis de cobertura
coverage run -m pytest

# Ver informe de cobertura
coverage report

# Generar informe HTML detallado
coverage html
# El informe estará disponible en htmlcov/index.html
```

## Contenido de los Tests

- **test_procesar_pdfs.py**: Verifica el procesamiento de PDFs y la comunicación con Grobid
- **test_links.py**: Prueba la extracción y filtrado de enlaces de los documentos XML
- **test_graficar.py**: Valida la generación de gráficos sobre figuras encontradas
- **test_wordcloud.py**: Comprueba la extracción de abstracts y generación de nubes de palabras

Los tests utilizan técnicas de mock para simular interacciones con el sistema de archivos, APIs externas y bibliotecas gráficas, permitiendo verificar la lógica del código sin dependencias externas.

## Añadir Nuevos Tests

Si contribuyes al proyecto, asegúrate de añadir tests para las nuevas funcionalidades:

1. Crea un nuevo archivo `test_nombre_modulo.py`
2. Implementa clases de test heredando de `unittest.TestCase`
3. Usa mocks cuando sea necesario para aislar el código de dependencias externas
4. Verifica que los tests pasen antes de enviar un Pull Request




# Solución de Problemas 🔧

Error: **"Conexión rechazada al servidor Grobid"**

Verifica que Docker esté en ejecución: **docker ps**

Reinicia el contenedor: **docker restart grobid**

Dependencias faltantes:

# Instalar manualmente:

**pip install wordcloud matplotlib numpy pillow**


# Estructura del Proyecto 🌳
```
├── pdfs.zip                   # PDFs originales
├── salida/                 # XML procesados y resultados
├── tests/                  # test unitarios
├── scripts/                # scripts del programa en python
│   ├── procesar_pdfs.py        # Procesamiento con Grobid
│   ├── generate_wordcloud.py   # Generador de nubes de palabras
│   ├──graficar.py             # Visualización de figuras
│   ├──links.py                # Extracción de enlaces
├── requirements.txt        # Dependencias de Python
```

# Contribuciones 👥

¡Bienvenidas las contribuciones! Sigue estos pasos:

Abre un issue describiendo la mejora.

Haz un fork del repositorio.

Crea una rama: git checkout -b mi-mejora.

Envía un Pull Request con tus cambios.

Licencia 📜
Distribuido bajo la licencia Apache-2.0 . Consulta el archivo **LICENSE** para más detalles.

**Nota:** Para procesar más de 10 artículos, se recomienda aumentar los recursos de Docker (RAM y CPU).
