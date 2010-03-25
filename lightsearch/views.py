"""
The Lightsearch code.
The perform_search do the big job. The search function is just a bridge between 
forms and searching.
"""

from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render_to_response as render
from django.template import RequestContext
from django.db.models import get_model
from lightsearch.utils import get_method, normalize_query
from lightsearch.utils import wildcardize as w
from lightsearch.forms import SearchForm
from lightsearch.classes import ResultsContainer

import re

MINUS_CAPTURE_REGEXP = re.compile(r'^-([\w\d\-_\*]*)', re.IGNORECASE)

def search(form):
    """Normalize the query from a form then perform the search"""
    keywords = normalize_query(form.cleaned_data['query'])
    return perform_search(keywords, normalized=True)

def perform_search(keywords, normalized=False, queryset=None):
    """Perform the search"""
    
    results = [] # The list of results starts empty
    actions_list = []

    if not normalized:
        keywords = normalize_query(keywords)
    
    # All keywords 'OR' which aren't followed and preceded by something MUST be
    # ignored.
    #
    # test OR world # OK!
    # test OR # Ignored
    # OR test # Ignored
    for i, keyword in enumerate(keywords):
        if keyword == 'OR' and not(i > 0 and i < len(keywords)-1):
            keywords.pop(i)

    # For each keyword
    for i, keyword in enumerate(keywords):
        if keyword == 'OR':
            # This keyword is an 'OR' statement and isn't the first nor the last
            # keyword
            kwds = [w(keywords[i-1]), w(keywords[i+1])]
            regexp = re.compile('|'.join(kwds), re.IGNORECASE)
            actions_list.append(('required', regexp))
        elif not keyword == 'OR':
            test = MINUS_CAPTURE_REGEXP.search(keyword)
            if test:
                # This keyword is an exclusion keyword
                regexp = re.compile(w(test.group(1)), re.IGNORECASE)
                actions_list.append(('not', regexp))
            else:
                leave = False
                if i+1 < len(keywords):
                    if keywords[i+1] == 'OR':
                        leave = True
                if not leave and i > 0:
                    if keywords[i-1] == 'OR':
                        leave = True
                if not leave:
                    regexp = re.compile(w(keyword), re.IGNORECASE)
                    actions_list.append(('required', regexp))

    models = [] # we'll store actual model references here, along with the queryset to use

    if queryset:
        models.append((queryset.model, queryset))
        name = queryset.model._meta.verbose_name.capitalize()

    else:
        model_names = settings.LIGHTSEARCH_MODELS

        for full_name in model_names:
            # The model link is <appname>.<model>
            link = full_name[1]
            # It's verbose name
            name = full_name[0]
            # Retrieve the model
            object = get_model(*link.split('.'))
            if object is None:
                raise Exception, "This model (%s) doesn't exist!" % full_name
            models.append((object, object.objects.all()))

    for object, objects in models:                
        # Create a new instance of the model
        instance = object()
        # Get the fields
        fields = instance.Lightsearch.fields

        # Make the list of results concerning this model empty
        objects_results = []
    
        # Loop on objects in the database
        for obj in objects:
            validated_actions = [ False for i in xrange(len(actions_list)) ]
            
            for i, action in enumerate(actions_list):
                if action[0] == 'not':
                    validated_actions[i] = True
            
            add_it = True
            for field in fields: # For each field allowed
                content = getattr(obj, field)

                for i, action in enumerate(actions_list):
                    result = action[1].findall(content)
                    
                    if result and action[0] == 'required':
                        # This action is needed and it returned something
                        validated_actions[i] = True
                        
                    elif result and action[0] == 'not':
                        # This action mustn't be validated and it returned
                        # something
                        validated_actions[i] = False
            
            for valids in validated_actions:
                if not valids:
                    add_it = False
                    break
            
            if add_it: # Finally, if the object validate all the conditions,
                objects_results.append(obj) # add it
            
        results.append((name, objects_results))
    container = ResultsContainer(results)
    return container

def search_callback(request):
    """Handle the search request"""
    
    method = get_method().upper()
    if request.method == method:
        form = SearchForm(getattr(request, method))
        if form.is_valid():
            container = search(form)
            return render('lightsearch/search_results.html',
                            {'results': container},
                            context_instance=RequestContext(request))
            
    return HttpResponseRedirect('/')
