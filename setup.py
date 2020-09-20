# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in webapp/__init__.py
from webapp import __version__ as version

setup(
	name='webapp',
	version=version,
	description='Web Application',
	author='Dhamu',
	author_email='pdhamodharanit@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
