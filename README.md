# Proyecto e-commerce genérico

Proyecto base reutilizable para e-commerce B2C/B2B en Django.

## Configuración inicial

1. Crear entorno virtual e instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Crear archivo `.env` con al menos:
   ```
   SECRET_KEY=tu_clave
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   CSRF_TRUSTED_ORIGINS=http://localhost
   ```
3. Migraciones y superusuario:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Ejecutar:
   ```bash
   python manage.py runserver
   ```
