#!/usr/bin/env python3
from .base import Base


class Emoji(Base):

    def __init__(self, app_key: str, token: str, id=None, use_log = False):
        super(Emoji, self).__init__(app_key=app_key, token=token,id=id, use_log=use_log)
        self.base_url = self.base_url + "/emoji"

    def get_avalible_emoji(self, locale: str = None, spritesheets: bool = False):

        query = {
            'key': self.app_key,
            'token': self.token,
            'locale': locale,
            'spritesheets': spritesheets
        }

        return super(Emoji, self).get_request(url=self.base_url, query=query)