#!/bin/sh

echo "Waiting for MySQL to initialize..."
sleep 15

echo "Applying database migrations..."
python manage.py migrate

sleep 2
echo "Creating initial data..."
python manage.py createinitialdata

sleep 2
python manage.py makemigrations
python manage.py migrate

sleep 2
echo "Starting Django development server..."
exec "$@"
