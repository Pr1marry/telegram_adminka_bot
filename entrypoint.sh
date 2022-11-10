#!/bin/sh

# Apply database migrations
echo "Applying database migrations ..."
python manage.py migrate

# Create superuser
echo "Creating superuser ..."
python manage.py createsuperuser --username "admin" --email "admin@banl.com" --password "adminpow"

# Start server
echo "Starting server ..."
python manage.py runserver 0.0.0.0:8000
