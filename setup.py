#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="i3-output-selector",
    packages=['i3_output_selector'],
    version="0.1.2",
    author="Krzysztof Warunek",
    author_email="krzysztof@warunek.net",
    description="GUI tool to change output for the current workspace in i3.",
    license="MIT",
    keywords="i3, workspace, selector, output",
    url="https://github.com/kwarunek/i3-output-selector",
    long_description=open('README.rst').read(),
    install_requires=['i3-py'],
    entry_points={
        'console_scripts': ['i3-output-selector = i3_output_selector.__main__:main']
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Operating System :: POSIX',
        'Development Status :: 3 - Alpha'
    ]
)
