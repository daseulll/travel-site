from .base import * 

import os
SECRET_KEY = os.environ["SECRET_KEY"]

import django_heroku
django_heroku.settings(locals())
