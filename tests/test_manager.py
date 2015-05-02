# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
tests.test_manager
==================
'''
from django.test import TestCase
from django.core.cache import cache

from .models import Author, Book
from .factories import AuthorFactory, BookFactory


class NaturalKeyCacheManagerTests(TestCase):
    def setUp(self):
        cache.clear()
        self.author = AuthorFactory.create()
        self.isbn = '9783161484100'
        self.book = BookFactory.create(author=self.author, isbn=self.isbn)

    def test_lookup(self):
        with self.assertNumQueries(0):
            author = Author.cache.get(pk=self.author.pk)
        self.assertEqual(author.pk, self.author.pk)
        self.assertEqual(author.name, self.author.name)

    def test_related(self):
        with self.assertNumQueries(0):
            book = Book.cache.get(isbn=self.isbn)
        self.assertEqual(book.isbn, self.book.isbn)
        self.assertEqual(book.pk, self.book.pk)
        author = book.author
        self.assertEqual(author.pk, self.author.pk)
        self.assertEqual(author.name, self.author.name)

    def test_doesnotexist(self):
        # First attempt should cause cache miss
        with self.assertNumQueries(1):
            with self.assertRaises(Book.DoesNotExist):
                Book.cache.get(isbn='missing')

        # Second attempt should not
        with self.assertNumQueries(0):
            with self.assertRaises(Book.DoesNotExist):
                Book.cache.get(isbn='missing')
