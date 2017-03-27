# Api.ai - sample webhook implementation in Python

This is a webhook implementation that gets Api.ai classification JSON (i.e. a JSON output of Api.ai /query endpoint) and returns a fulfillment response.
Additionally, this extracts action and params from the JSON and sends it to push server

More info about Api.ai webhooks could be found here:
[Api.ai Webhook](https://docs.api.ai/docs/webhook)

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a tv control fulfillment service that takes the tv control parameters from the action, returns user's input

The service packs the result in the Api.ai webhook-compatible response JSON and returns it to Api.ai.
