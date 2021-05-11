import requests
import json
import flask
from flask import request,jsonify
import datetime

def epochTimeCoverter(epochTime:int):
    convertedTime = datetime.datetime.fromtimestamp(epochTime//1000).strftime('%Y-%m-%d %H:%M:%S')
    return convertedTime

def body_frame(leadInfo):
    body={
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2",
    "body": [
        {
                "type": "TextBlock",
                "text": "Lead for {}".format(leadInfo["leadType"]),
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "FactSet",
                "facts": [
                    {
                        "title": "Contact Name",
                        "value": leadInfo["contactName"]
                    },
                    {
                        "title": "Contact Number",
                        "value": "[{}](tel:{})".format(leadInfo["contactNumber"],leadInfo["contactNumber"])
                    },
                    {
                        "title": "Sec. Contact",
                        "value": leadInfo["additionalContacts"]
                    },
                    {
                        "title": "Sec. Number",
                        "value": "[{}](tel:{})".format(leadInfo["additionalContactNumber"],leadInfo["additionalContactNumber"])
                    },
                    {
                        "title": "Last Update",
                        "value": "{} ({})".format("Verified & Available",leadInfo["lastUpdateBy"])
                    },
                    {
                        "title": "Timeline",
                        "value": "{}".format(epochTimeCoverter(leadInfo["verifiedAndStckAvlbleOn"]["$date"]))
                    }
                ]
            },
            {
                "type": "ActionSet",
                "actions": [
                    {
                        "type": "Action.Submit",
                        "title": "Worked",
                        "data": {
                            "status": "helpful",
                            "leadStatus": "worked",
                            "leadId": leadInfo["leadId"]
                        },
                        "style": "positive"
                    },
                    {
                        "type": "Action.Submit",
                        "title": "Resource Not Available",
                        "data": {
                            "status": "helpful",
                            "leadStatus": "resource-not-available",
                            "leadId": leadInfo["leadId"]
                        },
                        "style": "destructive"
                    },
                    {
                        "type": "Action.Submit",
                        "title": "Not Reachable",
                        "data": {
                            "status": "helpful",
                            "leadStatus": "not-reachable",
                            "leadId": leadInfo["leadId"]
                        },
                        "style": "destructive"
                    },
                    {
                        "type": "Action.Submit",
                        "title": "Incorrect Contact Information",
                        "data": {
                            "status": "helpful",
                            "leadStatus": "incorrect-contact",
                            "leadId": leadInfo["leadId"]
                        },
                        "style": "destructive"
                    }
                ],
                "id": "Spam",
                "horizontalAlignment": "Center"
            }
            # ,
        # {
        #     "type": "TextBlock",
        #     "text": "Does the above Lead Helped ?",
        #     "wrap": True,
        #     "size": "Medium",
        #     "weight": "Lighter",
        #     "color": "Accent",
        #     "isSubtle": True
        # },
        # {
        #     "type": "ActionSet",
        #     "actions": [
        #         {
        #             "type": "Action.Submit",
        #             "title": "YES",
        #             "style": "positive",
        #             "data": {
        #                 "status": "helpful",
        #                 "data": True,
        #                 "leadId":leadInfo["leadId"]
        #             }
        #         },
        #         {
        #             "type": "Action.Submit",
        #             "title": "Out Of Stock",
        #             "style": "destructive",
        #             "data": {
        #                 "status": "helpful",
        #                 "data": None,
        #                 "leadId":leadInfo["leadId"]
        #             }
        #         },
        #         {
        #             "type": "Action.Submit",
        #             "title": "NO",
        #             "style": "destructive",
        #             "data": {
        #                 "status": "helpful",
        #                 "data": False,
        #                 "leadId":leadInfo["leadId"]
        #             }
        #         }
        #     ],
        #     "horizontalAlignment": "Center"
        # }
    ]
}
    return body


def LeadFeedback(roomId,parentId,token,leadInfo):
    url="https://webexapis.com/v1/messages/"

    headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}

    body=body_frame(leadInfo)

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

