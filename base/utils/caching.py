from django.core.cache import cache
from base.utils.constants import Constant
from random import randint


class CachingProcedureHandler:
    """ Deal with settings and getting data from cache """
    def __init__(self):
        self.token_from = Constant.RANDOM_TOKEN_FROM
        self.token_to = Constant.RANDOM_TOKEN_TO
        self.expiration = Constant.REDIS_EXPIRATION

    def set_key(self, type, email, token):
        """ store a single key in cache """
        return cache.set(f"{type}:{token}", email, self.expiration)
    
    def get_key(self, type, token):
        """ get a value from cache """
        return cache.get(f"{type}:{token}")
    
    def generate_token(self):
        """ generate a random token """
        token = randint(self.token_from, self.token_to)
        return str(token)
