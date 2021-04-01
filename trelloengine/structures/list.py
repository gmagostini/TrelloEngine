#!/usr/bin/env python3
from .base import Base


class List(Base):

    def __init__(self, app_key: str, token: str,id=None):
        super(List, self).__init__(app_key=app_key,token=token)
        self.id = id
        self.request_url = self.base_url + "/lists"

    def get_cards(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/cards"
        else:
            url_temp = self.request_url + f"/{id}/cards"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(List, self).get_request(url_temp, query, headers = {"Accept": "application/json"})