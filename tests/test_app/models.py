# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
tests.models
============
'''
from django.db import models

from natural_key_cache.cache_manager import NaturalKeyCacheManager


class Author(models.Model):
    '''
    Test model with only pk/id as natural key
    '''
    objects = models.Manager()
    cache = NaturalKeyCacheManager()

    name = models.CharField(max_length=128)


class Shelf(models.Model):
    '''
    Test model with two fields as natural keys.
    '''
    objects = models.Manager()
    natural_keys = (
        'number',
        'room',
    )
    cache = NaturalKeyCacheManager(natural_keys)
    number = models.IntegerField()
    room = models.CharField(max_length=4)

    class Meta:  # pylint: disable=old-style-class,no-init
        ''' Meta '''
        unique_together = (
            'number',
            'room',
        )


class Book(models.Model):
    '''
    Test model with one fields as natural key.

    Also has a foreign key to another model.
    '''
    objects = models.Manager()
    natural_keys = (
        'isbn',
    )
    cache = NaturalKeyCacheManager(natural_keys)
    title = models.CharField(max_length=128)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author)
    shelf = models.ForeignKey(Shelf)
