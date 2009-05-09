from django import template
from lightsearch.forms import SearchForm
from lightsearch.utils import get_method, get_base_url

register = template.Library()

@register.inclusion_tag('lightsearch/search_form.html')
def lightsearch_searchform():
    """Returns the search form"""
    base_url = get_base_url()
    method = get_method()
    return { 'form': SearchForm(), 'base_url': base_url, 'method': method }