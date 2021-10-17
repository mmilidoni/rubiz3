#!/usr/bin/env python

from pip.req import parse_requirements
from setuptools import setup

install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="Rubiz",
    version="0.1-alpha",
    description="Simple, versatile address book",
    author="Michele Milidoni",
    author_email="michelemilidoni@gmail.com",
    url="https://github.com/mmilidoni/rubiz3",
    install_requires=reqs
)
