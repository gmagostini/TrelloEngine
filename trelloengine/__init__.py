#!/usr/bin/env python3
import time

from trelloengine.trellocore import TrelloCore
import time
import json
""" tutta la parte de power up va gestita perche non fuozniona (tranne enable a power up)"""

def Main():
    with open(".env","r") as file:
        key =json.load(file)
    test = TrelloCore(app_key=key["api_key"], token=key["token"])

    """board_id = test.member().get_boards(id = test.token().get_member()['id'])[0]['id']
    board = test.board(id=board_id)
    print(f"mebership: {board.get_membership(id = board_id)}")
    print(f"board: {board.get_board(id=board_id)}")
    print(f"board update: {board.update_board(id=board_id, parameters={'name':'test per trello','labelNames/blue':'piergiorgio'})}")
    print(f"field: {board.get_field(id=board_id, field='url')}")
    print(f"actions: {board.get_actions(id=board_id, filter='updateBoard')}")
    card_id = board.get_cards()[0]['id']
    print(f"id_card: {card_id}")
    print(f"card: {board.get_a_card(id_card=card_id,id=board_id)}")
    print(f"boardStar: {board.get_board_stars(id=board_id)}")
    print(f"checklist: {board.get_checklists(id=board_id)}")
    print(f"create checklist: {board.create_checklist(id=board_id,name='kyuta')}")
    print(f"cards: {board.get_cards(id=board_id)}")
    print(f"filtered cards: {board.get_filtered_card(id=board_id, filter='visible')}")
    print(f"costums field: {board.get_custom_fields(id=board_id)}")
    print(f"labels: {board.get_labels(id=board_id)}")
    print(f"create lacbel: {board.create_label(id=board_id, name='Dilan', color='red')}")
    print(f"lists: {board.get_lists(id=board_id)}")
    print(f"create list: {board.create_list(id=board_id, name='giovanni', pos='7')}")
    print(f"lists: {board.get_lists(id=board_id)}")
    print(f"filtered lists: {board.get_filtered_card(id=board_id, filter='open')}")
    print(f"members: {board.get_members(id=board_id)}")
    print(f"invite member email: {board.invite_member(id=board_id,email='liampreto@gmail.com',full_name='Mario Rossi')}")
    print(f"add member: {board.add_member(id=board_id,id_member='605308091396eb1afe3a39d4', type_member='normal')}")
    print(f"change mebership: {board.change_membership(id=board_id,id_membership='605308091396eb1afe3a39d4', type_member='admin')}")
    print(f"delete member: {board.remove_member(id=board_id, id_member='605308091396eb1afe3a39d4')}")
    print(f"create board: {board.creata_board(name='valle')}")
    print(f"create calendarKey: {board.create_calender_key(id=board_id)}")
    print(f"create meail key: {board.create_email_key()}")
    print(f"mark board as viewed: {board.mark_board_as_viewed()}")
    print(f"get powrs up: {board.get_power_ups()}")
    print(f"enable a power up: {board.enable_a_power_up(id=board_id, id_plugin='55a5d916446f517774210004')}")
    print(f"enable a power up: {board.disable_a_power_up(id=board_id, id_plugin=board.get_power_ups(id=board_id)[0]['id'])}")
    print(f"disable : {board.disable_power_up(power_up='calendar')}")
    print(f"enable : {board.enable_power_up(power_up='calendar')}")"""


    card = test.card(test.board().get_cards()[0]['id'])


if __name__ == '__main__':
    Main()