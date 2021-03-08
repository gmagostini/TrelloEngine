from .base import Base


class Member(Base):

    def __init__(self, app_key: str, token: str,id=None):
        super(Member, self).__init__(app_key=app_key,token=token)
        self.id = id
        self.url = self.url + f"/members"

    def get_boards (self, id=None):

        if id == None:
            url_temp = self.url + f"/{self.id}/boards"
        else:
            url_temp = self.url + f"/{id}/boards"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Member, self).make_request(url_temp,query,headers = {"Accept": "application/json"})
