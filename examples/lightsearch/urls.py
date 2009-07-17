"""
URLs map
"""

from django.conf.urls.defaults import url, patterns
from lightsearch.views import search_callback

urlpatterns = patterns('',
    url(r'^$', search_callback, name='lightsearch'),
)
