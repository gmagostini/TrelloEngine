from .structures.board import Board
from .structures.cards import Card
from .structures.checklist import Checklist
from .structures.customFields import CustumField
from .structures.emoji import Emoji
from .structures.enterprises import Enterprise
from .structures.labels import Label
from .structures.list import List
from .structures.member import Member
from .structures.notifications import Notification
from .structures.search import Search
from .structures.tokens import Tokens
from .structures.webhooks import Webhooks



class TrelloCore:


    def __init__(self, app_key : str, token : str):
        self.app_key = app_key
        self.token = token

        self.board = Board(app_key, token)
        self.card = Card(app_key, token)
        self.checklist = Checklist(app_key, token)
        self.custumField = CustumField(app_key, token)
        self.emoji = Emoji(app_key, token)
        self.enterprise = Enterprise(app_key, token)
        self.label = Label(app_key, token)
        self.list = List(app_key, token)
        self.member = Member(app_key, token)
        self.notification = Notification(app_key, token)
        self.Search = Search(app_key, token)
        self.tokens = Tokens(app_key, token)
        self.webhooks = Webhooks(app_key, token)






