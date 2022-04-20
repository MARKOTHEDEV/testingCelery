web: gunicorn proj.wsgi
worker_1: celery -A proj worker -l info --pool=solo
#worker_1: celery -A proj worker --loglevel=INFO 
worker_2: celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
