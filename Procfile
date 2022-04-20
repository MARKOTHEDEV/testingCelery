web: gunicorn proj.wsgi:application
worker_1: celery -A proj worker -l INFO
worker_2: celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
