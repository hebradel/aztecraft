FROM python:3.11-slim

# 1. Crear directorio de trabajo
WORKDIR /app

# 2. Copiar dependencias primero para cachear pip install
COPY requirements.txt /app/

# 3. Instalar pip y dependencias
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código
COPY . /app

# 5. Ejecutar collectstatic si aplica (remóntalo si no lo usas)
# RUN python manage.py collectstatic --noinput

# 6. Forma shell para que se expanda $PORT y lance Gunicorn
ENV PORT 8000
CMD ["/bin/sh", "-c", "exec gunicorn mi_proyecto.wsgi:application --bind 0.0.0.0:${PORT}"]
