python manage.py collectstatic --noinput
gunicorn --bind=0.0.0.0:8000 davixxa_website.wsgi