#!/usr/bin/env python

from setuptools import setup

setup(name='scaii',
        version='0.1.0',
        description='Python bindings for https://github.com/SCAII',
        author='Larry Neal',
        author_email='nealla@lwneal.com',
        packages=[
            'scaii',
        ],
        package_data={
            'scaii': ['_internal_/libscaii_core.so',
                     ]
        },
      install_requires=[
          "requests",
      ],
)
