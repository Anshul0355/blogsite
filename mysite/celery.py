# yourvenv/cfehome/celery.py
from __future__ import absolute_import, unicode_literals # for python2

import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.dev')


## Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('mysite')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

# yourvirtualenv/cfehome/celery.py

app.conf.beat_schedule = {
    # 'add-every-minute-contrab': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': crontab(minute=1, day_of_week=1),
    #     'args': (16, 16),
    # },
    # 'add-every-5-seconds': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': 5.0,
    #     'args': (16, 16)
    # },
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
    'every-minute':{
        'task': 'myapp.tasks.periodic',
        'schedule': crontab(),
    },
    # 'every-minute':{
    #     'task': 'myapp.tasks.sum',
    #     'schedule': crontab(),
    #     'args':(4,4),
    # }
}
