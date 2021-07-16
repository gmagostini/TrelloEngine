#!/usr/bin/env python3
from .base import Base


class Webhook(Base):
    
    def __init__(self, app_key: str, token: str, use_log = False):
        super(Webhook, self).__init__(app_key=app_key, token=token, use_log=use_log)
        self.base_url = self.base_url + f"/webhooks"

    def create_webhook(self,callback_URL: str, id_model: str, description: str = None, active: bool = True):

        query = {
            'key': self.app_key,
            'token': self.token,
            'callbackURL':callback_URL,
            'idModel': id_model,
            'description': description,
            'active': active
        }

        return super().post_request(url=self.base_url, query=query)
    
    def get_a_webhook(self, id: str = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super().get_request(url=url_rquest, query=query)


    def update_webhook(self,callback_URL: str = None, id_model: str = None, id: str = None, description: str = None, active: bool = True):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'callbackURL':callback_URL,
            'idModel': id_model,
            'description': description,
            'active': active
        }

        return super().put_request(url=url_rquest, query=query)


    def delete_webhooks(self, id: str = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super().delete_request(url=url_rquest, query=query)

    def get_field(self,field: str, id: str = None):
        url_rquest = self.select_id(id=id, string=[field])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super().get_request(url=url_rquest, query=query)