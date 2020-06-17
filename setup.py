#!/usr/bin/env python
import os
import subprocess
import time
from setuptools import find_packages, setup
import powerpack


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


if __name__ == '__main__':
    setup(
        name='powerpack',
        version=powerpack.__version__,
        description='A robust collection of useful scripts',
        long_description=readme(),
        author='Li Shenggui',
        keywords='Python, scripts',
        packages=find_packages(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
        license='Apache License 2.0',
        install_requires=powerpack.read_lines('requirements/requirements.txt'),
        zip_safe=False,
        entry_points={'console_scripts': ['powerpack = powerpack.command:cli']})
