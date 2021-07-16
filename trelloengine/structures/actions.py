#!/usr/bin/env python3
from .base import Base


class Actions(Base):


    def __init__(self, app_key: str, token: str,id=None,  use_log = False):
        super(Actions, self).__init__(app_key=app_key,token=token)
        self.id = id
        self.url = self.url + "/boards"