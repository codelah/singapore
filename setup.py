import os, sys
from distutils.core import setup
from distutils.command.install import install as _install
from setuptools import setup


setup(
  name = 'singapore',
  packages = ['singapore'],
  version = '0.0.1',
  install_requires=[
        'xmltodict','requests',
        'onemap', 'nea_api'
  ],
  description = "Singapore",
  author = 'CodeSG',
  author_email = 'zhchua@gmail.com',
  url = 'https://github.com/codelah/singapore',
  keywords = ['data.gov.sg', 'python', 'wrapper', 'psi', 'nea', 'onemap', 'singapore'],
  classifiers = [],
)
