from flask import Flask, request, Response
from flask import json
from waitress import serve

from trellocore import dict_to_string
from trellointernal import TrelloInternal

def create_app(arg1=None, arg2=None):
	app = Flask(__name__)
	trello = TrelloInternal()
	@app.route('/', methods=['GET','POST'])
	def internal_trello_switch():
		print(request)
		#dict_to_string(request.json)
		if request.json:
			trello.filter_action(request.json)
		else:
			print("[ERROR] data not valid")
		return app.response_class(status=200, mimetype='application/json')

	return app

if __name__ == "__main__":
	app = create_app()
	serve(app=app,host='0.0.0.0', port=8080 )
	#app.run(host='0.0.0.0')