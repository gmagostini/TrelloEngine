#!/usr/bin/env python3
from .base import Base


class Notification(Base):
    
    def __init__(self, app_key: str, token: str, id=None, use_log = False):
        super(Notification, self).__init__(app_key=app_key, token=token,id=id, use_log=use_log)
        self.base_url = self.base_url + "/notifications"

    
    def get_a_notification(self, id: str = None, board: bool = False, board_fields: str = 'all', card: bool = False, card_field: str = 'all',
                            display: bool = False, entities: bool = False, fields: str = 'all', trello_list: bool = False, member: bool = True, member_field: str = 'all',
                            member_creator: bool = True, member_creator_filed: str = 'all', organization: bool = False, organization_fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'board': board,
            'board_fields' : board_fields,
            'card': card,
            'card_fields': card_field,
            'display': display,
            'entities': entities,
            'fields': fields,
            'list': trello_list,
            'member': member,
            'member_fields': member_field,
            'memberCreator': member_creator,
            'memberCreator_fields': member_creator_filed,
            'organization': organization,
            'organization_fields': organization_fields
        }

        return super(Notification, self).get_request(url=url_rquest, query=query)
    
    def update_notification(self, id: str = None, unread: bool = False):
        url_rquest = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'unread': unread
        }

        return super(Notification, self).put_request(url=url_rquest, query=query)

    
    def get_field(self, field: str, id: str = None):
        url_rquest = self.select_id(id=id, string=[field])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Notification, self).get_request(url=url_rquest, query=query)

    def mark_all_as_read(self, id: str = None, read: bool = False, ids: list = None):
        url_rquest = self.select_id(id=id, string=['all', 'read'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'read': read,
            'ids': ids
        }

        return super(Notification, self).post_request(url=url_rquest, query=query)
    
    def update_status(self, id: str = None, value: str = None):
        url_rquest = self.select_id(id=id, string=['all', 'read'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Notification, self).put_request(url=url_rquest, query=query)
    
    def get_board(self, id: str = None, fields: str = None):
        url_rquest = self.select_id(id=id, string=['board'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Notification, self).get_request(url=url_rquest, query=query)

    def get_card(self, id: str = None, fields: str = None):
        url_rquest = self.select_id(id=id, string=['card'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Notification, self).get_request(url=url_rquest, query=query)

    def get_list(self, id: str = None, fields: str = None):
        url_rquest = self.select_id(id=id, string=['list'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Notification, self).get_request(url=url_rquest, query=query)

    def get_notification_for_this_member(self, id: str = None, fields: str = None):
        url_rquest = self.select_id(id=id, string=['member'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Notification, self).get_request(url=url_rquest, query=query)
    
    def get_notification_create_by_member(self, id: str = None, fields: str = None):
        url_rquest = self.select_id(id=id, string=['memberCreator'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Notification, self).get_request(url=url_rquest, query=query)

    def get_notification_related_with_organization(self, id: str = None, fields: str = None):
        url_rquest = self.select_id(id=id, string=['memberCreator'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Notification, self).get_request(url=url_rquest, query=query)
    

    