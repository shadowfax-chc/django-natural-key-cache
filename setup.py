#!/usr/bin/env python
# vim: set et ts=4 sw=4 fileencoding=utf-8:

from setuptools import setup, find_packages

requirements = [
    'Django>=1.7',
]
test_requirements = [
    'nose>=1.3,<2',
]

setup(
    name='django-natural-key-cache',
    version='0.1',
    description='Cache manager for caching django models by natural keys',
    long_description='Cache manager for caching django models by natural keys',
    author='Timothy Messier',
    author_email='tim.messier@gmail.com',
    url='https://github.com/shadowfax-chc/django-natural-key-cache',
    packages=find_packages(exclude=('tests', 'doc')),
    package_dir={'natural_key_cache': 'natural_key_cache'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='django-natural-key-cache',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements,
)
