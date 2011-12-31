
"""
E-mail validation regex from Django 1.3.1:

http://code.djangoproject.com/svn/django/branches/releases/1.3.X/django/core/validators.py

    >>> is_valid('luciano@ramalho.org')
    True
    >>> is_valid('a@b.cd')
    True
    >>> is_valid('x')
    False

"""

import re

email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain

def is_valid(email):
    return bool(email_re.match(email))
