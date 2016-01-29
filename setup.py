import hashlib
import os

import webapp2

import models


def make_flag():
    return "CTF{%s}" % hashlib.sha256(os.urandom(24)).hexdigest()


class SetupHandler(webapp2.RequestHandler):
    def get(self):
        # TODO: make idempotent
        flag = models.Flag(
                name = 'Your Flag',
                value = make_flag()
                )
        flag.put()
        self.response.out.write('Flag created.<br>')


app = webapp2.WSGIApplication([
    webapp2.Route('/setup', SetupHandler),
    ])
