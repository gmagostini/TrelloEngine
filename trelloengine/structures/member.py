#!/usr/bin/env python3
from .base import Base


class Member(Base):

    def __init__(self, app_key: str, token: str,id=None, use_log = False):
        super(Member, self).__init__(app_key=app_key,token=token, id=id, use_log=use_log)
        self.id = id
        self.base_url = self.base_url + f"/members"


    def get_list(self, id: str = None):

        request_url = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Member, self).get_request(url=request_url, query=query)
    def get_member(self, id: str = None, actions: str = None, boards: str = None, boardBackgrounds: str = None,
                    boardsInvited: str = 'all', boardsInvited_fields: str = 'all', boardStars: bool = False,
                    cards: str = None, customBoardBackgrounds: str = None, customEmoji: str = None, customStickers: str = None,
                    fields: str = None, notifications: str = None, organizations: str = None, organization_fields: str = None, 
                    organization_paid_account: bool = False, organizations_invited: str = None, organizationsInvited_fields: str = None,
                    paid_account: bool = False, savedSearches: bool = False, tokens: str = None):

        request_url = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'actions': actions,
            'boards': boards,
            'boardBackgrounds': boardBackgrounds,
            'boardsInvited': boardsInvited,
            'boardsInvited_fields': boardsInvited_fields,
            'boardStars': boardStars,
            'cards': cards,
            'customBoardBackgrounds':  customBoardBackgrounds,
            'customEmoji': customEmoji,
            'customStickers': customStickers,
            'fields': fields,
            'notifications': notifications,
            'organizations': organizations,
            'organization_fields': organization_fields,
            'organization_paid_account': organization_paid_account,
            'organizationsInvited': organizations_invited,
            'organizationsInvited_fields': organizationsInvited_fields,
            'paid_account': paid_account,
            'savedSearches': savedSearches,
            'tokens': tokens,
        }

        return super(Member, self).get_request(url=request_url, query=query)
    
    def update_member(self, id: str = None, full_name: str = None, initials: str = None, username: str = None, bio: str = None,
                     avatar_source: str = None, color_blind: bool = None, locale: str = None, minutes_between_summaries: int = None):
    
        request_url = self.select_id(id=id, string=[])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fullName': full_name,
            'initials': initials,
            'username': username,
            'bio': bio,
            'avatarSource': avatar_source, 
            'prefs/colorBlind': color_blind,
            'prefs/locale': locale,
            'prefs/minutesBetweenSummaries': minutes_between_summaries
        }

        return super(Member, self).put_request(url=request_url, query=query)
        

    def get_filed(self, field: str, id: str = None):
    
        request_url = self.select_id(id=id, string=[field])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Member, self).get_request(url=request_url, query=query)

    def get_actions(self, id: str = None, filter: str = None):
        
        request_url = self.select_id(id=id, string=['actions'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(Member, self).get_request(url=request_url, query=query)

    def get_custom_board_backgounds (self, id: str = None, filter: str = 'all'):
        request_url = self.select_id(id=id, string=['boardBackgrounds'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(Member, self).get_request(url=request_url, query=query)

    def upload_board_background(self, file: str, id: str = None):
        request_url = self.select_id(id=id, string=['boardBackgrounds'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'file': file
        }

        return super(Member, self).post_request(url=request_url, query=query)
    

    def get_board_background(self, id_background: str, id: str = None, fields: str = None):
        request_url = self.select_id(id=id, string=['boardBackgrounds',id_background])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        super(Member, self).get_request(url=request_url, query=query)

    def update_custom_board_background(self, id_background: str, id: str = None, brightness: str = None, tile: bool  = None):
        request_url = self.select_id(id=id, string=['boardBackgrounds',id_background])

        query = {
            'key': self.app_key,
            'token': self.token,
            'brightness': brightness,
            'tile': tile
        }

        return super(Member, self).put_request(url=request_url, query=query)

    def delete_custom_board_background(self, id_background: str, id: str = None, brightness: str = None, tile: bool  = None):
        request_url = self.select_id(id=id, string=['boardBackgrounds',id_background])

        query = {
            'key': self.app_key,
            'token': self.token,
            'brightness': brightness,
            'tile': tile
        }

        return super(Member, self).put_request(url=request_url, query=query)

    def get_costum_emojis(self, id: str = None):
        request_url = self.select_id(id=id, string=['customEmoji'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Member, self).get_request(url=request_url, query=query)

    def create_costum_emojis(self,file: str, name: str, id: str = None):
        request_url = self.select_id(id=id, string=['customEmoji'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'file': file,
            'name': name
        }

        return super(Member, self).post_request(url=request_url, query=query)

    def get_a_costum_emoji(self,id_emoji: str, id: str = None, field: str = 'all'):
        request_url = self.select_id(id=id, string=['customEmoji',id_emoji])

        query = {
            'key': self.app_key,
            'token': self.token,
            'field': field,
        }

        return super(Member, self).get_request(url=request_url, query=query)

    def get_costum_stickers(self, id: str = None):
        request_url = self.select_id(id=id, string=['customStickers'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Member, self).get_request(url=request_url, query=query)

    def create_costum_stiker(self, file: str, id: str = None):
        request_url = self.select_id(id=id, string=['customStickers'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Member, self).post_request(url=request_url, query=query)

    def get_a_costum_stickers(self,id_sticker: str, id: str = None, fields: str = 'all'):
        request_url = self.select_id(id=id, string=['customStickers',id_sticker])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Member, self).get_request(url=request_url, query=query)

    def delete_a_costum_stickers(self,id_sticker: str, id: str = None, fields: str = 'all'):
        request_url = self.select_id(id=id, string=['customStickers',id_sticker])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Member, self).delete_request(url=request_url, query=query)

    def get_notifications(self, id:str = None, entities: bool = False, display: bool = False, filte: str = 'all', 
                            read_filter: str = 'all', fields: str = 'all', limit: int = 50, page: int = 0,
                            before: str = None, since: str = None, member_creator: bool = True, member_creator_filed = 'all'):
        request_url = self.select_id(id=id, string=['notifications'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'entities ':entities,
            'display': display,
            'filter' : filter,
            'read_filter': read_filter,
            'fields': fields,
            'limit': limit,
            'page': page,
            'before': before,
            'since': since,
            'memberCreator': member_creator, 
            'memberCreator_fields': member_creator_filed
        }

        return super(Member,self).get_request(url=request_url, query=query)

    def get_organization(self, id: str = None, filter: str = 'all', fields: str = 'all', paid_accaunt: bool = False):
        request_url = self.select_id(id=id, string=['organizations'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter,
            'fields': fields,
            'paid_accaunt': paid_accaunt
        }

        return super(Member,self).get_request(url=request_url, query=query)

    def get_saved_searched(self, id: str = None):
        request_url = self.select_id(id=id, string=['savedSearches'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Member,self).get_request(url=request_url, query=query)

    def create_saved_searched(self,name: str, query: str, pos: (int, str), id: str = None):
        request_url = self.select_id(id=id, string=['savedSearches'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'query': query,
            'pos': pos
        }

        return super(Member,self).post_request(url=request_url, query=query)

    def get_a_saved_searched(self,idSearch: str, id: str = None):
        request_url = self.select_id(id=id, string=['savedSearches',idSearch])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Member,self).get_request(url=request_url, query=query)

    def update_a_saved_searched(self,idSearch: str, name: str = None, query: str = None, pos: (int, str) = None, id: str = None):
        request_url = self.select_id(id=id, string=['savedSearches',idSearch])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'query': query,
            'pos': pos
        }

        return super(Member,self).put_request(url=request_url, query=query)

    def delete_a_saved_searched(self,idSearch: str, id: str = None):
        request_url = self.select_id(id=id, string=['savedSearches',idSearch])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Member,self).delete_request(url=request_url, query=query)

    def get_token(self, webhooks: bool = False):
        request_url = self.select_id(id=id, string=['tokens'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'webhooks': webhooks
        }

        return super(Member,self).get_request(url=request_url, query=query)

    def create_avatar(self, file: str, id: str = None):
        request_url = self.select_id(id=id, string=['tokens'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'file': file
        }

        return super(Member,self).get_request(url=request_url, query=query)

    def dismiss_message(self, value: str, id: str = None):
        request_url = self.select_id(id=id, string=['oneTimeMessagesDismissed'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }
        
        return super(Member,self).post_request(url=request_url, query=query)

    def get_boards (self, id=None, filter: str = 'all', fields: str = 'all', lists: str = None, organization: bool = False, organization_fields: str = 'all'):

        request_url = self.select_id(id=id, string=['boards'])


        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter,
            'fields': fields,
            'lists': lists,
            'organization': organization,
            'organization_fields': organization_fields
        }

        return super(Member, self).get_request(url=request_url, query=query)

