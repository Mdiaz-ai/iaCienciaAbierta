# Fundamentación

Este documento explica la metodología y los procesos de validación para cada tarea en el análisis de 10 artículos de acceso abierto utilizando Grobid y scripts personalizados en Python.

---

## 1. Nube de palabras a partir de resúmenes

### Enfoque
- **Script**: `generate_wordcloud.py`
- **Herramientas**: Biblioteca `wordcloud`, salidas XML de Grobid.
- **Proceso**:
  - Los resúmenes se extraen de los archivos XML generados por Grobid usando consultas XPath.
  - El texto se limpia y se filtran palabras comunes (p. ej., "et", "al").
  - Se genera una nube de palabras basada en la frecuencia de términos.

### Validación
- **Muestreo manual**: Se compararon resúmenes de archivos XML seleccionados al azar con los PDF originales para verificar precisión.
- **Verificación de palabras excluidas**: Se confirmó que términos como "et" o "al" no aparecen en las nubes finales.
- **Inspección visual**: Las nubes generadas reflejan términos clave de los resúmenes (p. ej., jerga técnica específica de cada artículo).

---

## 2. Visualización de figuras por artículo

### Enfoque
- **Script**: `graficar.py`
- **Herramientas**: Matplotlib, salidas XML de Grobid.
- **Proceso**:
  - Cuenta las etiquetas `<tei:figure>` en cada XML usando XPath.
  - Genera un gráfico de barras con el número de figuras por documento.

### Validación
- **Conteo manual**: Para 3 artículos aleatorios, se contrastó el número de etiquetas `<tei:figure>` con las figuras reales en los PDFs.
- **Casos extremos**: Se probó con XML sin figuras para asegurar que el script maneja resultados vacíos.
  - Ejemplo: Un artículo sin figuras mostró `0` en el gráfico.

---

## 3. Extracción de enlaces

### Enfoque
- **Script**: `links.py`
- **Herramientas**: Parsing XML con `xml.etree.ElementTree`.
- **Proceso**:
  - Extrae atributos `target` que comienzan con `http://` o `https://`.
  - Guarda enlaces únicos y totales en `links.txt`.

### Validación
- **Verificación de enlaces**: Enlaces seleccionados al azar se comprobaron manualmente (accesibilidad y relevancia).
- **Detección de duplicados**: Se confirmó que `links.txt` distingue entre enlaces únicos y totales.
  - Ejemplo: Un DOI repetido se contabilizó en "Total" pero solo una vez en "Únicos".

---

## Validación general del flujo de trabajo

### Procesamiento de PDFs con Grobid
- **Script**: `procesar_pdfs.py`
- **Validación**:
  - Se aseguró que el servidor Grobid estuviera activo durante las pruebas.
  - Se revisaron salidas XML para confirmar que estructuras como títulos y resúmenes coincidían con los PDFs.

### Manejo de errores
- Todos los scripts incluyen bloques `try-except` para gestionar archivos corruptos o errores de red.
  - Ejemplo: `links.py` omite XML dañados y registra el error sin detener la ejecución.

### Reproducibilidad
- **Directorios**: Los scripts buscan automáticamente las carpetas `pdfs` y `salida` en el sistema, garantizando portabilidad.
- **Dependencias**: Requerimientos como `matplotlib` se documentan en el `README.md`.

---

## Limitaciones
1. **Dependencia de Grobid**: Requiere una instancia local de Grobid en ejecución. Fallos en el servidor pueden interrumpir el proceso.
2. **Supuestos en XML**: Los scripts asumen que las rutas XPath (p. ej., `<tei:figure>`) son consistentes en todos los XML. Cambios en Grobid podrían afectar su funcionamiento.
3. **Sesgo de idioma**: Las palabras excluidas ("et", "al") están orientadas a textos académicos en inglés/latín. Para otros idiomas, sería necesario ajustar la lista.

---

Para replicar el análisis, consulte el `README.md` del repositorio con instrucciones de configuración y dependencias.
