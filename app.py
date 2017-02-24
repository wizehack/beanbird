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
	print("Get Request:")
	print(json.dumps(req, indent=4))

	res = processRequest(req)
	print("Request processed")

	res = json.dumps(res, indent=4)
	print(res)

	r = make_response(res)
	print(r)

	r.headers['Content-Type'] = 'application/json'

	return r


def processRequest(req):
	if req.get("result").get("action") != "echoAction":
		return {}
	res = makeEchoResponse(req)

	# pass to push server
	URL = "http://52.39.36.22:8000"
	requests.post(URL, data=json.dumps(req))
	return res;


def makeEchoResponse(req):
	result = req.get("result")

	if result is None:
		speech = "I can not accept your request"
		return {
			"speech": speech,
			"displayText": speech,
			"source": "apiai-echo-sample"
		}

	query = result.get("resolvedQuery")
	param = result.get("parameters").get("any")

	if query is None:
		speech = "Query is null"
		return {
			"speech": speech,
			"displayText": speech,
			"source": "apiai-echo-sample"
		}


	if param is None:
		speech = "Parameter is null"
		return {
			"speech": speech,
			"displayText": speech,
			"source": "apiai-echo-sample"
		}


	speech = "You said " + query + ". " + param

	return {
		"speech": speech,
		"displayText": speech,
		"source": "apiai-echo-sample"
	}


if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))

	print("Starting app on port %d" % port)

	app.run(debug=False, port=port, host='0.0.0.0')
