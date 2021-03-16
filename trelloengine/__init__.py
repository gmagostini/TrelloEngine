#!/usr/bin/env python3
import time

from trelloengine.trellocore import TrelloCore
import json


def Main():
    with open(".env","r") as file:
        key =json.load(file)
    test = TrelloCore(app_key=key["api_key"], token=key["token"])

    board_id = test.member.get_boards(id = test.tokens.get_member()['id'])[0]['id']
    print(f"mebership: {test.board.get_membership(id = board_id)}")

    print(f"filed: {test.board.get_field(id=board_id, field='url')}")
    print(f"actions: {test.board.get_actions(id=board_id, filter='updateBoard')}")
    card_id = test.board.get_cards(id=board_id)[0]['id']
    print(f"id_card: {card_id}")
    print(f"card: {test.board.get_a_card(id_card=card_id,id=board_id)}")
    print(f"board star: {test.board.get_board_stars(id=board_id)}")
if __name__ == '__main__':
    Main()