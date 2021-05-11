import requests
import json
import flask
from flask import request,jsonify




def body_frame(inputs,user_info):
    if 'avatar' in user_info.keys():
        user_profile=user_info['avatar']
    else:
        user_profile="https://www.grandmetric.com/wp-content/uploads/2018/02/Screenshot_626.png"

    if inputs['pincode']=='':
        inputs['pincode']='Not Provided'

    body={
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
            {
                "type": "TextBlock",
                "text": "Covid Support Alert",
                "weight": "Bolder",
                "size": "Large",
                "color": "Accent",
                "horizontalAlignment": "Center"
            },
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "width": "auto",
                        "items": [
                            {
                                "type": "Image",
                                "url": user_profile,
                                "size": "Small",
                                "style": "Person"
                            }
                        ]
                    },
                    {
                        "type": "Column",
                        "width": "stretch",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": user_info['displayName'],
                                "weight": "Bolder",
                                "wrap": True
                            },
                            {
                            "type": "TextBlock",
                            "spacing": "None",
                            "text": user_info['emails'][0].replace("@cisco.com",""),
                            "isSubtle": True,
                            "wrap": True
                        }
                        ]
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": '''Hi Team, {} is looking for assistance.
                Criticality : __{}__.\n'''.format(user_info['firstName'],inputs['sev']),
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "Here are the details provided:"
            },
            {
                "type": "FactSet",
                "facts": [
                    {
                        "title": "State:",
                        "value": inputs['state']
                    },
                    {
                        "title": "District:",
                        "value": inputs['city']
                    },
                    {
                        "title": "PIN Code:",
                        "value": inputs['pincode']
                    },
                    {
                        "title": "Requirement:",
                        "value": "__{}__".format(inputs['req1'])
                    }
                ],
                "separator": True
            },
            {
                "type": "TextBlock",
                "text": "Details:",
                "weight": "Bolder",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "{}".format(inputs['RequestElaborate']),
                "spacing": "Small",
                "wrap": True
            }
    
        ]
    }

    return body





def InformationRequestCard(inputs,user_info,token):
    print("I am here !!!")
    body=body_frame(inputs,user_info)
    url="https://webexapis.com/v1/messages"

    headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}

    card={
      "roomId":'Y2lzY29zcGFyazovL3VzL1JPT00vMjcwZjFjOTAtYWQ5Yi0xMWViLWEzZTAtNjU3ZWM1NjhhY2Q0',
      "markdown": "Emergency | User requested information is not available in lead DB !!!",
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
    print(send_message)
    return send_message