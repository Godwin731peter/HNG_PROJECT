web: gunicorn hng_task.wsgi --log-file -

web: python manage.py migrate && gunicorn hng_task.wsgi