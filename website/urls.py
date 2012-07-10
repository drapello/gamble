from django.conf.urls.defaults import *
from website.views import crawl
urlpatterns = patterns('django.views.generic.simple',
    (r'crawl', crawl),
)
