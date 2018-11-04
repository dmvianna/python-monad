# setup.py

from setuptools import setup, find_packages
from os import path
from io import open


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'python-monad'
    ,version = '0.0.0'
    ,description = 'Haskell Maybe and Either types implemented as Python classes'
    ,long_description = long_description
    ,long_description_content_type = 'text/markdown'
    ,author = 'Daniel Vianna'
    ,author_email = 'dmlvianna@gmail.com'
    ,license = 'MIT'
    ,classifiers=[
        'Development Status :: 3 - Alpha'
        ,'Intended Audience :: Developers'
        ,'License :: OSI Approved :: MIT License'
        ,'Programming Language :: Haskell'
        ,'Topic :: Software Development :: Object Brokering'
        ,'Programming Language :: Python :: 3'
    ]
    ,keywords = 'error-handling development'
    ,project_urls = dict(
        Source = 'https://github.com/dmvianna/python-monad'
    )
)
    
