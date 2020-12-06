# -*- coding: utf-8 -*-

import setuptools

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open("requirements.txt", "r") as fh:
   requirements = fh.readlines()

setup(
    name='iomyfiles',
    version='0.0.0',
    description='collections of tools to load/import different file format for power electronic',
    long_description=readme,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='riccardo tinivella',
    author_email='tinix84@gmail.com',
    url='https://github.com/tinix84/iomyfiles',
    license=license,
    packages=setuptools.find_packages(exclude=('data', 'tests', 'docs', 'mfiles')),
    install_requires=[req for req in requirements if req[:2] != "# "],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ], 
)
