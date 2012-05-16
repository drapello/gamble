import os, sys
import posixpath

print "passou aqui 1"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.abspath("%s/.." % PROJECT_ROOT))
sys.path.insert(0, PROJECT_ROOT)

print "passou aqui 2"


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

print "passou aqui 3"
