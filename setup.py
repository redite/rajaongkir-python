#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
  name='RajaOngkir',
  packages=['RajaOngkir'],
  version='1.0.0',
  description='Python Client for RajaOngkir.com API',
  author='Widnyana',
  author_email='wid@widnyana.web.id',
  url='https://github.com/kalarau/rajaongkir',
  download_url='https://github.com/kalarau/rajaongkir/archive/master.zip',
  keywords=['ongkir', 'rajaongkir', 'JNE', 'TIKI', 'Pos'],
  classifiers=[],
  install_requires=[
    'requests>=2.8.1'
  ]
)
