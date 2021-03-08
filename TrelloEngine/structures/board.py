from .base import Base


class Board(Base):


    def __init__(self, app_key: str, token: str,id=None):
        super(Board, self).__init__(app_key=app_key,token=token)
        self.id = id
        self.url = self.url + "/boards"





    def get_actions(self, id=None):

        if id == None:
            url_temp = self.url + f"/{self.id}/actions"
        else:
            url_temp = self.url + f"/{id}/actions"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).make_request(url_temp,query)

    def get_cards(self, id=None):

        if id == None:
            url_temp = self.url + f"/{self.id}/cards"
        else:
            url_temp = self.url + f"/{id}/cards"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).make_request(url_temp, query)

    def get_checklists(self, id=None):

        if id == None:
            url_temp = self.url + f"/{self.id}/checklists"
        else:
            url_temp = self.url + f"/{id}/checklists"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).make_request(url_temp,query)

    def get_custom_fields(self, id=None):

        if id == None:
            url_temp = self.url + f"/{self.id}/customFields"
        else:
            url_temp = self.url + f"/{id}/customFields"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).make_request(url_temp,query)


    def get_labels(self, id=None):

        if id == None:
            url_temp = self.url + f"/{self.id}/labels"
        else:
            url_temp = self.url + f"/{id}/labels"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).make_request(url_temp,query)

    def get_lists(self, id=None):

        if id == None:
            url_temp = self.url + f"/{self.id}/lists"
        else:
            url_temp = self.url + f"/{id}/lists"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).make_request(url_temp,query)