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

    board_id = test.member.get_boards(id = test.tokens.get_member()['id'])[0]['id']
    #print(f"mebership: {test.board.get_membership(id = board_id)}")
    #print(f"board: {test.board.get_board(id=board_id)}")
    #print(f"board update: {test.board.update_board(id=board_id, parameters={'name':'test per trello','labelNames/blue':'piergiorgio'})}")
    #print(f"field: {test.board.get_field(id=board_id, field='url')}")
    #print(f"actions: {test.board.get_actions(id=board_id, filter='updateBoard')}")
    card_id = test.board.get_cards(id=board_id)[0]['id']
    #print(f"id_card: {card_id}")
    #print(f"card: {test.board.get_a_card(id_card=card_id,id=board_id)}")
    #print(f"boardStar: {test.board.get_board_stars(id=board_id)}")
    #print(f"checklist: {test.board.get_checklists(id=board_id)}")
    #print(f"create checklist: {test.board.create_checklist(id=board_id,name='kyuta')}")
    #print(f"cards: {test.board.get_cards(id=board_id)}")
    #print(f"filtered cards: {test.board.get_filtered_card(id=board_id, filter='visible')}")
    #print(f"costums field: {test.board.get_custom_fields(id=board_id)}")
    #print(f"labels: {test.board.get_labels(id=board_id)}")
    #print(f"create lacbel: {test.board.create_label(id=board_id, name='Dilan', color='red')}")
    #print(f"lists: {test.board.get_lists(id=board_id)}")
    #print(f"create list: {test.board.create_list(id=board_id, name='giovanni', pos='7')}")
    #print(f"lists: {test.board.get_lists(id=board_id)}")
    #print(f"filtered lists: {test.board.get_filtered_card(id=board_id, filter='open')}")
    #print(f"members: {test.board.get_members(id=board_id)}")
    #print(f"invite member email: {test.board.invite_member(id=board_id,email='liampreto@gmail.com',full_name='Mario Rossi')}")
    #print(f"add member: {test.board.add_member(id=board_id,id_member='605308091396eb1afe3a39d4', type_member='normal')}")
    #time.sleep(3)
    #print(f"change mebership: {test.board.change_membership(id=board_id,id_membership='605308091396eb1afe3a39d4', type_member='admin')}")
    #time.sleep(3)
    #print(f"delete member: {test.board.remove_member(id=board_id, id_member='605308091396eb1afe3a39d4')}")
    #print(f"create board: {test.board.creata_board(name='valle')}")
    #print(f"create calendarKey: {test.board.create_calender_key(id=board_id)}")
    print(f"create meail key: {test.board.create_email_key(id=board_id)}")
    print(f"mark board as viewed: {test.board.mark_board_as_viewed(id=board_id)}")
    print(f"get powrs up: {test.board.get_power_ups(id=board_id)}")
    #print(f"enable a power up: {test.board.enable_a_power_up(id=board_id, id_plugin='55a5d916446f517774210004')}")
    #print(f"enable a power up: {test.board.disable_a_power_up(id=board_id, id_plugin=test.board.get_power_ups(id=board_id)[0]['id'])}")
    print(f"enable : {test.board.enable_power_up(id=board_id, power_up='calendar')}")
    print(f"disable : {test.board.disable_power_up(id=board_id,power_up='calendar')}")
if __name__ == '__main__':
    Main()