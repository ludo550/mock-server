import json
import random
import uuid
from datetime import datetime
import eventlet
from marshmallow import ValidationError

eventlet.monkey_patch()
from flask import Flask, session, request
from flask_bootstrap import Bootstrap
from flask import jsonify
from dotenv import load_dotenv
from.bofa import BaseSchema

def is_english(s):
    return s.isascii()


load_dotenv()
app = Flask(__name__)

app.config["SECRET_KEY"] = uuid.uuid4().hex

Bootstrap(app)


@app.context_processor
def inject_now():
    """ sends datetime to templates as 'now' """
    return {'now': datetime.utcnow()}

bofa_response = { "response": {
    "transactionIdentification": "",
    "paymentStatus": "Received By Bank",
    "endToEndIdentification": "{{$body 'debtorAccountId'}}{{$body 'clientPaymentId'}}",
    "reason": []
    }, "status": 200
}

@app.route("/bofamock", methods=['POST'])
def bofamock():
    request_data = request.json
    # try:
    #     schema = BaseSchema()
    #     schema.add()
    #     schema.load(request_data)
    # except ValidationError as err:
    #     # Return a nice message if validation fails
    #     return jsonify(err.messages), 400
    try:
        file = open('bofa_mock.json', 'r')
        bofa_resp = json.loads(file.read())
    except:
        bofa_resp = bofa_response
    if 'endToEndIdentification' in bofa_resp['response']:
        bofa_resp['response']['endToEndIdentification'] = f"{request_data['debtorAccountId']}{request_data['clientPaymentId']}"
    if 'transactionIdentification' in bofa_resp['response']:
        bofa_resp['response']['transactionIdentification'] = "A0L{}".format(random.randint(1000000000000, 9999999999999))

    return jsonify(bofa_resp['response']), bofa_resp['status']

@app.route("/bofamockconfigure", methods=['POST'])
def bofamockconfigure():
    bofa_resp = request.json
    file = open('bofa_mock.json', 'w+')
    file.write(json.dumps(bofa_resp))
    return jsonify({"success": True, "config": bofa_resp['response']}), bofa_resp['status']


def create_app():
    return app
