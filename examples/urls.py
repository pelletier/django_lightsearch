from django.conf.urls.defaults import *
from myapp.views import welcome

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', welcome), # The test page
    (r'^search/', include('lightsearch.urls')), # The lightsearch area
    (r'^admin/(.*)', admin.site.root), # The admin page to add fixtures
)
