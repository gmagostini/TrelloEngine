#!/usr/bin/env python3
from .base import Base


class Organization(Base):
    
    def __init__(self, app_key: str, token: str, id=None):
        super(Organization, self).__init__(app_key=app_key, token=token, id=id)
        self.base_url = self.base_url + "/organizations"
    
    def create_organization(self,display_name: str, id: str = None, desc: str =  None, name: str = None, website: str = None):

        
        query = {
            'key': self.app_key,
            'token': self.token,
            'displayName': display_name,
            'desc': desc,
            'name': name,
            'website': website
        }
        
        return super(Organization, self).post_request(url=self.base_url, query=query)

    def get_organization(self, id: str = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)

    def delete_organization(self, id: str = None):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).delete_request(url=url_rquest, query=query)
    
    def get_field(self, field: str, id: str = None):
        url_rquest = self.select_id(id=id, string=[field])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)

    def get_actions(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['actions'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)

    def get_board(self, filter: str = 'all', fileds: str = 'all'):
        url_rquest = self.select_id(id=id, string=['actions'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter,
            'fileds': fileds
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)

    def retrive_exposts(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['exports'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)

    def create_expost(self, id: str = None, attachemts: bool = True):
        url_rquest = self.select_id(id=id, string=['exports'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).post_request(url=url_rquest, query=query)

    def get_members(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['members'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)

    def update_members(self,email: str, full_name: str,  id: str = None, type: str = 'normal'):
        url_rquest = self.select_id(id=id, string=['members'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'type': type
        }

        return super(Organization, self).put_request(url=url_rquest, query=query)

    def get_memberships(self, id: str = None, filter: str = 'all', member: bool = False):
        url_rquest = self.select_id(id=id, string=['memberships'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter,
            'member': member
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)


    def get_a_membership(self,idMembership: str, id: str = None, member: bool = False):
        url_rquest = self.select_id(id=id, string=['memberships', idMembership])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter,
            'member': member
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)
    
    def get_plugin_data(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['pluginData'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)
    
    def get_tags(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['tags'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).get_request(url=url_rquest, query=query)

    def create_tags(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['tags'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).post_request(url=url_rquest, query=query)
    
    def update_a_member(self,idMember: str, type: str,  id: str = None):
        url_rquest = self.select_id(id=id, string=['members', idMember])

        query = {
            'key': self.app_key,
            'token': self.token,
            'type': type
        }

        return super(Organization, self).put_request(url=url_rquest, query=query)

    def remove_a_member(self,idMember: str, id: str = None):
        url_rquest = self.select_id(id=id, string=['members', idMember])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).delete_request(url=url_rquest, query=query)
    
    def deative_or_reactive(self,id_member:str, value: bool, id: str = None):
        url_rquest = self.select_id(id=id, string=['members', id_member])
        """Da implemetare come un interrutore on/off"""
        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Organization, self).delete_request(url=url_rquest, query=query)

    def update_logo(self, value: bool, id: str = None):
        url_rquest = self.select_id(id=id, string=['logo'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).delete_request(url=url_rquest, query=query)
    
    def delete_logo(self, value: bool, id: str = None):
        url_rquest = self.select_id(id=id, string=['logo'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).delete_request(url=url_rquest, query=query)

    
    def remove_member_from_organization_and_board(self, id_member: str , id: str = None):
        url_rquest = self.select_id(id=id, string=['members', id_member, 'all'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Organization, self).delete_request(url=url_rquest, query=query)

    def remove_asosciete_google_apps_domain_fro_a_workspace(self, id: str = None):
        url_rquest = self.select_id(id=id, string=['prefs', 'associatedDomain'])

        