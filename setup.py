#!/usr/bin/python
# -*- coding:utf-8 -*-
from setuptools import setup
from source.main import VERSION
setup(
    name="mppf",
    version=VERSION,
    author="nsrx",
    author_email="cjsliuj@163.com",
    description="A simple command line tool for managing provisioning profiles.",
    url="https://github.com/cjsliuj/mppf",
    platforms = "any",
    packages = [
        'source'
    ],
    python_requires='>=3.5',
    install_requires=[
        'pyopenssl'
    ],
    entry_points={
        'console_scripts': [
            'mppf = source.main:exec',
        ]
    }
)