#!/usr/bin/env python

from setuptools import setup

setup(
    install_requires=[
        # 'target-core==0.1.0',
        'target-core @ git+ssh://git@gitlab.com/adam614/target-core.git',
        'boto3==1.26.82'
    ]
)
