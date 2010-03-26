.. _searches:

Perform searches
================

Requirements
------------

You must have installed and configured Lightsearch. See :ref:`installation`. 
Also, you must understand how to use Lightsearch. You create a form and send
results to the URL of Lightsearch using ``POST``. See the example page included
in the zip file.


Render a search form
--------------------

Lightsearch provides a tag to render a search form:

.. code-block:: django
   
   {% load lightsearch_forms %}
   {% lightsearch_searchform %}

The default template used to render the form is really dry and ugly, but of 
course, you can override it.

Override the results page
-------------------------

So, you hate my *so* beautiful results page? Okay. Its template file is 
``lightsearch/search_results.html``. You have to know that Lightsearch add one 
variable to the context of the results page: ``results`` (surprising isn't it?).
``results`` is a ``ResultsContainer`` instance. The aim of the 
``ResultsContainer`` class is to make the management of the results of the 
search easy. Here is an example to print all the results:

.. code-block:: django

   {% for model in results.sets %}
   <h2>{{model.name}}</h2>
   <p>
        <ul>
                {% for item in model.results %}
                <li>{{item}}</li>
                {% endfor %}
        </ul>
   </p>
   {% endfor %}

As you can see, the results are grouped by model. It's for now the only 
structure provided by Lightsearch.

Template tags
-------------

In the results page, you can load ``lightsearch_data``:

.. code-block:: django

   {% load lightsearch_data %}

It will contain some useful tags and filters to manage results. For now, the 
only one tag is ``models_type``. Here is its syntax:

.. code-block:: django

   {% models_type in results as variable %}

``variable`` will contain a list of the name of models where results have been 
found. Here is an example:

.. code-block:: django

   {% models_type in results as mt %}
   Results found in:
   <ul>
        {% for type in mt %}
        <li>{{type}}</li>
        {% endfor %}
        </ul>

Limiting the search pool
------------------------

It is possible to pass a queryset to lightsearch in order to specify a subset
of models to search from at runtime.

For example, with the following models:

.. code-block:: python

   class Category(models.Model):
       title = models.CharField(max_length=50)
       description = models.TextField()
   
   class BlogPost(models.Model):
       title = models.Char(max_length=100)
       entry = models.TextField()
       category = models.ForiegnKey(Category)
       
It would be desireable to allow users to search for BlogPosts within a
particular category.

To do this, create a queryset in your view which defines the models to be searched,
then pass that queryset to the lightsearch.views.perform_search.

.. code-block:: python

   from lightsearch.views import perform_search
   
   queryset = BlogPost.objects.filter(category__pk=0)
   results = perform_search(keywords, queryset=queryset)

Here is a more complete example of a possible view. Here a form has been created which
sends a GET request with the search keywords in key `c` and the `Category.pk` in
key `c`.

.. code-block:: python

   # views.py
   
   from lightsearch.views import perform_search
   
   def search_by_category(request):
       # leaving out error checking, etc. for clarity.
       keywords = request.GET.get('q', None)
       category_pk = request.GET.get('c', None)
       
       if keywords and category_pk:
           queryset = BlogPost.objects.filter(category__pk=category_pk)
           
           # pass the specific queryset to perform_search()
           results = perform_search(keywords, queryset=queryset)
           
           return render_to_response('lightsearch/search_results.html',
                                     {'results': results},
                                     context_instance=RequestContext(request))


The results are returned in the same format as usual, so you can most likely use the same template.


Have fun !