from .base import Base


class Card(Base):

    def __init__(self, app_key: str, token: str, id=None):
        super(Card, self).__init__(app_key=app_key, token=token, id=id)
        self.request_url = self.base_url + "/cards"

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
            'urlSource': url_source,
            'fileSource': file_source,
            'idCardSource': id_card_source,
            'keepFromSource': keep_from_source,
            'andress': address,
            'locationName': location_name,
            'coordinates': coordinate
        }

        return super(Card, self).post_request(url=self.request_url,query=self.bool_to_string(query=query))

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

    def update_card(self, parameters: dict = {}, id: str =None):
        """

        :param parameters:
        :param id:
        :param **name
        :param **desc
        :param **closed
        :param **idMembers
        :param **idAttachmentCover
        :param **idList
        :param **idLabels
        :param **idBoard
        :param **pos
        :param **due
        :param **dueComplete
        :param **subscribed
        :param **address
        :param **locationName
        :param **coordinates
        :param **cover
        :return:
        """

        url_rquest = self.select_id(id=id)

        query = {
            'key': self.app_key,
            'token': self.token,
            **parameters
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

        url_rquest = self.select_id(id=id, string=f'{field}')

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_actions(self, id: str =None, filter: str = "commentCard, updateCard:idList"):
        url_rquest = self.select_id(id=id, string='actions')

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def get_attachments(self, id: str =None, fields: str = 'all', filter: (bool, str) = False):

        url_rquest = self.select_id(id=id, string='attachments')

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(Card, self).get_request(url=url_rquest, query=query)

    def create_attachment(self, id: str =None):
        pass

    def get_attachment(self, id: str =None):
        pass

    def delete_attachment(self, id: str =None):
        pass

    def get_board(self, id: str =None):
        pass

    def get_checkitems(self, id: str =None):
        pass

    def get_checklists(self, id: str =None):
        pass

    def create_checklist(self, id: str =None):
        pass

    def get_checkitem(self, id: str =None):
        pass

    def update_checkitem(self, id: str =None):
        pass

    def delete_checkitem(self, id: str =None):
        pass

    def get_list(self, id: str =None):
        pass

    def get_members(self, id: str =None):
        pass

    def get_members_who_voted(self, id: str =None):
        pass

    def add_member_vote(self, id: str =None):
        pass

    def get_plugin_data(self, id: str =None):
        pass

    def get_stickers(self, id: str =None):
        pass

    def add_sticker(self, id: str =None):
        pass

    def update_stiker(self, id: str =None):
        pass

    def delete_stiker(self, id: str =None):
        pass

    def update_comment(self, id: str =None):
        pass

    def delete_comment(self, id: str =None):
        pass

    def update_costum_filed(self, id: str =None):
        pass

    def get_costum_field(self, id: str =None):
        pass

    def add_comment(self, id: str =None):
        pass

    def add_label(self, id: str =None):
        pass

    def add_member(self, id: str =None):
        pass

    def create_label(self, id: str =None):
        pass

    def remove_label(self, id: str =None):
        pass

    def remove_member(self, id: str =None):
        pass

    def remove_member_vote(self, id: str =None):
        pass

    def update_checkitem_on_checklist(self, id: str =None):
        pass

    def delete_checklist(self, id: str =None):
        pass

