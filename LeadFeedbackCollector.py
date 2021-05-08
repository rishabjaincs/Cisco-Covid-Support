import requests
import json
import flask
from flask import request,jsonify

def body_frame(leadId):
    body={
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2",
    "body": [
        {
            "type": "TextBlock",
            "text": "Does the above Lead Helped ?",
            "wrap": True,
            "size": "Medium",
            "weight": "Lighter",
            "color": "Accent",
            "isSubtle": True
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "YES",
                    "style": "positive",
                    "data": {
                        "status": "helpful",
                        "data": True,
                        "leadId":leadId
                    }
                },
                {
                    "type": "Action.Submit",
                    "title": "Out Of Stock",
                    "style": "destructive",
                    "data": {
                        "status": "helpful",
                        "data": None,
                        "leadId":leadId
                    }
                },
                {
                    "type": "Action.Submit",
                    "title": "NO",
                    "style": "destructive",
                    "data": {
                        "status": "helpful",
                        "data": False,
                        "leadId":leadId
                    }
                }
            ],
            "horizontalAlignment": "Center"
        }
    ]
}
    return body


def LeadFeedback(roomId,parentId,token,leadId):
    url="https://webexapis.com/v1/messages/"

    headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}

    body=body_frame(leadId)

    card={
     "roomId": roomId,
     "parentId":parentId,
      "markdown": "Feedback regarding the provided Lead !!",
      "attachments": [
        {
          "contentType": "application/vnd.microsoft.card.adaptive",
          "content": body
        }
      ]
    }


    payload=json.dumps(card)
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.json())
    print(response.status_code)
    return response.status_code

