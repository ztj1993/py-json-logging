# -*- coding: utf-8 -*-

import os.path
import re

from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8')
readme = f.read()
f.close()

f = open(os.path.join(os.path.dirname(__file__), 'ZtjJsonLogging.py'), encoding='utf8')
version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)
f.close()

setup(
    name='py-ztj-json-logging',
    version=version,
    description='python json logging logger formatter',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=['ZtjJsonLogging'],
    url='https://github.com/ztj1993/py-json-logging',
    author='ZhangTianJie',
    author_email='ztj1993@gmail.com',
    keywords='json logging logger formatter',
    license='MIT License',
)
