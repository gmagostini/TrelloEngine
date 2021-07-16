#!/usr/bin/env python3
from .base import Base


class Label(Base):
    

    def __init__(self, app_key: str, token: str, id=None, use_log = False):
        super(Label, self).__init__(app_key=app_key, token=token,id=id, use_log=use_log)
        self.base_url = self.base_url + "/labels"


    def get_label(self, id: str = None, fileds: str = 'all'):

        url_rquest =  self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fileds': fileds
        }

        super(Label,self).get_request(url=url_rquest, query= query)
    
    def update_label(self, id: str = None, name: str = None, color: str = None):

        url_rquest =  self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'color': color
        }

        super(Label,self).put_request(url=url_rquest, query= query)

    def delete_label(self, id: str = None):

        url_rquest =  self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        super(Label,self).delete_request(url=url_rquest, query= query)

    def update_field(self,field: str, value: str, id: str = None):
    
        url_rquest =  self.select_id(id=id, string=[field])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        super(Label,self).put_request(url=url_rquest, query= query)


    def create_label(self,name: str, color: str, id_board: str, id: str = None):

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'color': color,
            'idBoard': id_board
        }

        super(Label,self).post_request(url=self.base_url, query= query)