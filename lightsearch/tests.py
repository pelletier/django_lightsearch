"""
=======================
Lightsearch test suite
=======================

Be sure you have correctly installed lightsearch before running tests.

imports
-------

    >>> from utils import get_method, normalize_query
    >>> from views import search
    >>> from forms import SearchForm
    >>> from django.conf import settings

utils
-----

get_method:

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

    >>> normalize_query('  just some   words "which   make" the   query  ')
    ['just', 'some', 'words', 'which make', 'the', 'query']
    
views
-----

search:

    >>> data = {'query': 'he*o test'}
    >>> f = SearchForm(data)
    >>> if f.is_valid():
    ...    pass
    >>> results = search(f)
    >>> results.count()
    2

"""