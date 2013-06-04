from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^devingithub/', include('devingithub.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^watcher/', include('watcher.urls')),
    (r'^globoservico/', include('globoservico.urls')),
    (r'^globocom/', include('globojoinus.urls')),
    (r'^github/', include('processeja.urls')),
    (r'^admin/', include(admin.site.urls)),
)
