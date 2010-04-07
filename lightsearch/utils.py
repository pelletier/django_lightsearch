"""
Multiple functions to simplify the code.
"""

from django.conf import settings
from django.core.urlresolvers import reverse

import re

def get_method():
    """
        Returns the method which must be used to send the form.
        'post' is the default value.
    """
    try:
        method = settings.LIGHTSEARCH_METHOD
    except AttributeError:
        return 'post'
    
    if method.lower() != 'post' and method.lower() != 'get':
        return 'post' # POST as default
    else:
        return method
        
def get_base_url():
    """
        Returns the base URL of lightsearch
    """
    return reverse('lightsearch')
    
def normalize_query(query):
    """
        Normalize the given query (ie: remove useless spaces, split etc...)
    """
    result = []
    regexp = re.compile(r'"([^"]+)"|(\S+)')
    
    for match in regexp.findall(query):
        if match[0]:
            result.append(match[0])
        elif match[1]:
            result.append(match[1])
        else:
            pass
    return result

def wildcardize(key):
    """
        Modify a keyword to be regexp-ready
    """
    return key.replace('*', r'[\w\d\-_]*')