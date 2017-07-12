#!/usr/bin/env pytho
from distutils.core import setup

VERSION = "0.1.4"
setup(name='slick-bitcoinrpc',
    version=VERSION,
    description='Just another Python bitcoin-rpc client',
    long_description=open('README.rst').read(),
    url="https://github.com/barjomet/slick-bitcoinrpc",
    license="MIT",
    author = "Oleksii Ivanchuk",
    author_email = "barjomet@barjomet.com",
    keywords='bitcoin',
    packages=['slickrpc'],
    install_requires=['configobj',
                      'pycurl',
                      'ujson'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        ]
    )
