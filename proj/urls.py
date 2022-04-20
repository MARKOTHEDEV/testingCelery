"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from app1 import tasks
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
from datetime import datetime,timedelta
def me(request):
    
    schedule, created = IntervalSchedule.objects.get_or_create(

    every=2,

    period=IntervalSchedule.SECONDS,

)
    # tasks.some_task.delay()
    PeriodicTask.objects.create(
 interval=schedule,                  # we created this above.
    name='Testing SomeTask Contact',          # simply describes this periodic task.
    task='app1.tasks.add',  # name of task.
    args=json.dumps([1, 120]),
    # kwargs=json.dumps({
    #    'be_careful': True,
    # }),

    # expires=datetime.utcnow() + timedelta(seconds=30)
    )
    return HttpResponse('wow')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',me)
]

