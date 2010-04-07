"""
=======================
Lightsearch test suite
=======================

Be sure you have correctly installed lightsearch before running tests.

imports
-------

    >>> from utils import get_method, normalize_query, wildcardize
    >>> from views import search, perform_search
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

perform_search:

    >>> keywords = "mike OR jeff"
    >>> results = perform_search(keywords)
    >>> results.count()
    2

    >>> keywords = "hel*o -mike"
    >>> keywords = normalize_query(keywords)
    >>> results = perform_search(keywords, normalized=True)
    >>> results.count()
    1

perform_search with custom queryset:

    >>> from myapp.models import Author, Ticket
    >>> queryset = Ticket.objects.filter(author__pk=1) # Only mike's posts
    >>> results = perform_search("name", queryset=queryset)
    >>> results.count()
    1

    >>> from myapp.models import Author, Ticket
    >>> queryset = Ticket.objects.filter(author__pk=1) # Only mike's posts
    >>> results = perform_search("mike OR jeff", queryset=queryset)
    >>> results.count()
    0 

"""
