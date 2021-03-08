from .base import Base
import requests
import json

class Tokens(Base):

    def __init__(self, app_key: str, token: str):
        super(Tokens, self).__init__(app_key=app_key,token=token)
        self.url = self.url + f"/tokens/{self.token}"

    def get_member(self):
        url_temp = self.url + "/member"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super().make_request(url_temp,query)


