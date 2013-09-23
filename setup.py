# encoding: utf-8
from setuptools import setup
import sys

def long_description():
    """Generate .rst document for PyPi."""
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc', dest="doc",
            action="store_true", default=False)
    args, sys.argv = parser.parse_known_args(sys.argv)
    if args.doc:
        import doc2md, pypandoc
        md = doc2md.doc2md(doc2md.__doc__, "doc2md", toc=False)
        long_description = pypandoc.convert(md, 'rst', format='md')
    else:
        return None

# invoke distutils
setup(
    name='doc2md',
    version='0.1.0',
    description='Lightweight docstring to markdown converter',
    long_description=long_description(),
    author='Thomas Gläßle',
    author_email='t_glaessle@gmx.de',
    url='https://github.com/coldfix/doc2md',
    license='WTFPL',
    py_modules=['doc2md',],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)

