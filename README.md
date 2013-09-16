## doc2md

Very lightweight docstring to Markdown converter.

- [License](#license)
- [Description](#description)
- [API](#api)
- [Limitations](#limitations)


### License

Copyright © 2013 Thomas Gläßle <t_glaessle@gmx.de>

This work  is free. You can  redistribute it and/or modify  it under the
terms of the Do What The Fuck  You Want To Public License, Version 2, as
published by Sam Hocevar. See the COPYING file for more details.

This program  is free software.  It comes  without any warranty,  to the
extent permitted by applicable law.


### Description

Little convenience tool to extract docstrings from a module or class and
convert them to GitHub Flavoured Markdown:

https://help.github.com/articles/github-flavored-markdown

Its purpose is to quickly generate `README.md` files for small projects.


### API

The interface consists of the following functions:

 - `doctrim(docstring)`
 - `doc2md(docstring, title)`

You can run this script from the command line like:

```bash
$ doc2md.py [-a] [--no-toc] [-t title] module-name [class-name] > README.md
```


### Limitations

At the moment  this is suited only  for a very specific use  case. It is
hardly forseeable, if I will decide to improve on it in the near future.
