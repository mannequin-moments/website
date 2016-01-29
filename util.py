import functools
import logging
import urllib2
import urlparse

import webapp2


def require_login(f):
    @functools.wraps(f)
    def wrapped(self, *args, **kwargs):
        if not self.session.get('user'):
            return webapp2.redirect('/login', response=self.response)
        return f(self, *args, **kwargs)
    return wrapped


