from trellocore import TrelloCore, dict_to_string
import os
import json
import sqlite3


def create_connection(db_file):
	""" create a database connection to the SQLite database
	specified by db_file
	:param db_file: database file
	:return: Connection object or None
	"""
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Exception as e:
		print(e)

	return conn

class TrelloInternal:
	
	
	def __init__ (self):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"ENV",".env"),"r") as file:
			key =json.load(file)
		self.trellocore = TrelloCore(app_key=key["api_key"], token=key["token"])

		db_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),"ENV", "database.db")
		conn = create_connection(db_file=db_file)




	def filter_action(self, request: dict):
		if 'action' in request.keys():
				if 'CheckItem' in request['action']['type']:
					#print(dict_to_string(request))
					temp = request['action']['data']
					print
					checkitem = self.trellocore.checklist(id=temp['checklist']['id']).get_checkitem(id_check_item=temp['checkItem']['id'])
					print(dict_to_string(checkitem))
		else:
			print("[ERROR] data not valid")

	