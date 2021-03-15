from .base import Base


class Board(Base):

    def __init__(self, app_key: str, token: str,id=None):
        super(Board, self).__init__(app_key=app_key,token=token, id=id)
        self.request_url = self.request_url + "/boards"

    def creata_board(self, name, **kwargs):
        """
        :param kwargs: name desc descData closed idOrganization idEnterprise pinned url shortUrl prefs labelNames
        :return: None
        """
        url_temp = self.request_url

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            **kwargs
        }

        return super(Board, self).post_request(url_temp, query)

    def update_board(self, id=None,**kwargs):
        """
        aggiorna la tabella seondo i paramteri passsati in kwarg \n
        :param id:
        :param kwargs: name desc descData closed idOrganization idEnterprise pinned url shortUrl prefs labelNames
        :return: None
        """
        if id == None:
            url_temp = self.request_url + f"/{self.id}"
        else:
            url_temp = self.request_url + f"/{id}"

        query = {
            'key': self.app_key,
            'token': self.token,
            **kwargs
        }

        return super(Board, self).put_request(url_temp, query)

    def delete_board(self, id=None):
        if id == None:
            url_temp = self.request_url + f"/{self.id}"
        else:
            url_temp = self.request_url + f"/{id}"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).delete_request(url_temp, query)


    def get_board(self, id=None):
        if id == None:
            url_temp = self.request_url + f"/{self.id}"
        else:
            url_temp = self.request_url + f"/{id}"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)


    def get_actions(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/actions"
        else:
            url_temp = self.request_url + f"/{id}/actions"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def get_cards(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/cards"
        else:
            url_temp = self.request_url + f"/{id}/cards"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def get_checklists(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/checklists"
        else:
            url_temp = self.request_url + f"/{id}/checklists"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def get_custom_fields(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/customFields"
        else:
            url_temp = self.request_url + f"/{id}/customFields"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)


    def get_labels(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/labels"
        else:
            url_temp = self.request_url + f"/{id}/labels"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def get_lists(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/lists"
        else:
            url_temp = self.request_url + f"/{id}/lists"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)



