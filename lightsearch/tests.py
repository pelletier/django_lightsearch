"""
=======================
Lightsearch test suite
=======================

Be sure you have correctly installed lightsearch before running tests.

imports
-------

    >>> from utils import get_method, normalize_query, wildcardize
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
    
wildcardize:
    
    >>> wildcardize('wil*card')
    'wil[\\\\w\\\\d\\\\-_]*card'
    
views
-----

search:

    >>> data = {'query': 'je*f'}
    >>> f = SearchForm(data)
    >>> if f.is_valid():
    ...    pass
    >>> results = search(f)
    >>> results.count()
    1
    
    >>> data = {'query': 'hel*o -mike'}
    >>> f = SearchForm(data)
    >>> if f.is_valid():
    ...    pass
    >>> results = search(f)
    >>> results.count()
    1
    
    >>> data = {'query': 'mike OR jeff'}
    >>> f = SearchForm(data)
    >>> if f.is_valid():
    ...    pass
    >>> results = search(f)
    >>> results.count()
    2

    >>> data = {'query': 'mike OR'}
    >>> f = SearchForm(data)
    >>> if f.is_valid():
    ...    pass
    >>> results = search(f)
    >>> results.count()
    1
    
    >>> data = {'query': 'OR mike'}
    >>> f = SearchForm(data)
    >>> if f.is_valid():
    ...    pass
    >>> results = search(f)
    >>> results.count()
    1

"""