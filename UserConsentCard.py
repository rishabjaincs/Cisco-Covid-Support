import requests
import json
import flask
from flask import request,jsonify






def approval_frame(inputs,user_info,parent_id):
    body={
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
            {
            "type": "TextBlock",
            "text": "No Result found, Please confirm if we need further support !!",
            "color": "Warning",
            "horizontalAlignment": "Center",
            "size": "Small",
            "spacing": "Large"
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "YES",
                    "style": "positive",
                    "id": "yes",
                    "data":{
                      "access":True,
                      "status":inputs['status'],
                      "UserEmail":user_info['emails'][0],
                      "UserName":user_info['firstName'],
                      "state":inputs['state'],
                      "pincode":inputs['pincode'],
                      "parentId":parent_id,
                      "req1":inputs['req1'],
                      "RequestElaborate":inputs['RequestElaborate'],
                      "sev":inputs['sev']
                  }
                },
                {
                    "type": "Action.Submit",
                    "title": "NO",
                    "style": "destructive",
                    "id": "no",
                    "data":{
                      "access":False,
                      "status":inputs['status'],
                      "pincode":inputs['pincode'],
                      "UserEmail":user_info['emails'][0],
                      "UserName":user_info['firstName'],
                      "state":inputs['state'],
                      "parentId":parent_id,
                      "req1":inputs['req1'],
                      "RequestElaborate":inputs['RequestElaborate'],
                      "sev":inputs['sev']

                  }
                }
            ],
            "separator": True,
            "horizontalAlignment": "Center"
        }
        ]}

    return body


def BuddyAssistApproval(inputs,user_info,parent_id,token):
    body=approval_frame(inputs,user_info,parent_id)
    url="https://webexapis.com/v1/messages"

    headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}
         
    card={
      "toPersonEmail": user_info['emails'][0],
      "parentId": parent_id,
      "markdown": "Approval or Decline Button for Moderators !!!",
      "attachments": [
        {
          "contentType": "application/vnd.microsoft.card.adaptive",
          "content": body
        }
      ]
    }

    payload=json.dumps(card)
    response = requests.request("POST", url, data=payload, headers=headers)
    send_message=response.json()
    return send_message