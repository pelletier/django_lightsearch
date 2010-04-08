.. _installation:

Installation
============

Download Ligthsearch
--------------------

First of all, you need to download the latest released version of Lightsearch.
Go to our `downloads section`_ then download the latest tagged version. If you 
don't understand what it mean or if you are too lazy, here is the direct link to
`download the 0.2 version`_.

.. _downloads section: http://bitbucket.org/Kizlum/django-lightsearch/downloads/
.. _download the 0.2 version: http://bitbucket.org/Kizlum/django-lightsearch/get/0.2.zip


Register the application
------------------------

It's just like every Django applications: edit your ``settings.py`` file and 
add **lightsearch** to the ``INSTALLED_APPS`` list. 


Configure the engine
--------------------

Stay in your ``settings.py`` file, and add the ``LIGHTSEARCH_MODELS`` setting. 
It is a list of tuples. Each tuple represents a model. Its first part is the 
verbose name of the model (ie: the human readable name) and the second is the 
link to the model (ie: something like <application_name>.<model>). Here is an 
example:

.. code-block:: python
   
   LIGHTSEARCH_MODELS = [
       # ('Verbose name', '<appname>.<model>'),
       ('Ticket', 'myapp.ticket'),
       ('Author', 'myapp.author'),
   ]

You also have to add the template directory of Lightsearch in the 
``TEMPLATE_DIRS`` setting. Here is an example:

.. code-block:: python

   # Those two lines are needed
   import os
   ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

   # A part of your settings.py there

   TEMPLATE_DIRS = (
                 os.path.join(ROOT_PATH, 'templates'), # This line doesn't matter. Just for example
                 os.path.join(ROOT_PATH, 'lightsearch', 'templates'), # Add this line
   )

   # The end of your setting.py

It's okay for the basic configuration of the ``settings.py`` file. If you want 
to tweak a bit more the engine, read the suitable part of the documentation.


Add the URLs
------------

You just have to include ``lightsearch.urls`` in you ``urls.py`` file:

.. code-block:: python

   (r'^search/', include('lightsearch.urls')),


Configure the models
--------------------

Now, you have to set which fields of your models have to be included in the 
search queries. So, open your ``models.py`` file(s) and add a ``Lightsearch`` 
class containing a ``fields`` list to each model you have added in your 
``settings.py``. Here is an example:

.. code-block:: python
   
   class Author(models.Model):
    """
        An author who write a lot of tickets
        
        >>> jack = Author.objects.create(name="jack", address="jack@example.com", bio="I love Django")
        >>> jack.name
        "jack"
        
    """
    name = models.CharField('Name', max_length=200)
    address = models.CharField('Address', max_length=200)
    bio = models.TextField('Life')
    
    def __unicode__(self):
        return '%s (%s)' % (self.name, self.address)
    
    class Lightsearch:
        fields = ['name', 'bio']

Once you have finished, you are ready to go.