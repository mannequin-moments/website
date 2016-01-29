import logging

from google.appengine.api import datastore_errors
from google.appengine.ext import ndb


class LoginError(Exception):
    
    def __init__(self, query, ex):
        super(LoginError, self).__init__()
        self.query = query
        self.ex = ex

    def __str__(self):
        # TODO display query on query errors
        logging.error(str(self.ex))
        if isinstance(self.ex, datastore_errors.BadQueryError):
            return 'Login error: %s, query: %s' % (str(self.ex), self.query)
        return 'Login error.'


class User(ndb.Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    gpg_key = ndb.TextProperty()

    @classmethod
    def Login(cls, username, password):
        query = "SELECT * FROM User WHERE username = '%s'" % username
        if password is not None:
            query += " AND password = '%s'" % password
        logging.info('Login query: [%s]', query)
        try:
            qry = ndb.gql(query)
            return qry.get()
        except Exception as ex:
            raise LoginError(query, ex)

    @classmethod
    def Get(cls, username):
        return cls.query(cls.username == username).get()


class Flag(ndb.Model):
    name = ndb.StringProperty()
    value = ndb.StringProperty()
