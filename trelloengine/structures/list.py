#!/usr/bin/env python3
from .base import Base


class List(Base):

    def __init__(self, app_key: str, token: str,id=None, use_log = False):
        super(List, self).__init__(app_key=app_key,token=token, id=id, use_log=use_log)
        self.id = id
        self.base_url = self.base_url + "/lists"


    def get_list(self, id: str = None):

        request_url = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(List, self).get_request(url=request_url, query=query)

    def update_list(self, id: str = None, name: str = None, closed: bool = None, id_board: str = None, 
                   pos: (str, float) = None, subscibed: bool = None):
        
        request_url = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'clodes': closed,
            'idBoard': id_board,
            'pos': pos,
            'subscibed': subscibed
        }

        return super(List, self).put_request(url=request_url, query=query)

    def create_list(self, id_board: str, name: str, id_list_source: str = None, pos: (str, float) = None):

        query = {
            'key': self.app_key,
            'token': self.token,
            'idBoard': id_board,
            'name': name,
            'idListSource': id_list_source,
            'pos': pos
        }

        return super(List, self).post_request(url=self.base_url, query=query)

    def archive_all_cards(self, id: str = None):
        request_url = self.select_id(id=id, string=['archiveAllCards'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(List, self).post_request(url=request_url, query=query)

    def move_all_card(self, id_board: str, id_list: str, id: str = None):

        request_url = self.select_id(id=id, string=['moveAllCards'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'idBoard': id_board,
            'idList': id_list,
        }

        return super(List, self).post_request(url=request_url, query=query)

    def archive_list(self, id: str = None, value: bool = True):

        request_url = self.select_id(id=id, string=['archiveAllCards'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(List, self).put_request(url=request_url, query=query)

    def update_field(self, field: str, id: str = None, value: (str, bool, float) = None):
    
        request_url = self.select_id(id=id, string=['idBoard',field])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(List, self).put_request(url=request_url, query=query)


    def get_actions(self, id: str = None, filter: str = None):
        
        request_url = self.select_id(id=id, string=['actions'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(List, self).get_request(url=request_url, query=query)

    def get_board(self, id: str = None, fields: str = 'all'):
        
        request_url = self.select_id(id=id, string=['board'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields 
        }

        return super(List, self).get_request(url=request_url, query=query)

    def get_cards(self, id: str = None):

        request_url = self.select_id(id=id, string=['cards'])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(List, self).get_request(url=request_url,query=query)