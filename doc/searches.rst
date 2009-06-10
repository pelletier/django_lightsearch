.. _searches:

Perform searches
================

Requirements
------------

You must have installed and configured Lightsearch. See :ref:`installation`. 
Also, you must understand the way to use Lightsearch. You create a form and send
results to the URL of Lightsearch. See the example page.


Render a search form
--------------------

Lightsearch provides a tag to render a search form:

.. code-block:: django
   
   {% load lightsearch_forms %}
   {% lightsearch_searchform %}

The default template used to render the form is really dry and so ugly, but of 
course, you can override it.

Override the results page
-------------------------

So, you hate my *so* beautiful results page? Okay. Its template file is 
``lightsearch/search_results.html``. You have to know that Lightsearch add one 
variable to the context of the results page: ``results`` (surprising isn't it?).
``results`` is a ``ResultsContainer`` instance. The aim of the 
``ResultsContainer`` class is to make easy the management of the results of the 
search. Here is an example to print all the results:

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

It will contains some useful tags and filters to manage results. For now, the 
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

Have fun !