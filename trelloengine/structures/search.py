#!/usr/bin/env python3
from .base import Base


class Search(Base):
    
    def __init__(self, app_key: str, token: str, id=None , use_log = False):
        super(Search, self).__init__(app_key=app_key, token=token, id=None, use_log=use_log)
        self.base_url = self.base_url + "/search"
    
    def serach_trello(self,id_board: str = None, id_organization: str = None, id_card: str = None, model_types: str = 'all', 
                        board_fields: str = 'name,idOrganization', board_limist: int = 10, card_fields: str = 'all', 
                        cards_limit: int = 10,cards_page: int = 0, card_members: bool = False, card_attachments: bool = False, 
                        organization_fields: str = 'name,displayName', organizations_limit: int = 10, 
                        member_fields: str = 'avatarHash,fullName,initials,username,confirmed', members_limit: int = 10, partial: bool = False):

        query = {
            'key': self.app_key,
            'token': self.token,
            'idBoards': id_board,
            'idOrganizations': id_organization,
            'idCards': id_card,
            'modelTypes': model_types,
            'board_fields': board_fields,
            'boards_limit': board_limist,
            'card_fields': card_fields,
            'cards_limit': cards_limit,
            'cards_page': cards_page,
            'card_board': card_members,
            'card_list': card_attachments,
            'card_members': organization_fields,
            'card_stickers': organizations_limit,
            'card_attachments': card_attachments,
            'organization_fields': organization_fields,
            'organizations_limit': organizations_limit,
            'member_fields': member_fields,
            'members_limit': members_limit,
            'partial': partial
        }

        return super(Search, self).get_request(url=self.base_url, query=query)

    def search_member(self, limit: int = 8, id_board: str = None, id_organization: str = None, only_or_members: bool = False):
        url_rquest = self.select_id(id="not_used", string=['members'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'limit': limit, 
            'idBoard': id_board, 
            'idOrganization': id_organization, 
            'onlyOrgMembers': only_or_members
        }

        return super(Search, self).get_request(url=url_rquest, query=query)

    
    
