#!/usr/bin/env python

from setuptools import setup

setup(name='scaii',
        version='0.1.0',
        description='Python bindings for https://github.com/SCAII',
        author='Larry Neal',
        author_email='nealla@lwneal.com',
        packages=[
            'scaii',
            'scaii/env',
            'scaii/protos',
            'scaii/sky_rts',
            'scaii/sky_rts/env',
            'scaii/sky_rts/env/scenarios',
            'scaii/sky_rts/protos',
            'scaii/env',
            'scaii/env/sky_rts',
            'scaii/env/sky_rts/protos',
            'scaii/env/sky_rts/env',
        ],
        package_data={
            'scaii': ['_internal_/libscaii_core.so',
                     ]
        },
      install_requires=[
          "requests",
      ],
)
