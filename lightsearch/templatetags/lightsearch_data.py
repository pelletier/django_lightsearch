"""
Templatetags built to use search results in templates.
"""
from django import template


register = template.Library()

class ModelsTypeNode(template.Node):
    """The node for templates"""
    def __init__(self, results, var_name):
        template.Node.__init__(self)
        self.results = results
        self.var_name = var_name
    
    def render(self, context):
        """Render the node in the template : add the variable to the context"""
        names = []
        models_type_list = context[self.results]
        for item in models_type_list.sets:
            names.append(item.name)
        context[self.var_name] = names
        return ''

def models_type(parser, token):
    """
        Returns a list containing the verbose name of each model with at least
        one result
        
        Usage:
        {% models_type in results as mt%}
    """
    
    # Get the bits
    bits = token.contents.split()
    len_bits = len(bits)
    
    # Check the syntax
    if not len_bits == 5:
        raise template.TemplateSyntaxError("%s tag needs 4 arguments" % bits[0])
    if not bits[1] == 'in':
        raise template.TemplateSyntaxError('The first argument must be "in"')
    if not bits[3] == 'as':
        raise template.TemplateSyntaxError('The fourth argument must be "as"')
    
    # Compute
    return ModelsTypeNode(bits[2], bits[4])
    
register.tag(models_type)
