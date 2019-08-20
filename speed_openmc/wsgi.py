"""
WSGI config for Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys


current_dir = os.path.abspath(os.path.dirname(__file__).replace('\\','/'))
dirs = current_dir.split(os.path.sep)
del(dirs[-1])
codespeed_dir = os.path.sep.join(dirs)
del(dirs[-1])
project_dir = os.path.sep.join(dirs)

sys.path.append(project_dir)
sys.path.append(codespeed_dir)
os.environ.setdefault("PYTHON_EGG_CACHE", project_dir+"/egg_cache")

from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = codespeed_dir.split(os.path.sep)[-1] + '.settings'
application = get_wsgi_application()
