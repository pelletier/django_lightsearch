from django.conf.urls.defaults import *
from views import search 

urlpatterns = patterns('',
    url(r'^$', search, name='lightsearch'),
)
