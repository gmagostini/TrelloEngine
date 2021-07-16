#!/usr/bin/env python3
from .base import Base


class Enterprise(Base):

    def __init__(self, app_key: str, token: str, id=None, use_log = False):
        super(Enterprise, self).__init__(app_key=app_key, token=token,id=id, use_log=use_log)
        self.base_url = self.base_url + "/enterprises"

    def get_enterprise(self, id: str = None, fields: str = 'all', members: str = None,
                       member_fields: str = 'none, normal, admins, owners, all', member_filter: str = None,
                       member_sort: str = None, member_sort_by: str = None, member_sort_order: str = 'id',
                       member_start_index: int = 1, member_count: int = 10, organizations: str = None, organization_fields: str = None,
                       organization_paid_accounts: bool = False, organization_memberships: str = None):

        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields,
            'members': members,
            'member_fields': member_fields,
            'member_filter': member_filter,
            'member_sort': member_sort,
            'member_sortBy': member_sort_by,
            'member_sortOrder': member_sort_order,
            'member_startIndex': member_start_index,
            'member_count': member_count,
            'organizations': organizations,
            'organization_fields': organization_fields,
            'organization_paid_accounts': organization_paid_accounts,
            'organization_memberships': organization_memberships
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

    def get_member(self,id_member: str, id: str = None, fileds: str = 'all', organization_fields: str = 'all', board_fields: str = 'name'):

        url_rquest = self.select_id(id=id, string=['members', id_member])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fileds,
            'organization_fields': organization_fields,
            'board_fields': board_fields
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def get_whether_an_organization_can_be_transferred_to_an_enterprise(self, id_organization: str,  id: str = None):

        url_rquest = self.select_id(id=id, string=['transferrable', 'organization', id_organization])

        query = {
            'key': self.app_key,
            'token': self.token,
            'idOrganization': id_organization,
        }

        return super(Enterprise, self).get_request(url=url_rquest, query=query)

    def create_auth_token(self, id: str = None, expiration: str = None):

        url_rquest = self.select_id(id=id, string=['tokens'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'expiration': expiration
        }

        return super(Enterprise, self).post_request(url=url_rquest, query=query)

    def transfer_organization_to_an_enterprise(self, id_organization: str, id: str = None):

        url_rquest = self.select_id(id=id, string=['organizations'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'idOrganization': id_organization
        }

        return super(Enterprise, self).put_request(url=url_rquest, query=query)

    def update_a_member_licensed_status(self, id_member: str, value: bool, id: str = None):

        url_rquest = self.select_id(id=id, string=['members', id_member, 'licensed'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'Values': value
        }

        return super(Enterprise, self).put_request(url=url_rquest, query=query)

    def deactive_member(self, id_member: str, value: bool, id: str = None, fields: str = 'all', organization_fields: str = 'all',
                       board_fields: str = 'all'):

        url_rquest = self.select_id(id=id, string=['members',id_member,'deactivated'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value,
            'fields': fields,
            'organization_fields': organization_fields,
            'board_fields': board_fields
        }

        return super(Enterprise, self).put_request(url=url_rquest, query=query)

    def update_member_to_admin(self, id_member: str, id: str = None):

        url_rquest = self.select_id(id=id, string=['admins', id_member])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).post_request(url=url_rquest, query=query)

    def delete_organization(self,id_org: str, id: str = None):

        url_rquest = self.select_id(id=id, string=['organizations', id_org])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).delete_request(url=url_rquest, query=query)

    def remove_member(self, id_member: str, id: str = None):

        url_rquest = self.select_id(id=id, string=['organizations',id_member])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Enterprise, self).delete_request(url=url_rquest, query=query)