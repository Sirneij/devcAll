# Devc

**NOTE**: Exposing some secret details in the `settings.py` file was delibrate!

[sirneijblog.herokuapp.com](https://sirneijblog.herokuapp.com) is a complex web application inspired by `Frances Nnamadim`, a senior and regular colleague who worked as a Business Analyst and UI/UX designer in `ipNX Nigeria Ltd's` department of Business Intel­ligence and Data Analytics (BIDA). It is `blogging` and `portfolio` application fully implemented in `Django` frame­work with `PostgreSQL` database at the back­end and some bits of `Ajax` for better user experiences. Utilizing the free `HTML` template oferred by [Styleshout](https://www.styleshout.com/), [sirneijblog.herokuapp.com](https://sirneijblog.herokuapp.com) was built with three (3) other main applications embedded, each embedding other systems in turn:

- **Account management system**: This application provides interfaces for users
  authentication and authorization. It allows direct authentication from popular social
  and technical websites such as `Facebook`, `Twitter` and `Github` among others as shown
  in below:
  ![Sirneijblog Login and Signup](https://github.com/sirneij/devcAll/blob/master/devcsignup.png?raw=true)

- **Blogging system**: This is the heart of the overall system. It controls `user’s posts` - their `creation` and `update`, with a `rich text editor` and advanced text formatting sys­
  tem; and posts’ `deletion` - ­profiles and portfolio with various mini­-systems such as
  `full­text search engine`, `tagging`, `related­ posts recommendation`, `asynchronous threaded comment­ing` and `slack­-like chatting(yet to be rolled out)` systems, embedded. Users’ posts could also be `liked` and
  shared asynchronously`.

- **Portfolio system**: This serves as an extension of the account management sys­
  tem where authors of post(s) showcase their skills to their potential recruiters. It
  structures authors profiles, education, skills, projects and recommendations accord­
  ingly which can be downloaded in Portable Document Format (PDF)

# Local testing

To run this piece of software locally, two files need to be taken care of - `wsgi.py` and `manage.py`.

Currently, `wsgi.py` ans `manage.py` files have the contents below:

## `wsgi.py`

```
  """
WSGI config for devc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.conf import settings

from django.core.wsgi import get_wsgi_application
if settings.DEBUG:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devc.settings.dev')
else:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'devc.settings.production')

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devc.settings')

application = get_wsgi_application()

```

and,

## `manage.py`

```
  #!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
  # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devc.settings')
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devc.settings.dev')
  try:
      from django.core.management import execute_from_command_line
  except ImportError as exc:
      raise ImportError(
          "Couldn't import Django. Are you sure it's installed and "
          "available on your PYTHONPATH environment variable? Did you "
          "forget to activate a virtual environment?"
      ) from exc
  execute_from_command_line(sys.argv)


if __name__ == '__main__':
  main()

```

Ensure that both files use `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devc.settings.dev')` as their entry settings file.
