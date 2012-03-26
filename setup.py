#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Get text from README.txt
readme_text = file('README.rst', 'rb').read()

setup(name          = 'python-safe',
      version       = '0.1',
      description   = 'Spatial Analysis F* Engine',
      license       = 'BSD',
      keywords      = 'gis vector feature raster data',
      author        = 'Ole Nielsen',
      author_email  = 'ole.moller.nielsen@gmail.com',
      maintainer        = 'Ariel Núñez',
      maintainer_email  = 'ingenieroariel@gmail.com',
      url   = 'http://github.com/AIFDR/safe',
      long_description = readme_text,
      packages = ['safe'],
      install_requires  = [],
      tests_require = ['nose'],
      test_suite = 'nose.collector',
      classifiers   = [
        'Development Status :: 5 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
        ],
)
