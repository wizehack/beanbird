import requests
import os
import json
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	print(">>> Request:")
	print(json.dumps(req, indent=4))

	action = req.get("result").get("action")
	param = req.get("result").get("parameters")

	if action is not None:
		query = makeQuery(action, param)
	else:
		print("action is None")

	print("query")
	print(json.dumps(query, indent=4))

	# pass to push server
	if query is not None:
		speech = "Got it"
		pushToServer(query)

	response = makeSpeechResponse(speech)
	res = json.dumps(response, indent=4)

	print(">>> Response:")
	print(res)

	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'

	return r


def pushToServer(query):
	URL = "http://52.39.36.22:8000"

	if query is not None:
		requests.post(URL, data=json.dumps(query))


def makeSpeechResponse(speech):
	if speech is None:
		speech = "Sorry, I cannot understand your command"

	return {
		"speech" : speech,
		"displayText" : speech,
		"source" : "beanbird"
	}


def makeQuery(action, param):
	print("aciton")
	print(action)

	print("param")
	print(json.dumps(param, indent=4))

	if param is None:
		print("param is None")
		return {}

	return {
		"action" : action,
		"param" : param
	}


if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))

	print("Starting app on port %d" % port)

	app.run(debug=False, port=port, host='0.0.0.0')
