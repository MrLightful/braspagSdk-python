#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='cieloApi3',
    version='0.1.5',
    description='SDK API-3.0 Python Cielo',
    author='Thiago Malaquias',
    author_email='thiago.malaca@gmail.com',
    url='https://github.com/thiago-Malaca/API-3.0-Python',
    keywords='api3.0 cielo python sdk ecommerce',
    packages=find_packages(),
    install_requires=['requests'],
    license='MIT',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    )
)


setup(**settings)




# # -*- coding: utf-8 -*-
# from setuptools import setup

# setup(
#     name='cieloApi3',
#     version='0.1.1',
#     url='',
#     license='MIT License',
#     author='Thiago Malaquias',
#     author_email='',
#     keywords='api3.0 cielo python sdk ecommerce',
#     description=u'',
#     packages=['cielo.api30'],
#     install_requires=['requests'],
# )
