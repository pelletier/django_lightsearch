"""
=======================
Lightsearch test suite
=======================

Be sure you have correctly installed lightsearch before running tests.

utils
-----

get_method:

    >>> from utils import get_method
    >>> from django.conf import settings
    >>> settings.LIGHTSEARCH_METHOD = 'post'
    >>> get_method()
    'post'
    >>> settings.LIGHTSEARCH_METHOD = 'get'
    >>> get_method()
    'get'
    >>> settings.LIGHTSEARCH_METHOD = 'unknown'
    >>> get_method()
    'post'

normalize_query:

    >>> from utils import normalize_query
    >>> normalize_query('  just some   words "which   make" the   query  ')
    ['just', 'some', 'words', 'which make', 'the', 'query']
"""