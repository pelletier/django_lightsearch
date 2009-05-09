from django.db import models
from django.contrib import admin

class Author(models.Model):
    """
        An author who write a lot of tickets
        
        >>> jack = Author.objects.create(name="jack", address="jack@example.com", "I love Django")
        
    """
    name = models.CharField('Name', max_length=200)
    address = models.CharField('Address', max_length=200)
    bio = models.TextField('Life')
    
    class Lightsearch:
        fields = ['name', 'bio']

class Ticket(models.Model):
    author = models.ForeignKey('author')
    title = models.CharField('The title', max_length=200)
    content = models.TextField('I write my life here')
    
    class Lightsearch:
        fields = ['title', 'content']

admin.site.register([Author, Ticket])