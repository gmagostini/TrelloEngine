#!/usr/bin/env python3
from .base import Base


class CustumField(Base):

    def __init__(self, app_key: str, token: str, id=None, use_log = False):
        super(CustumField, self).__init__(app_key=app_key, token=token,id=id, use_log=use_log)
        self.base_url = self.base_url + "/customFields"


    def create_custom_field(self,id_model: str, model_type: str, name: str, type: str, pos: (str, float),
                            options: str = None, display_card_front: bool = True ):
        """
        Create a new Custom Field on a board.
        :param id_model: i don't know what it is
        :param model_type: The type of model that the Custom Field is being defined on. This should always be board.
        :param name: The name of the Custom Field
        :param type: The type of Custom Field to create.
        :param pos: Normally pos is the position, but I do not understand what it refers to in this case.
        :param options: If the type is checkbox
        :param display_card_front: Whether this Custom Field should be shown on the front of Cards
        """
        query = {
            'key': self.app_key,
            'token': self.token,
            'idModel': id_model,
            'modelType': model_type,
            'name': name,
            'type': type,
            'options': options,
            'pos': pos,
            'display_cardFront': display_card_front
        }

        return super(CustumField, self).get_request(url=self.base_url, query=query)

    def get_custom_fields(self, id: str = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(CustumField, self).get_request(url=url_rquest, query=query)

    def update_custom_fields(self, id: str = None, name: str = None, pos: (str, float) = None, display: bool = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(CustumField, self).get_request(url=url_rquest, query=query)

    def delete_custom_fields(self, id: str = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(CustumField, self).delete_request(url=url_rquest, query=query)

    def get_options(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['options'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(CustumField, self).get_request(url=url_rquest, query=query)

    def add_option(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['options'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(CustumField, self).post_request(url=url_rquest, query=query)

    def get_option(self, id_custom_field_option: str, id: str = None):
        url_rquest = self.select_id(id=id, string=['options', id_custom_field_option])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(CustumField, self).get_request(url=url_rquest, query=query)

    def delete_option(self, id_custom_field_option: str, id: str = None):
        url_rquest = self.select_id(id=id, string=['options', id_custom_field_option])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(CustumField, self).get_request(url=url_rquest, query=query)