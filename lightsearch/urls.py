from django.conf.urls.defaults import *
from views import search_callback

urlpatterns = patterns('',
    url(r'^$', search_callback, name='lightsearch'),
)
