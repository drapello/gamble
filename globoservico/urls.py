from django.conf.urls.defaults import *
from globoservico.views import incidentes
urlpatterns = patterns('django.views.generic.simple',
    (r'incidentes', incidentes),
)
