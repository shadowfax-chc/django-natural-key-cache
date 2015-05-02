# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
tests.factories
===============
'''
import factory
from factory import fuzzy

from tests.models import Author, Book


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = fuzzy.FuzzyText()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    title = fuzzy.FuzzyText()
    isbn = fuzzy.FuzzyText(length=13)
    author = factory.SubFactory(AuthorFactory)
