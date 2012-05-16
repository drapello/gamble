import os, sys
import posixpath

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.abspath("%s/.." % PROJECT_ROOT))
sys.path.insert(0, PROJECT_ROOT)

# os.environ['DJANGO_SETTINGS_MODULE'] = '<%=portal_id%>_settings'
# os.environ['RUNNING_MODE'] = 'wsgi'
# os.environ['HTTPD_INSTANCE'] = 'be'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
