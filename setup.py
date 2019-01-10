#!/usr/bin/env python
from setuptools import setup
from setuptools.command.install import install
from distutils.dir_util import copy_tree
import os

LUA_SRC = 'scaii/lua'
LUA_DST = os.path.expanduser('~/.scaii/backends/sky-rts/maps/')

class PostInstallCommand(install):
    def run(self):
        print('Installing SCAII .lua files to {}'.format(LUA_DST))
        copy_tree(LUA_SRC, LUA_DST)
        install.run(self)


setup(name='scaii',
        version='0.3.0',
        description='Python bindings for https://github.com/SCAII',
        author='Larry Neal',
        author_email='nealla@lwneal.com',
        packages=[
            'scaii',
            'scaii/_internal_',
            'scaii/env',
            'scaii/protos',
            'scaii/sky_rts',
            'scaii/sky_rts/env',
            'scaii/sky_rts/env/scenarios',
            'scaii/sky_rts/protos',
            'scaii/env',
            'scaii/env/sky_rts',
            'scaii/env/sky_rts/env',
            'scaii/env/sky_rts/env/scenarios',
            'scaii/env/sky_rts/protos',
        ],
        package_data={
            'scaii': ['_internal_/libscaii_core.so',
                     ]
        },
      install_requires=[],
      cmdclass={
          'install': PostInstallCommand,
      },
)
