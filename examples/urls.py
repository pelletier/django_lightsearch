from django.conf.urls.defaults import *
from myapp.views import welcome, templatetags

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # The test page
    (r'^$', welcome),
    # The lightsearch area
    (r'^search/', include('lightsearch.urls')),
    # Test the templatetags
    (r'^templatetags/', templatetags),
    # The admin page to add fixtures
    (r'^admin/(.*)', admin.site.root),
)
