#!/usr/bin/env python3
from .base import Base


class Member(Base):

    def __init__(self, app_key: str, token: str,id=None):
        super(Member, self).__init__(app_key=app_key,token=token)
        self.id = id
        self.request_url = self.base_url + f"/members"

    def get_boards (self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/boards"
        else:
            url_temp = self.request_url + f"/{id}/boards"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Member, self).get_request(url_temp, query, headers = {"Accept": "application/json"})
