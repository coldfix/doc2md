# encoding: utf-8
from setuptools import setup
from distutils.spawn import find_executable
from subprocess import check_output

# Generate markdown from docstring
try:
    import doc2md
    md = doc2md.doc2md(doc2md.__doc__, "doc2md", toc=False)
except ImportError:
    with open('README.md') as f:
        md = f.read()

# Generate .rst document for PyPi
try:
    import pypandoc
    long_description = pypandoc.convert(md, 'rst', format='md')
except ImportError:
    long_description = None

# invoke distutils
setup(
    name='doc2md',
    version='0.1.0',
    description='Lightweight docstring to markdown converter',
    long_description=long_description,
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

