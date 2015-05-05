#!/usr/bin/env python

from setuptools import setup

__version__ = None  # to satisfy Linter
with open('csr/version.py') as f:
    exec(f.read())

setup(
    name='csr',
    version=__version__,
    packages=['csr'],
    install_requires=[
        'Flask',
        'sqlalchemy',
        'Flask-Login',
    ],
    include_package_data=True,
    description='Python program to allow tracking of notes against customers',
    author='Jordan Brennan',
    maintainer='Jordan Brennan',
    zip_safe=False,
)
