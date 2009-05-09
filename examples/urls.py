from django.conf.urls.defaults import *
from myapp.views import welcome

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # The test page
    (r'^$', welcome),
    # The lightsearch area
    (r'^search/', include('lightsearch.urls')),
    # The admin page to add fixtures
    (r'^admin/(.*)', admin.site.root),
)
