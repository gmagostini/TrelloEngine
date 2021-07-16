#!/usr/bin/env python3
from .base import Base
import requests
import json

class Token(Base):

    def __init__(self, app_key: str, token: str, use_log = False):
        super(Token, self).__init__(app_key=app_key, token=token, use_log=use_log)
        self.base_url = self.base_url + f"/tokens"

    def get_token(self, fields: str = 'all'):
        url_rquest = self.select_id(id=self.token, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super().get_request(url=url_rquest, query=query)
    

    def get_member(self):
        url_rquest = self.select_id(id=self.token, string=['member'])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super().get_request(url=url_rquest, query=query)

    def get_webhooks(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['webhooks'])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super().get_request(url=url_rquest, query=query)

    def create_webhook(self,callback_URL: str, id_model: str, id: str = None, description: str = None):
        url_rquest = self.select_id(id=id, string=['webhooks'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'callbackURL':callback_URL,
            'idModel': id_model,
            'description': description
        }

        return super().post_request(url=url_rquest, query=query)
    
    def get_a_webhook(self,id_webhook: str, id: str = None):
        url_rquest = self.select_id(id=id, string=['webhooks',id_webhook])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super().get_request(url=url_rquest, query=query)


    def update_webhook(self,callback_URL: str = None, id_model: str = None, id: str = None, description: str = None):
        url_rquest = self.select_id(id=id, string=['webhooks'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'callbackURL':callback_URL,
            'idModel': id_model,
            'description': description
        }

        return super().put_request(url=url_rquest, query=query)


    def delete_webhooks(self,id_webhook: str, id: str = None):
        url_rquest = self.select_id(id=id, string=['webhooks',id_webhook])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super().delete_request(url=url_rquest, query=query)

    def delete_tokens(self, id: str = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super().delete_request(url=url_rquest, query=query)
