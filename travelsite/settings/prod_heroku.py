from .base import * 

DEBUG = False
ALLOWED_HOSTS = ['travel-blog-site.herokuapp.com', '127.0.0.1']

import django_heroku
django_heroku.settings(locals())

