import json
import logging

import jinja2
import webapp2

from webapp2_extras import sessions

import models
import util

class RequestHandler(webapp2.RequestHandler):
    """Base request handler for Mannequin Moments."""
    jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('templates')
            )

    def dispatch(self):
        self._session_store = sessions.get_store(request=self.request)

        try:
            super(RequestHandler, self).dispatch()
        finally:
            self._session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        return self._session_store.get_session()

    def render(self, tpl_name, **args):
        tmpl = self.jinja_env.get_template(tpl_name)
        args['logged_in'] = True if self.session.get('user') else False
        self.response.out.write(tmpl.render(**args))


class HomeHandler(RequestHandler):
    def get(self):
        self.render('index.tpl')


class LoginHandler(RequestHandler):
    def get(self):
        self.render('login.tpl')

    def post(self):
        user = None
        username = self.request.get('username') or None
        password = self.request.get('password') or None
	# Change #1281 - emergency maintenance due to security issues
	# user = redo auth.
	return self.render('login.tpl', error='Undergoing emergency maintenance, sorry for any inconvenience caused')
        self.session['user'] = username
        return webapp2.redirect('/', response=self.response)


class FlagHandler(RequestHandler):
    @util.require_login
    def get(self):
        flags = models.Flag.query().fetch()
        self.render('flags.tpl', flags=flags)


config = {
        'webapp2_extras.sessions': {
            'secret_key': 'a793134b-c2c5-4cbf-973b-64ff7eea863a',
            'name': 'mannequin-moments',
        }
}

app = webapp2.WSGIApplication([
    webapp2.Route('/', HomeHandler),
    webapp2.Route('/login', LoginHandler),
    webapp2.Route('/flags', FlagHandler),
], config=config)
