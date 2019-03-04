from .base import * 

import django_heroku
django_heroku.settings(locals())

DEBUG = False
ALLOWED_HOSTS = ['travel-blog-site.herokuapp.com', '127.0.0.1']
