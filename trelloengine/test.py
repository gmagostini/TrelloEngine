#!/usr/bin/env python3
import time
import os

from trellocore import TrelloCore
import time
import json
from structures.logger import init_logger
""" tutta la parte de power up va gestita perche non fuozniona (tranne enable a power up)"""

def test_board(test,logger):
    board_id = test.member().get_boards(id=test.token().get_member()['id'])[0]['id']
    board_list = test.member().get_boards(id = test.token().get_member()['id'])
    board_valle = [id_board['id'] for id_board in board_list if id_board['name'] == 'valle']
    board = test.board(id=board_id)

    logger.info("GET MEBERSHIP")
    board.get_membership()
    logger.info("GET BOARD")
    board.get_board()
    logger.info("UPDATE BOARD")
    board.update_board(parameters={'name':'test per trello','labelNames/blue':'piergiorgio'})
    if board_valle:
        logger.info("DELETE BOARD")
        board.delete_board(id= board_valle[0])
    logger.info("GET FIELD")
    board.get_field(field='url')
    logger.info("GET ACTIONS")
    board.get_actions(filter='updateBoard')
    logger.info("GET CARDS")
    card_id = board.get_cards()[0]['id']
    logger.info("GET A CARD")
    board.get_a_card(id_card=card_id)
    logger.info("GET BOARD STARS")
    board.get_board_stars()
    logger.info("GET CHECKLIST")
    board.get_checklists()
    logger.info("CREATE CHECKLIST")
    board.create_checklist(id=board_id,name='kyuta')
    logger.info("GET FILTERED CARD")
    board.get_filtered_card(id=board_id, filter='visible')
    logger.info("GET CUSTOM FILESD")
    board.get_custom_fields()
    logger.info("GET LABELS")
    board.get_labels()
    logger.info("CREATE LABEL")
    board.create_label(id=board_id, name='Dilan', color='red')
    logger.info("CREATE LISTS")
    board.create_list(id=board_id, name='giovanni', pos='7')
    logger.info("GET LISTS")
    board.get_lists()
    logger.info("GET FILTERED LISTS")
    board.get_filtered_card(id=board_id, filter='open')
    logger.info("MEMBERS")
    board.get_members()
    logger.info("INVITE MEMBER")
    board.invite_member(id=board_id,email='liampreto@gmail.com',full_name='Mario Rossi')
    logger.info("ADD MEMBER")
    board.add_member(id=board_id,id_member='605308091396eb1afe3a39d4', type_member='normal')
    logger.info("CHANGE MEMBER STATUS")
    board.change_membership(id=board_id,id_membership='605308091396eb1afe3a39d4', type_member='admin')
    logger.info("REMOVE MEBER")
    board.remove_member(id=board_id, id_member='605308091396eb1afe3a39d4')
    logger.info("CREATE BOARD")
    board.create_board(name='valle')
    logger.info("CREATE CALENDER KEY")
    board.create_calender_key()
    logger.info("CREATE EMAIL KEY")
    board.create_email_key()
    logger.info("MARK BOARD AS VIEWD")
    board.mark_board_as_viewed()
    logger.info("GET POWER UPS")
    board.get_power_ups()
    logger.info("ENAMBE A POWER UP")
    board.enable_a_power_up(id=board_id, id_plugin='55a5d916446f517774210004')
    logger.info("DISABLE A POWER UP")
    board.disable_a_power_up(id=board_id, id_plugin=board.get_power_ups()[0]['id'])
    logger.info("DISABLE POWER UP")
    board.disable_power_up(power_up='calendar')
    logger.info("ENAMBEL POWER UP")
    board.enable_power_up(power_up='calendar')


def test_card(test,logger):
    board_id = test.member().get_boards(id=test.token().get_member()['id'])[0]['id']
    card = test.card()
    list_id = test.board(id=board_id).get_lists()[0]['id']
    logger.info("CREATE CARD")
    card_element = card.create_card(id_list=list_id,name='pluto',desc="Non era il più alto, ma nemmeno il più basso")
    logger.info("GET CARD")
    card = test.card(id=card_element['id'])
    card.get_card()
    logger.info("UPDATE CARD")
    card.update_card(id= card_element['id'], name="Cosimo il basso")
    logger.info("GET FIELD")
    card.get_field(field='name')
    logger.info("GET ACTIONS")
    card.get_actions()
    logger.info("CREATE ATTACHMENTE")
    card.create_attachment(url="http://esoteric-test.ddns.net:8081/")
    logger.info("GET ATTACHMENTS")
    attachment = card.get_attachments()[0]['id']
    logger.info("GET AN ATTACHMENT")
    card.get_attachment(id_attachment=attachment)
    logger.info("DELETE AN ATTACHMENT")
    card.delete_attachment(id_attachment=attachment)
    logger.info("GET BOARD")
    card.get_board()
    logger.info("update checkitem")







    logger.info("DELETE CARD")
    card.delete_card(id=card_element['id'])


def emoji(test,logger):
    logger.info("GET AVALIBLE EMOJI")
    #print(test.emoji().get_avalible_emoji())
    test.emoji().get_avalible_emoji()

def Main():
    logger = init_logger(dunder_name=__name__, level="DEBUG")
    with open(os.path.join("trelloengine",".env"),"r") as file:
        key =json.load(file)
    test = TrelloCore(app_key=key["api_key"], token=key["token"])

    # test_board(test,logger)
    #test_card(test,logger)
    #emoji(test,logger)






if __name__ == '__main__':
    Main()