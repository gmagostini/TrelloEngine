from .base import Base


class List(Base):

    def __init__(self, app_key: str, token: str,id=None):
        super(List, self).__init__(app_key=app_key,token=token)
        self.id = id
        self.url = self.url + "/lists"

    def get_cards(self, id=None):

        if id == None:
            url_temp = self.url + f"/{self.id}/cards"
        else:
            url_temp = self.url + f"/{id}/cards"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(List, self).make_request(url_temp,query,headers = {"Accept": "application/json"})