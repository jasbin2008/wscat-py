#!/usr/bin/env python

#
# Copyright (c) 2013, Digium, Inc.
#

import os

from setuptools import setup

setup(
    name="wscat-py",
    version="0.0.1",
    license="BSD 3-Clause License",
    description="Command line WebSocket client",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.md")).read(),
    author="Digium, Inc.",
    url="https://github.com/leedm777/wscat-py",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    setup_requires=['nose>=1.3'],
    tests_require=['coverage', 'tissue'],
    install_requires=['websocket-client'],
    entry_points="""
    [console_scripts]
    wscat = wscat.wscat:main
    """
)
