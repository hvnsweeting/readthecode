#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requisites = []

setup(
    name='readthecode',
    version='0.1.3',
    description='You read the doc, now better read the code',
    long_description=open('README.rst').read(),
    author='Viet Hung Nguyen',
    author_email='hvn@familug.org',
    url='https://github.com/hvnsweeting/readthecode',
    license='MIT',
    py_modules=['main'],
    classifiers=[
        'Environment :: Console',
    ],
    entry_points={
        'console_scripts': [
            'readthecode=main:cli',
            'rtc=main:cli',
        ],
    },
)
