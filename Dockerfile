FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar todos los archivos
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto (opcional)
EXPOSE 8000

# Ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
