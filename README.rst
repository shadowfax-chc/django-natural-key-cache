Django Natural Key Cache
========================

|build-status|

Cache models via natural keys.

.. |build-status| image:: http://img.shields.io/travis/shadowfax-chc/django-natural-key-cache/master.svg?style=flat
    :alt: Build Status
    :scale: 100%
    :target: https://travis-ci.org/shadowfax-chc/django-natural-key-cache


Quick Start
-----------

Add manager to model.

.. code-block:: python

    from django.db import models
    from natural_key_cache.cache_manager import NaturalKeyCacheManager

    class MyModel(models.Model):
        # Define natural keys, this can be ommited if id/pk is the natural key
        natural_keys = (
            'nat_key',
        )
        cache = NaturalKeyCacheManager(natural_keys)
        nat_key = models.CharField(max_length=32, unique=True)

Then access the cached model via the new manager.

.. code-block:: python

    MyModel.cache.get(nat_key='unique_instance')
