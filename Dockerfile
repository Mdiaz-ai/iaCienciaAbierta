# Usar imagen base de Python
FROM python:3.9-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GROBID_HOST=http://grobid:8070

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Crear directorios necesarios
RUN mkdir -p /app/pdfs /app/salida

# Puerto para posibles servicios (ajustar si es necesario)
EXPOSE 5000

# Comando por defecto (puede sobrescribirse al ejecutar)
CMD ["python", "scripts/procesar_pdfs.py"]
