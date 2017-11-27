## doc2md

Very lightweight docstring to Markdown converter.

- [Project status](#project-status)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [API](#api)

### Project status

I stopped using this package and therefore will not push any updates (I now
usually write README.rst manually). Nonetheless, you may still find it useful.
Should you encounter bugs or have improvements, feel free to submit a PR. If
you want to take over maintenance, feel free to contact me.

For a more feature-rich and well maintained alternative, see:

- https://github.com/NiklasRosenstein/pydoc-markdown/ (I didn't try it)


### Installation

No installation necessary. However, if you want:

```bash
    $ pip install doc2md
```


### Usage

Simplistic utility to extract docstrings from a module or class and throw
them into a simple [GitHub Flavoured Markdown](md) document. Its purpose is
to quickly generate `README.md` files for small projects.

[md]: https://help.github.com/articles/github-flavored-markdown

You can run this script from the command line like:

```bash
    $ doc2md.py [-a] [--no-toc] [-t title] [-d depth] module-name [class-name]         > README.md
```

At the moment  this is suited only  for a very specific use  case. It is
hardly forseeable, if I will decide to improve on it in the near future.

For a simple example output document, see the generated README (i.e. the
github frontpage). It is extracted from the `doc2md.py` file using this
very utility:

```bash
    $ ./doc2md.py -a -d1 doc2md > README.md
```


### License

Copyright © 2013-2017 Thomas Gläßle <t_glaessle@gmx.de>

This work  is free. You can  redistribute it and/or modify  it under the
terms of the Do What The Fuck  You Want To Public License, Version 2, as
published by Sam Hocevar. See the COPYING file for more details.

This program  is free software.  It comes  without any warranty,  to the
extent permitted by applicable law.


### API

- [`doctrim`](#doctrim)
- [`doc2md`](#doc2md)


#### `doctrim`

Clean up indentation from docstrings.


Any whitespace that can be uniformly removed from the second line
onwards is removed.


#### `doc2md`

Convert a docstring to a markdown text.

