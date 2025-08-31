
#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create admin user
echo "Creating admin user..."
python manage.py create_admin

# Start Gunicorn server
echo "Starting Gunicorn server..."
gunicorn --bind 0.0.0.0:7860 schoolproj.wsgi:application
