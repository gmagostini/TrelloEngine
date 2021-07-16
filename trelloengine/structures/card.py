#!/usr/bin/env python3
from .base import Base


class Card(Base):

    def __init__(self, app_key: str, token: str, id=None, use_log = False):
        super(Card, self).__init__(app_key=app_key, token=token, id=id, use_log = use_log)
        self.base_url = self.base_url + "/cards"

    def create_card(self, id_list: str, name: str =None, desc: str = None, pos:str= None, due: str = None, deu_complete: bool =False,
                    id_members: list = None, id_labels: list = None, url_source: str = None, file_source: str = None,
                    id_card_source: str = None, keep_from_source: str = None, address: str = None, location_name: str = None,
                    coordinate: str = None):


        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'desc': desc,
            'pos': pos,
            'due': due,
            'dueComplete': deu_complete,
            'idList': id_list,
            'idMembers': id_members,
            'idLabels': id_labels,
            'urlSource': url_source,
            'fileSource': file_source,
            'idCardSource': id_card_source,
            'keepFromSource': keep_from_source,
            'andress': address,
            'locationName': location_name,
            'coordinates': coordinate
        }

        return super(Card, self).post_request(url=self.base_url,query=self.bool_to_string(query=query))

    def get_card(self, id: str = None, fields: str = 'all', actions: str = None, attachments: (str, bool) = False, attachment_fields: str = "all",
                 members: bool = False, member_filed:str = 'all', member_votet: bool = False, member_voted_field: str = 'all',
                 check_item_states: bool = False, checklists: str = None, checklist_filed: str = 'all', board: bool = False, board_filed: str = 'all',
                 get_list: bool = False, plugin_data: bool = None, stickers: bool = False, sticker_field: str = 'all', custom_field_items: bool = False):

        url_rquest = self.select_id(id=id)

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields,
            'actions': actions,
            'attachments': attachments,
            'attachment_fields': attachment_fields,
            'members': members,
            'meber_field': member_filed,
            'membersVoted': member_votet,
            'memberVoted_fields': member_voted_field,
            'checkItemsStates': check_item_states,
            'checklists': checklists,
            'checklist_fields': checklist_filed,
            'board': board,
            'board_field': board_filed,
            'list': get_list,
            'pluginData': plugin_data,
            'stickers': stickers,
            'sticker_fields': sticker_field,
            'customFieldItems': custom_field_items
        }

        return super(Card, self).get_request(url=url_rquest,query=query)

    def update_card(self, id: str =None, name: str = None, desc: str = None, closed: bool = None, id_member: str = None,
                    id_atacment_cover: str = None, id_list: str = None, id_label: str = None, id_board:str = None, pos: (str,int) = None,
                    due: str = None, due_completed: bool = None, subscribed: str = None, address: str = None, location_name: str = None,
                    coodinates: str = None, cover: object = None):


        url_rquest = self.select_id(id=id)

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'desc': desc,
            'closed': closed,
            'idMembers': id_member,
            'idAttachmentCover': id_atacment_cover,
            'idList': id_list,
            'idLabels': id_label,
            'idBoard': id_board,
            'pos': pos,
            'due': due,
            'dueComplete:':due_completed,
            'subscribed': subscribed,
            'address': address,
            'locationName': location_name,
            'coordinates': coodinates,
            'cover': cover
        }

        return super(Card, self).put_request(url=url_rquest,query=query)


    def delete_card(self, id: str =None):
        url_rquest = self.select_id(id=id)

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Card, self).delete_request(url=url_rquest, query=query)

    def get_field(self,field: str, id: str =None):

        url_rquest = self.select_id(id=id, string=[f'{field}'])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_actions(self, id: str =None, filter: str = "commentCard, updateCard:idList"):
        url_rquest = self.select_id(id=id, string=['actions'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_attachments(self, id: str =None, fields: str = 'all', filter: (bool, str) = False):

        url_rquest = self.select_id(id=id, string=['attachments'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields,
            'filter': filter
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def create_attachment(self, id: str =None, name: str = None, file: str =None, mine_type: str = None, url: str = None,
                          set_cover: bool = False, ):
        url_rquest = self.select_id(id=id, string=['attachments'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'file': file,
            'mineType':mine_type,
            'url':url,
            'setCover': set_cover
        }

        return super(Card, self).post_request(url=url_rquest, query=query)

    def get_attachment(self,id_attachment: str, id: str =None, fields: list = None):
        url_rquest = self.select_id(id=id, string=[f'attachments', id_attachment])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def delete_attachment(self, id_attachment: str, id: str =None):
        url_rquest = self.select_id(id=id, string=[f'attachments', id_attachment])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).delete_request(url=url_rquest, query=query)

    def get_board(self, id: str =None, fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=['board'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_completed_checkitems(self, id: str =None, fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=['checkItemStates'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_checklists(self, id: str =None, check_items: str = 'all', checkitem_fields: str = 'all', filter: str = 'all',
                       fields: str = 'all'):

        url_rquest = self.select_id(id=id, string=['checklists'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'checkItems':check_items,
            'checkItem_fields': checkitem_fields,
            'filter': filter,
            'fields': fields
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def create_checklist(self, id: str =None, name: str = None, id_checklist_source: str = None, pos: (str, int) = 'top'):
        url_rquest = self.select_id(id=id, string=['checklists'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'idChecklistSource ': id_checklist_source,
            'pos': pos
        }

        return super(Card, self).post_request(url=url_rquest, query=query)

    def get_checkitem(self, id_check_item: str, id: str =None, fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=['checkItem', id_check_item])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def update_checkitem(self, id_check_item: str, id: str =None, name: str = None, state: str = None,
                        id_checklist:str = None, pos: (str, float) = None):
        url_rquest = self.select_id(id=id, string=['checkItem', id_check_item])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'state': state,
            'idChecklist': id_checklist,
            'pos': pos
        }

        return super(Card, self).put_request(url=url_rquest, query=query)

    def delete_checkitem(self,id_check_item: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['checkItem', id_check_item])

        query = {
            'key': self.app_key,
            'token': self.token,

        }

        return super(Card, self).delete_request(url=url_rquest, query=query)

    def get_list(self, id: str =None, fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=['list'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_members(self, id: str =None, fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=['members'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_members_who_voted(self, id: str =None,fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=['membersVoted'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def add_member_vote(self,value: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['membersVoted'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Card, self).post_request(url=url_rquest, query=query)

    def get_plugin_data(self, id: str =None):
        url_rquest = self.select_id(id=id, string=['pluginData'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_stickers(self, id: str =None, fields: str = 'all'):
        url_rquest = self.select_id(id=id, string=['attachments'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fields': fields
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def add_sticker(self, image: str, top: float, left: float, zindex: int, id: str =None, rotate: float = 0):
        url_rquest = self.select_id(id=id, string=['stickers'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'image': image,
            'top': top,
            'left': left,
            'zIndex': zindex,
            'rotate': rotate
        }

        return super(Card, self).post_request(url=url_rquest, query=query)

    def update_stiker(self, id_sticker: str, top: float, left: float, zindex: int, id: str =None, rotate: float = 0):
        url_rquest = self.select_id(id=id, string=['stickers'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'top': top,
            'left': left,
            'zIndex': zindex,
            'rotate': rotate
        }

        return super(Card, self).put_request(url=url_rquest, query=query)

    def delete_stiker(self,id_sticker: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['stickers', id_sticker])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).delete_request(url=url_rquest, query=query)

    def update_comment(self, id_action: str, text:str, id: str =None):
        url_rquest = self.select_id(id=id, string=['actions', id_action, 'comments'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'text': text
        }

        return super(Card, self).put_request(url=url_rquest, query=query)

    def delete_comment(self, id_action: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['actions', id_action, 'comments'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).delete_request(url=url_rquest, query=query)

    def update_costum_filed(self,id_custom_field: str, id: str =None):

        url_rquest = self.select_id(id=id, string=['customField', id_custom_field, 'item'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).put_request(url=url_rquest, query=query)

    def get_costum_field(self, id_custom_field: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['customField', id_custom_field, 'item'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def add_comment(self,text: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['actions', 'comments'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'text': text
        }

        return super(Card, self).post_request(url=url_rquest, query=query)

    def add_label(self, id: str =None, id_label: str = None):
        url_rquest = self.select_id(id=id, string=['idLabels'])

        query = {
            'key': self.app_key,
            'token': self.token,
            #'value': id_label
        }

        return super(Card, self).post_request(url=url_rquest, query=query)

    def add_member(self, id: str =None, id_member:str = None):
        url_rquest = self.select_id(id=id, string=['attachments', 'idMembers'])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': id_member
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def create_label(self, color: str, id: str =None, name:str = None):
        url_rquest = self.select_id(id=id, string=['labels'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).post_request(url=url_rquest, query=query)

    def remove_label(self, id: str =None):
        url_rquest = self.select_id(id=id, string=['labels'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def mark_card_notifications_as_read(self, id: str =None):
        url_rquest = self.select_id(id=id, string=['markAssociatedNotificationsRead'])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).post_request(url=url_rquest, query=query)

    def remove_member(self, id_member: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['idMembers', id_member])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).delete_request(url=url_rquest, query=query)

    def remove_member_vote(self, id_member: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['membersVoted', id_member])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).delete_request(url=url_rquest, query=query)

    def update_checkitem_on_checklist(self,id_checklist: str, id_check_item: str, id: str =None, pos: (str,float) = None):
        url_rquest = self.select_id(id=id, string=['checklist', id_checklist, 'checkItem', id_check_item])

        query = {
            'key': self.app_key,
            'token': self.token,
            'pos': pos
        }

        return super(Card, self).put_request(url=url_rquest, query=query)

    def delete_checklist(self,id_checklist: str, id: str =None):
        url_rquest = self.select_id(id=id, string=['checklists', id_checklist])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Card, self).delete_request(url=url_rquest, query=query)

