# Usa la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de la carpeta actual al directorio de trabajo
COPY . .

# Expone el puerto 8000 para acceder a la aplicación
EXPOSE 8000

# Ejecuta el comando para iniciar la aplicación
CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "8000"]