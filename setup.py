#!/usr/bin/env python
#-*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.0.123'

setup(
    name='django-webpay',
    version=version,
    description='Aplicación Django para integrar WebPay',
    author='FyF',
    author_email="dev@felicesyforrados.cl",
    url='https://github.com/felicesyforrados/django-webpay',
    license='MIT license',
    platforms = ['any'],
    packages=find_packages(),
    classifiers=[
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
     include_package_data=True,
     zip_safe=False,
)
