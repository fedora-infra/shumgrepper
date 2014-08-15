#!/usr/bin/env python

PROJECT = 'shumgrepper'

VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.md', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='A webapp for summershum',
    long_description=long_description,

    author='Pierre-Yves Chibon and Charul',
    author_email='charul.agrl@gmail.com',

    url='https://github.com/fedora-infra/shumgrepper',
    download_url='https://github.com/fedora-infra/shumgrepper/tarball/master',

    classifiers=['Development Status :: 1 - Beta',
                 'License :: gplv2+',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],
    scripts=[],
    provides=[],
    install_requires=[
        "Flask",
        "fedmsg>=0.7.0",
        "fedmsg_meta_fedora_infrastructure",
        "M2Crypto",
        "M2ext",
        "docutils",
        "Flask-WTF",
    ],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
