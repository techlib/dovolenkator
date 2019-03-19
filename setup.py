#!/usr/bin/python3 -tt

from setuptools import setup
import os.path

setup(
    name = 'dovolenkator',
    version = '1',
    author = 'NTK',
    description = ('tool to track remaining occupational leave'),
    license = 'MIT',
    keywords = 'API occupational leave',
    url = 'http://github.com/techlib/dovolenkator',
    include_package_data = True,
    package_data = {
        '': ['*.png', '*.js', '*.html'],
    },
    packages = [
        'dovolenkator',
    ],
    classifiers = [
        'License :: OSI Approved :: MIT License',
    ],
    scripts = ['dovolenkator-daemon']
)


# vim:set sw=4 ts=4 et:
# -*- coding: utf-8 -*-
