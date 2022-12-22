# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, '/home/anton/www/depparis.store/depparis')
sys.path.insert(1, '/home/anton/www/depparis.store/paris_env/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'depparis.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
