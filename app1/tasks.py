from __future__ import absolute_import,unicode_literals
from celery import shared_task
from proj.celery import app
from celery.utils.log import get_task_logger
from .models import TestingME
logger = get_task_logger(__name__)


@shared_task
def add(x,y):
    a= TestingME.objects.create(name='yehdfnrig') 
    a.save() 
    return x+y
