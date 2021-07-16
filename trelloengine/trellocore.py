#!/usr/bin/env python3
from structures.board import Board
from structures.card import Card
from structures.checklist import Checklist
from structures.customField import CustumField
from structures.emoji import Emoji
from structures.enterprise import Enterprise
from structures.label import Label
from structures.list import List
from structures.member import Member
from structures.notification import Notification
from structures.organization import Organization
from structures.plugin import Plugin
from structures.search import Search
from structures.token import Token
from structures.webhook import Webhook

import json


def dict_to_string(data):
    return  json.dumps(data, sort_keys=True, indent=4, separators=(",", ": "))


def json_to_string(data):
    return json.dumps(json.load(data), sort_keys=True, indent=4, separators=(',', ': '))

class TrelloCore:


    def __init__(self, app_key : str = None, token : str = None, logger_level = None, use_log:bool = False):

        if app_key is None or token is None:
            raise ValueError('app_key and token are not set correctly')

        self.app_key = app_key
        self.app_token = token
        self.use_log = use_log

  
    def swith_loggingging(self,local: bool):

        if local or self.use_log:
            return True
        else:
            return False

    def board(self, id: str = None, use_log: bool = False) -> Board:
        return Board(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def card(self, id: str = None, use_log: bool = False) -> Card:
        return Card(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def checklist(self, id: str = None, use_log: bool = False) -> Checklist:
        return Checklist(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def custom_field(self, id: str = None, use_log: bool = False) -> CustumField:
        return CustumField(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def emoji(self, id: str = None, use_log: bool = False) -> Emoji:
        return Emoji(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def enterprises(self, id: str = None, use_log: bool = False) -> Enterprise:
        return Enterprise(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def label(self, id: str = None, use_log: bool = False) -> Label:
        return Label(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def list(self, id: str = None, use_log: bool = False) -> List:
        return List(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def member(self, id: str = None, use_log: bool = False) -> Member:
        return Member(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def notification(self, id: str = None, use_log: bool = False) -> Notification:
        return Notification(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def organization(self, id: str = None, use_log: bool = False) -> Organization:
        return Organization(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def plugin(self, id: str = None, use_log: bool = False) -> Plugin:
        return Plugin(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def search(self,use_log= False) -> Search:
        return Search(app_key=self.app_key, token=self.app_token, id=id, use_log=self.swith_loggingging(use_log))

    def token(self,use_log= False) -> Token:
        return Token(app_key=self.app_key, token=self.app_token, use_log=self.swith_loggingging(use_log))

    def webhook(self, id: str = None, use_log: bool = False) -> Webhook:
        return Webhook(app_key=self.app_key, token=self.app_token, use_log=self.swith_loggingging(use_log))




