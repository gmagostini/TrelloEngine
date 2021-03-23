from .base import Base
import requests
import json

class Token(Base):

    def __init__(self, app_key: str, token: str):
        super(Token, self).__init__(app_key=app_key, token=token)
        self.request_url = self.base_url + f"/tokens/{self.token}"

    def get_member(self):
        url_temp = self.request_url + "/member"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super().get_request(url_temp, query)


