#!/usr/bin/env python3
import requests
import json

from .logger import init_logger

class Base(object):
    """
    i valori boolean vanno coverti in string, la maiuscola di True e False danno problemi e ritornano valore non valido
    """

    def __init__(self, app_key: str, token: str, id:str = None, use_log = False):
        super(Base, self).__init__()
        self.app_key = app_key
        self.token = token
        self.id = id
        self.base_url = f"https://api.trello.com/1"

        self.response =None
        self.use_log = use_log
        self.logger = init_logger(dunder_name=__name__, level="DEBUG")



    def select_id(self, id: str, string: list = None) -> str:
        """
        Switch for id selection. If no id is passed as a parameter use the global one. If no id exists raise a ValueError.
        Adds the last part of the url.
        :param id: local id
        :param string: last part of the url
        :return: correct url
        """
        if id is None and self.id is None:
            raise ValueError("id is not set correctly")
        elif id == "not_used":
            pass
        elif id is None:
            url_temp = self.base_url + f"/{self.id}"
        else:
            url_temp = self.base_url + f"/{id}"

        if string is not None:
            for i in string:
                url_temp += '/' + i

        return url_temp


    def bool_to_string(self,query: dict()) -> dict:
        """
        Converts boolean values to string so that they can be passed correctly
        :param query: query to be evaluated
        :return: query
        """
        for key in query.keys():
            if isinstance(query[key], bool):
                query[key] = 'true' if query[key] else 'false'

        return query

    def do_logg(self,url, response):
        if self.use_log:
            print(f": {self.use_log}")
            if response.__str__() == "<Response [200]>":
                self.logger.info(f"[RESPONSE]     : {response}")
                self.logger.info(f"[URL REQUEST]  : {url}")
                #self.logger.info(f"[RESPONSE.TEXT]: {response.text}")
                self.logger.info(f"[RESPONSE.TEXT]: {json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(',', ': '))}")
            else:
                self.logger.error(f"[RESPONSE]     : {response}")
                self.logger.error(f"[URL REQUEST]  : {url}")
                self.logger.error(f"[RESPONSE.TEXT]: {response.text}")
                return {"response": response, "text": response.text}


    def get_request(self, url, query, headers = {"Accept": "application/json"}) -> json:
        """
        basic function for the get request
        :param url:
        :param query:
        :param headers:
        :return:
        """
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=self.bool_to_string(query)
        )

        self.do_logg(url, response)

        if response.__str__() == "<Response [200]>":
            return response.json()

       

    def put_request(self, url, query) -> json:
        """
        basic function for the put request
        :param url:
        :param query:
        :return:
        """
        response = requests.request(
            "PUT",
            url,
            params=self.bool_to_string(query)
        )

        self.do_logg(url, response)

        if response.__str__() == "<Response [200]>":
            return response.json()


    def post_request(self, url, query) -> json:
        """
        basic function for the post request
        :param url:
        :param query:
        :return:
        """

        response = requests.request(
            "POST",
            url,
            params=self.bool_to_string(query)
        )

        self.do_logg(url, response)

        if response.__str__() == "<Response [200]>":
            return response.json()


    def delete_request(self, url, query) -> json:
        """
        basic function for the delete request
        :param url:
        :param query:
        :return:
        """
        response = requests.request(
            "DELETE",
            url,
            params=self.bool_to_string(query)
        )

        self.do_logg(url, response)

        if response.__str__() == "<Response [200]>":
            return response.json()



