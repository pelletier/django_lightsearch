from django.db import models
from django.contrib import admin

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

class Ticket(models.Model):
    """
        A ticket written by an author
        
        >>> jack = Author.objects.create(name="jack", address="jack@example.com", bio="I love Django")
        >>> novel = Ticket.objects.create(author=jack, title="Hello", content="Bio")
        >>> novel.author.name
        "jack"
    """
    
    author = models.ForeignKey('author')
    title = models.CharField('The title', max_length=200)
    content = models.TextField('I write my life here')
    
    def __unicode__(self):
        return '%s written by %s' % (self.title, self.author.name)
    
    class Lightsearch:
        fields = ['title', 'content']

admin.site.register([Author, Ticket])