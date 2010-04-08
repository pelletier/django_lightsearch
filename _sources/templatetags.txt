.. _templatetags:

Template tags
=============

Here is the complete template tags list. Each tag is illustrated by a small code
example.

perform_search
--------------

**Part of** ``lightsearch_actions``.

This tag performs a search then returns the results as a ResultsContainer 
object.

.. code-block:: django

   {% load lightsearch_actions %}
   {% perform-search my keywords as myvar %}


models_type
-----------

**Part of** ``lightsearch_data``.

Returns a list containing the verbose name of each model with at least one 
result.

.. code-block:: django

   {% load lightsearch_data %}
   {% models_type in results as mt %}


lightsearch_searchform
----------------------

**Part of** ``lightsearch_forms``.

Displays the default search form. You can tweak it by modifying the ``templates/search_form.html`` file.

.. code-block:: django

   {% load lightsearch_forms %}
   {% lightsearch_forms %}