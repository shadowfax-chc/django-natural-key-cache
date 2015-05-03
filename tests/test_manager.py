# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
tests.test_manager
==================
'''
from django.test import TestCase
from django.core.cache import cache

from .models import Author, Book, Shelf
from .factories import AuthorFactory, BookFactory, ShelfFactory


class NaturalKeyCacheManagerTests(TestCase):
    '''
    Test using models with NaturalKeyCacheManager
    '''
    def setUp(self):
        cache.clear()
        self.author = AuthorFactory.create()
        self.isbn = '9783161484100'
        self.shelf = ShelfFactory.create(
            number=1,
            room='100a',
        )
        self.book = BookFactory.create(
            author=self.author,
            isbn=self.isbn,
            shelf=self.shelf,
        )

    def test_lookup_pk(self):
        '''
        Test looking up an object with a pk natural key.
        '''
        with self.assertNumQueries(0):
            author = Author.cache.get(pk=self.author.pk)
        self.assertEqual(author.pk, self.author.pk)
        self.assertEqual(author.name, self.author.name)

    def test_lookup_single_field(self):
        '''
        Test looking up an object with a single natural key.
        '''
        with self.assertNumQueries(0):
            book = Book.cache.get(isbn=self.isbn)
        self.assertEqual(book.isbn, self.book.isbn)
        self.assertEqual(book.pk, self.book.pk)

    def test_lookup_multi_field(self):
        '''
        Test looking up an object with multiple natural keys.
        '''
        with self.assertNumQueries(0):
            shelf = Shelf.cache.get(number=1, room='100a')
        self.assertEqual(shelf.number, self.shelf.number)
        self.assertEqual(shelf.room, self.shelf.room)
        self.assertEqual(shelf.pk, self.shelf.pk)
        with self.assertNumQueries(0):
            shelf = Shelf.cache.get(room='100a', number=1)
        self.assertEqual(shelf.number, self.shelf.number)
        self.assertEqual(shelf.room, self.shelf.room)
        self.assertEqual(shelf.pk, self.shelf.pk)

    def test_cache_miss(self):
        '''
        Test after a cache miss that the object gets cached.
        '''
        cache.clear()
        with self.assertNumQueries(1):
            Author.cache.get(pk=self.author.pk)
        with self.assertNumQueries(0):
            Author.cache.get(pk=self.author.pk)

    def test_foreign_key_access(self):
        '''
        Test accessing a foriegn keyed object after retrive from cache.
        '''
        with self.assertNumQueries(0):
            book = Book.cache.get(isbn=self.isbn)
        self.assertEqual(book.isbn, self.book.isbn)
        self.assertEqual(book.pk, self.book.pk)
        with self.assertNumQueries(0):
            author = book.author
        self.assertEqual(author.pk, self.author.pk)
        self.assertEqual(author.name, self.author.name)

    def test_doesnotexist(self):
        '''
        Test that DoesNotExist gets cached.
        '''
        # First attempt should cause cache miss
        with self.assertNumQueries(1):
            with self.assertRaises(Book.DoesNotExist):
                Book.cache.get(isbn='missing')

        # Second attempt should not
        with self.assertNumQueries(0):
            with self.assertRaises(Book.DoesNotExist):
                Book.cache.get(isbn='missing')
