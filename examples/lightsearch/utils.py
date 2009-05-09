from django.conf import settings

def get_method():
    """
        Returns the method which must be used to send the form.
        'post' is the default value.
        
        >>> django.conf import settings
        >>> settings.LIGHTSEARCH_METHOD = 'post'
        >>> get_method()
        'post'
        >>> settings.LIGHTSEARCH_METHOD = 'get'
        >>> get_method()
        'get'
        >>> settings.LIGHTSEARCH_METHOD = 'unknown'
        'post'
        
    """
    
    method = settings.LIGHTSEARCH_METHOD
    if method.lower() != 'post' and method.lower() != 'get':
        return 'post' # POST as default
    else:
        return method