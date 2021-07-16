from trellocore import TrelloCore
import os
import json

trellocore = None
with open(os.path.join(os.path.abspath(''),"ENV",".env"),"r") as file:
    key =json.load(file)
    trellocore = TrelloCore(app_key=key["api_key"], token=key["admin_token"])

member_id = trellocore.token().get_member()['id']
boards = trellocore.member().get_boards(id=member_id, fields="id,name")
print(boards)
ufficio = [board['id'] for board in boards if "UFFICIO" == board['name']][0]
print(ufficio)

board = trellocore.board(id=ufficio)
#print(board_id)
liste = board.get_lists(fields="id,name", filter='open')
#[print(elemento) for elemento in liste]
bacheche_personali = [name['id'] for name in liste if "bacheche personali" == name['name'] ]
print(bacheche_personali)

cards = trellocore.list(id=bacheche_personali[0]).get_cards()
cards = [elemento['name'].split(':') for elemento in cards][1:]
bacheche_personali = [{'username': elemento[0],'board_name': elemento[1] } for elemento in cards]
print(bacheche_personali)

for elemento in bacheche_personali: 
    elemento['id'] = (trellocore.member(id=elemento['username']).get_member(fields="id")['id'])

for elemento in bacheche_personali:
    if elemento['username'] == 'zaninelli':
      elemento['type'] = 1
      elemento['token'] = key["admin_token"]
    else:
        elemento['type'] = 0
        elemento['token'] = None
    print(elemento)

for elemento in bacheche_personali:
    for board in boards:
        if board['name'] == elemento['board_name']:
            elemento['board_id'] =  board['id']
            #print(elemento)


for elemento in bacheche_personali:
    board = trellocore.board(id=elemento['board_id'])
    liste = board.get_lists(fields="id,name", filter='open')

    elemento['list_id'] = [name['id'] for name in liste if "MANAGMEENT" == name['name'] ]

print(bacheche_personali[0].keys())

import sqlite3
import os
db_file = os.path.join(os.path.abspath(''),"ENV", "database.sqlite3")
conn = sqlite3.connect(db_file)
cur = conn.cursor()



query = """
		CREATE TABLE IF NOT EXISTS Employee (
			id CHAR(24),
			username CHAR(50),
			board_id CHAR(24),
            board_name CHAR(50),
			list_id CHAR(24),
			token CHAR(50),
            type INT,
			PRIMARY KEY (id)
		);
        """
cur.execute(query)

for line in bacheche_personali:
    print(line)

for line in bacheche_personali:
    sql = f"""
    INSERT INTO Employee(id, username, board_id, board_name, list_id, token, type)
    VALUES(?,?,?,?,?,?,?);
    """
    value =(line['id'],line['username'],line['board_id'],line['board_name'],line['list_id'][0],line['token'],line['type'])
    cur.execute(sql,value)