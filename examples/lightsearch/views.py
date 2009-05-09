from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render_to_response as render
from django.template import RequestContext
from django.db.models import get_model
from lightsearch.utils import get_method, normalize_query
from lightsearch.forms import SearchForm

import re

def search(request):
    """Handle the search request and search"""
    method=get_method().upper()
    if request.method == method:
        form = SearchForm(getattr(request, method))
        if form.is_valid():
            results = [] # The list of results starts empty
            # Normalize the query
            keywords = normalize_query(form.cleaned_data['query'])
            # Create a regexp containing the keywords
            print '|'.join(keywords)
            regexp = re.compile('|'.join(keywords), re.IGNORECASE)
            # Retrieve the list of searchable models
            models = settings.LIGHTSEARCH_MODELS
            # For each searchable model
            for model in models:
                # The model link is <appname>.<model>
                link = model[1]
                # It's verbose name
                name = model[0]
                # Retrieve this model
                object = get_model(*link.split('.'))
                if object is None:
                    raise Exception, "This model (%s) doesn't exist!" % model
                # Create a new instance of the model
                instance = object()
                # Get the fields
                fields = instance.Lightsearch.fields
                # Retrieve the objects from the database
                objects = object.objects.all()
                # Make the list of results concerning this model empty
                objects_results = []
                # Loop on objects in the databse
                for obj in objects:
                    for field in fields: # For each field allowed
                        content = getattr(obj, field) # Retrieve the content
                        if regexp.findall(content):
                            # If one of the keywords matches
                            objects_results.append(obj) # Add this object
                            break # Leave the looping on fields
                # Once all objects of this model have been checked
                # add the results to the global results list
                results.append((name, objects_results))
            # Finally, render the pages
            return render('lightsearch/search_results.html',
                            {'results': results},
                            context_instance=RequestContext(request))
            
    return HttpResponseRedirect('/') # TODO: better redirection