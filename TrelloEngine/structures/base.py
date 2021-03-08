import requests
import json


class Base(object):

    def __init__(self, app_key: str, token: str):
        super(Base, self).__init__()
        self.app_key = app_key
        self.token = token
        self.url = f"https://api.trello.com/1"



    def make_request(self, url, query, param = "GET",  headers = {"Accept": "application/json"}):

        response = requests.request(
            param,
            url,
            headers=headers,
            params=query
        )
        print(url)
        if response.__str__() == "<Response [200]>":
            print(response)
            print(response.encoding)
            print(response.headers['Content-Type'])
            return response.json()
        else:
            return {"[ERROR]":response.__str__()}

