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
    cache = NaturalKeyCacheManager()

    name = models.CharField(max_length=128)


class Book(models.Model):
    '''
    Test model with one fields as natural key.

    Also has a foreign key to another model.
    '''
    natural_keys = (
        'isbn',
    )
    cache = NaturalKeyCacheManager(natural_keys)
    title = models.CharField(max_length=128)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author)
