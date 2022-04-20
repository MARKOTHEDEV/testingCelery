web: gunicorn proj.wsgi
worker_1: celery -A proj worker --loglevel=INFO --concurrency=2
worker_2: celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
