#!/usr/bin/env python3
from .base import Base


class Checklist(Base):

    def __init__(self, app_key: str, token: str, id=None):
        super(Checklist, self).__init__(app_key=app_key, token=token, id=id)
        self.base_url = self.base_url + "/checklists"



    def create_checklist(self, id_card: str, id_checklist: str, id: str = None, name:str = None, pos: (str, float) = "top",
                         id_checklist_source: str = None ):

        query = {
            'key': self.app_key,
            'token': self.token,
            'diCard': id_card,
            'name': name,
            'pos': pos,
            'idChecklistSource': id_checklist_source
        }

        return super(Checklist, self).post_request(url=self.base_url, query=query)

    def get_checklist(self,id: str = None, cards: str = 'none', check_items: str = 'all', check_item_filed: str = 'all',
                      fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'cards': cards,
            'checkItems': check_items,
            'checkItem_fields': check_item_filed,
            'fields': fields
        }

        return super(Checklist, self).get_request(url=url_rquest, query=query)


    def update_checklist(self,id: str = None, name: str = None, pos: (str, float) = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'pos': pos
        }

        return super(Checklist, self).put_request(url=url_rquest, query=query)

    def delete_checklist(self,id: str = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Checklist, self).delete_request(url=url_rquest, query=query)

    def get_field(self,fild: str, id: str = None):
        url_rquest = self.select_id(id=id, string=[fild])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Checklist, self).get_request(url=url_rquest, query=query)

    def update_field(self, fild: str, value: (str, float), id: str = None):
        url_rquest = self.select_id(id=id, string=[fild])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Checklist, self).put_request(url=url_rquest, query=query)

    def get_board(self,id: str = None, fields:str = 'all'):
        url_rquest = self.select_id(id=id, string=['board'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Checklist, self).get_request(url=url_rquest, query=query)

    def get_card(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['cards'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Checklist, self).get_request(url=url_rquest, query=query)

    def get_checkitems(self, id: str = None, filter:str = 'all', fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=['checkItems'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter,
            'fields': fields
        }

        return super(Checklist, self).get_request(url=url_rquest, query=query)

    def create_checkitem(self, name: str, id: str = None, pos: (str, float) = 'bottom', checked: bool = False):
        url_rquest = self.select_id(id=id, string=['checkItems'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'pos': pos,
            'checked': checked
        }

        return super(Checklist, self).post_request(url=url_rquest, query=query)

    def get_checkitem(self,id_check_item: str, id: str = None, fileds: str = 'all'):
        url_rquest = self.select_id(id=id, string=['checkItems', id_check_item])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fileds': fileds
        }

        return super(Checklist, self).get_request(url=url_rquest, query=query)

    def delete_checkitem(self, id_check_item: str, id: str = None):
        url_rquest = self.select_id(id=id, string=['checkItems',id_check_item])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Checklist, self).delete_request(url=url_rquest, query=query)
