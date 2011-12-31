
"""
E-mail validation regex copied from Django 1.3.1

http://code.djangoproject.com/svn/django/branches/releases/1.3.X/django/core/validators.py

    >>> validar_email('luciano@ramalho.org')
    True
    >>> validar_email('a@b.cd')
    True
    >>> validar_email('x')
    False

"""

import re

email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain

def validar_email(email):
    return bool(email_re.match(email))
