#!/usr/bin/env python3
from .base import Base


class Enterprise(Base):

    def __init__(self, app_key: str, token: str, id=None):
        super(Enterprise, self).__init__(app_key=app_key, token=token, id=id)
        self.base_url = self.base_url + "/enterprises"

    def get_enterprise(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def get_auditlog(self, id: str = None):

        url_rquest = self.select_id(id=id, string=['auditlog'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def get_enterprise_admin(self, id: str = None, fileds: str = 'all'):

        url_rquest = self.select_id(id=id, string=['admins'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fileds,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def get_signup_url(self, id: str = None, authenticate: bool = False, confirmation_accepted: bool = False,
                       return_url: str = None, tos_acceptes: bool = False):

        url_rquest = self.select_id(id=id, string=['signupUrl'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'authenticate': authenticate,
            'confirmationAccepted': confirmation_accepted,
            'returnUrl': return_url,
            'tosAccepted': tos_acceptes
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def get_members(self, id: str = None, fiels: str = 'all', filter: str = None, sort: str = None, sort_by: str = None,
                    sort_order: str = None, start_index: int = None, count: str = 'none', ):

        url_rquest = self.select_id(id=id, string=['members'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def get_member(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def get_whether_an_organization_can_be_transferred_to_an_enterprise(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def get_enterprise(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def transfer_organization_to_an_enterprise(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def update_a_member_licensed_status(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def deactive_member(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def update_member_to_admin(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def delete_organization(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def remove_member(self, id: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)