from django import template
from django.core.urlresolvers import reverse
from lightsearch.forms import SearchForm
from lightsearch.utils import get_method

register = template.Library()

@register.inclusion_tag('lightsearch/search_form.html')
def lightsearch_searchform():
    """Returns the search form"""
    base_url = reverse('lightsearch')
    method = get_method()
    return { 'form': SearchForm(), 'base_url': base_url, 'method': method }