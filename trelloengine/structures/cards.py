from .base import Base


class Card(Base):

    def __init__(self, app_key: str, token: str, id=None):
        super(Card, self).__init__(app_key=app_key, token=token, id=id)
        self.request_url = self.request_url + "/boards"

    def create_card(self):
        pass

    def get_card(self):
        pass

    def update_card(self):
        pass

    def delete_card(self):
        pass

    def get_field(self):
        pass

    def get_attachments(self):
        pass

    def create_attachment(self):
        pass

    def get_attachment(self):
        pass

    def delete_attachment(self):
        pass

    def get_board(self):
        pass

    def get_checkitems(self):
        pass

    def get_checklists(self):
        pass

    def create_checklist(self):
        pass

    def get_checkitem(self):
        pass

    def update_checkitem(self):
        pass

    def delete_checkitem(self):
        pass

    def get_list(self):
        pass

    def get_members(self):
        pass

    def get_members_who_voted(self):
        pass

    def add_member_vote(self):
        pass

    def get_plugin_data(self):
        pass

    def get_stickers(self):
        pass

    def add_sticker(self):
        pass

    def update_stiker(self):
        pass

    def delete_stiker(self):
        pass

    def update_comment(self):
        pass

    def delete_comment(self):
        pass

    def update_costum_filed(self):
        pass

    def get_costum_field(self):
        pass

    def add_comment(self):
        pass

    def add_label(self):
        pass

    def add_member(self):
        pass

    def create_label(self):
        pass

    def remove_label(self):
        pass

    def remove_member(self):
        pass

    def remove_member_vote(self):
        pass

    def update_checkitem_on_checklist(self):
        pass

    def delete_checklist(self):
        pass

