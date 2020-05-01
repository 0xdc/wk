#!/usr/bin/env python

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='wk',
	version='0.6',
	packages=find_packages(),
	include_package_data=True,
	long_description=README,
	url="https://github.com/0xdc/wk",
	author="Daniel Cordero",
	author_email="well-known@0xdc.io",
)
