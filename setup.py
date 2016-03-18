#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Igalia S.L.
#
# Distributed under terms of the GPLv3 or, at your option,
# under the terms of the Apache 2.0 license.

from setuptools import setup

if __name__ == "__main__":
    setup(
        name="indicium-git",
        version="0.1.0a0",
        description="Generic key-value interface to a Git repository",
        author="Adrián Pérez de Castro",
        author_email="aperez@igalia.com",
        url="https://github.com/aperezdc/indicium-git",
        license=["GPLv3", "Apache-2.0"],
        packages=["indicium.git"],
        install_requires=[
            "dulwich>=0.12",
            "indicium>=0.1.0a2",
        ],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "License :: OSI Approved :: Apache Software License",
        ],
        test_suite="indicium.git.test",
    )
