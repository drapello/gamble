from django.conf.urls.defaults import *
from globojoinus.views import quemfaz
urlpatterns = patterns('django.views.generic.simple',
    (r'quemfaz', quemfaz),
)
    