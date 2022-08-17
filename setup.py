#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gviejo
# @Date:   2022-08-17 12:12:25
# @Last Modified by:   gviejo
# @Last Modified time: 2022-08-17 12:22:48

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

# with open('docs/HISTORY.md') as history_file:
#     history = history_file.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("requirements_dev.txt") as f:
    requirements_dev = f.read().splitlines()

setup(
    author="Guillaume Viejo",
    author_email="guillaume.viejo@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Logging manager for data analysis with pynapple",
    install_requires=requirements,
    extras_require=dict(dev=requirements_dev),
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords="neuroscience",
    name="pynalog",
    packages=find_packages(include=["pynalog", "pynalog.*"]),
    test_suite="tests",
    tests_require=["pytest"],
    url="https://github.com/PeyracheLab/pynalog",
    version="v0.0.1",
    zip_safe=False,
    long_description_content_type="text/markdown",
)
