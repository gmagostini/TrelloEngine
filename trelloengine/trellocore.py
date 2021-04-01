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
from structures.search import Search
from structures.token import Token
from structures.webhook import Webhook



class TrelloCore:


    def __init__(self, app_key : str = None, token : str = None):

        if app_key is None or token is None:
            raise ValueError('app_key and token are not set correctly')

        self.app_key = app_key
        self.app_token = token


    def board(self, id: str = None) -> Board:
        return Board(app_key=self.app_key, token=self.app_token, id=id)

    def card(self, id: str = None) -> Card:
        return Card(app_key=self.app_key, token=self.app_token, id=id)

    def checklist(self, id: str = None) -> Checklist:
        return Checklist(app_key=self.app_key, token=self.app_token, id=id)

    def custom_field(self, id: str = None) -> CustumField:
        return CustumField(app_key=self.app_key, token=self.app_token, id=id)

    def emoji(self, id: str = None) -> Emoji:
        return Emoji(app_key=self.app_key, token=self.app_token, id=id)

    def enterprises(self, id: str = None) -> Enterprise:
        return Enterprise(app_key=self.app_key, token=self.app_token, id=id)

    def label(self, id: str = None) -> Label:
        return Label(app_key=self.app_key, token=self.app_token, id=id)

    def list(self, id: str = None) -> List:
        return List(app_key=self.app_key, token=self.app_token, id=id)

    def member(self, id: str = None) -> Member:
        return Member(app_key=self.app_key, token=self.app_token, id=id)

    def notification(self, id: str = None) -> Notification:
        return Notification(app_key=self.app_key, token=self.app_token, id=id)

    def organization(self, id: str = None) -> Organization:
        return Organization(app_key=self.app_key, token=self.app_token, id=id)

    def search(self, id: str = None) -> Search:
        return Search(app_key=self.app_key, token=self.app_token, id=id)

    def token(self) -> Token:
        return Token(app_key=self.app_key, token=self.app_token)

    def webhook(self, id: str = None) -> Webhook:
        return Webhook(app_key=self.app_key, token=self.app_token, id=id)




