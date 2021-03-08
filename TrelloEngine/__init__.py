#!/usr/bin/env python3
from TrelloEngine.TrelloCore import TrelloCore
import json
def Main():
    with open(".env","r") as file:
        key =json.load(file)
    test = TrelloCore(app_key=key["api_key"], token=key["token"])
    liste = []
    member = test.tokens.get_member()
    print(member)
    board = test.member.get_boards(member['id'])
    print(board[0])
    liste.append(list(board[0].keys()))
    lista = test.board.get_lists(board[0]['id'])
    print(lista[0])
    liste.append(list(lista[0].keys()))
    card = test.board.get_cards(board[0]['id'])
    print(card[0])
    liste.append(list(card[0].keys()))
    label = test.board.get_labels(board[0]['id'])
    print(label[0])
    liste.append(list(label[0].keys()))
    print(f"liste: {liste}")
    elementi_comuni =set(liste[0]).intersection(*liste)
    print(f"elementi in comune: {elementi_comuni}")
if __name__ == '__main__':
    Main()