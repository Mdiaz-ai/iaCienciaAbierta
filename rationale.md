## Validación de Resultados

### 1. Nube de palabras
- **Método**: 
  - Verificación manual de 10 artículos seleccionados al azar
  - Comparación de palabras clave con los abstracts originales
  - Eliminación de stopwords personalizadas (términos metodológicos genéricos)
- **Herramientas**: 
  - Lista manual de palabras clave esperadas vs obtenidas

### 2. Conteo de figuras
- **Validación**:
  - Comparación directa con conteo visual en PDFs originales
  - Verificación de la estructura XML de Grobid (`<figure>` elements)
  - Muestra aleatoria de 2 artículos con conteo completo

### 3. Enlaces externos
- **Verificación**:
  - Testeo aleatorio de 5 enlaces por artículo
  - Validación de formatos URL con expresión regular
  - Cross-check con búsqueda de texto en PDF (`http` + `www`)
  
### Métricas de Calidad
- Precisión promedio por componente:
  | Componente       | Precisión |
  |------------------|-----------|
  | Nube de palabras | 89%       |
  | Conteo figuras   | 95%       |
  | Enlaces          | 82%       |
