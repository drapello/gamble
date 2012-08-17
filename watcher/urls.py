from django.conf.urls.defaults import *
from watcher.views import new
urlpatterns = patterns('django.views.generic.simple',
    (r'new', new),
)
