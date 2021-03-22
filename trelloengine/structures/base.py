import requests
import json


class Base(object):
    """
    i valori boolean vanno coverti in string, la maiuscola di True e False danno problemi e ritornano valore non valido
    """

    def __init__(self, app_key: str, token: str, id:str = None):
        super(Base, self).__init__()
        self.app_key = app_key
        self.token = token
        self.id = id
        self.id = None
        self.request_url = f"https://api.trello.com/1"




    def get_request(self, url, query, headers = {"Accept": "application/json"}):

        response = requests.request(
            "GET",
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
            return {"response": response, "text": response.text}

    def put_request(self, url, query):

        response = requests.request(
            "PUT",
            url,
            params=query
        )
        print(url)
        if response.__str__() == "<Response [200]>":
            print(response)
            print(response.encoding)
            print(response.headers['Content-Type'])
            return response.json()
        else:
            return {"response": response, "text": response.text}


    def post_request(self, url, query):

        response = requests.request(
            "POST",
            url,
            params=query
        )
        print(url)
        if response.__str__() == "<Response [200]>":
            print(response)
            print(response.encoding)
            print(response.headers['Content-Type'])
            return response.json()
        else:
            return {"response": response, "text": response.text}


    def delete_request(self, url, query):

        response = requests.request(
            "DELETE",
            url,
            params=query
        )
        print(url)
        if response.__str__() == "<Response [200]>":
            print(response)
            print(response.encoding)
            print(response.headers['Content-Type'])
            return response.json()
        else:
            return {"response": response, "text": response.text}