"""
Tags to interact with the search engine
"""

from django import template
from lightsearch.utils import normalize_query as norm
from lightsearch.views import perform_search as search_view

REGISTER = template.Library()

class SearchNode(template.Node):
    """Template node to use the template context"""
    def __init__(self, keywords, var_name):
        template.Node.__init__()
        self.keywords = norm(" ".join(keywords))
        self.var_name = var_name

    def render(self, context):
        """Add the result to the template context"""
        context[self.var_name] = search_view(self.keywords, normalized=True)
        return ''

def perform_search(parser, token):
    """
        Returns the results of the search using the given keywords.

        Usage:
        {% perform_search my keywords -here as results %}
    """

    # Get the bits
    bits = token.contents.split()
    len_bits = len(bits)

    # Check the syntax
    if not len_bits >= 4:
        raise template.TemplateSyntaxError("%s tag needs 3 arguments" % bits[0])
    if not bits[len_bits-2] == "as":
        raise template.TemplateSyntaxError('The penultimate must be "as"')

    # Compute
    return SearchNode(bits[1:len_bits-2], bits[len_bits-1])

REGISTER.tag(perform_search)
