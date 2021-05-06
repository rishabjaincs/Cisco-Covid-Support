import requests
import json
import flask
from flask import request,jsonify
from manager import AttachmentValidator
from manager import FurtherAssistanceNeeded

# My JOB is to listen all the messages recieved to the BOT ( EVERYTHING ) that hookbuster will throw

app = flask.Flask(__name__)
app.config["DEBUG"]

@app.route('/',methods=['POST'])
def post():
    posted_data = request.json
    print("Here's the RAW Data received from Attachments:")
    print("======================================================================================")
    print(posted_data)
    print("======================================================================================")
    if 'access' in posted_data['data']['inputs'].keys():
    	FurtherAssistanceNeeded(posted_data)
    else:
        AttachmentValidator(posted_data)
    return "The data is processing !!"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True) # To run our server