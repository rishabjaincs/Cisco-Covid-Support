import requests
import json
import flask
from flask import request,jsonify



body={
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2",
    "body": [
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": 80,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Cisco Covid Support",
                            "wrap": True,
                            "horizontalAlignment": "Center",
                            "size": "ExtraLarge",
                            "weight": "Lighter",
                            "color": "Accent",
                            "isSubtle": True,
                            "separator": True
                        }
                    ]
                }
            ]
        },
        {
            "type": "Input.ChoiceSet",
            "choices": [{'title': 'Maharashtra', 'value': 'Maharashtra'},
 {'title': 'Delhi', 'value': 'Delhi'},
 {'title': 'Karnataka', 'value': 'Karnataka'},
 {'title': 'Gujarat', 'value': 'Gujarat'},
 {'title': 'Telangana', 'value': 'Telangana'},
 {'title': 'Tamil Nadu', 'value': 'Tamil Nadu'},
 {'title': 'West Bengal', 'value': 'West Bengal'},
 {'title': 'Rajasthan', 'value': 'Rajasthan'},
 {'title': 'Uttar Pradesh', 'value': 'Uttar Pradesh'},
 {'title': 'Bihar', 'value': 'Bihar'},
 {'title': 'Madhya Pradesh', 'value': 'Madhya Pradesh'},
 {'title': 'Andhra Pradesh', 'value': 'Andhra Pradesh'},
 {'title': 'Punjab', 'value': 'Punjab'},
 {'title': 'Haryana', 'value': 'Haryana'},
 {'title': 'Jammu and Kashmir', 'value': 'Jammu and Kashmir'},
 {'title': 'Jharkhand', 'value': 'Jharkhand'},
 {'title': 'Chhattisgarh', 'value': 'Chhattisgarh'},
 {'title': 'Assam', 'value': 'Assam'},
 {'title': 'Chandigarh', 'value': 'Chandigarh'},
 {'title': 'Odisha', 'value': 'Odisha'},
 {'title': 'Kerala', 'value': 'Kerala'},
 {'title': 'Uttarakhand', 'value': 'Uttarakhand'},
 {'title': 'Puducherry', 'value': 'Puducherry'},
 {'title': 'Tripura', 'value': 'Tripura'},
 {'title': 'Mizoram', 'value': 'Mizoram'},
 {'title': 'Meghalaya', 'value': 'Meghalaya'},
 {'title': 'Manipur', 'value': 'Manipur'},
 {'title': 'Himachal Pradesh', 'value': 'Himachal Pradesh'},
 {'title': 'Nagaland', 'value': 'Nagaland'},
 {'title': 'Goa', 'value': 'Goa'},
 {'title': 'Andaman and Nicobar Islands',
  'value': 'Andaman and Nicobar Islands'},
 {'title': 'Arunachal Pradesh', 'value': 'Arunachal Pradesh'},
 {'title': 'Dadra and Nagar Haveli', 'value': 'Dadra and Nagar Haveli'}],
            "placeholder": "Select the State",
            "id": "state"
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "Proceed",
                    "style": "positive",
                    "data":{
                      "status":"start",
                  }
                }
            ],
            "horizontalAlignment": "Center"
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.ShowCard",
                    "title": "Help Links",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": "Global Support",
                                "wrap": True
                            },
                            {
                                "type": "ActionSet",
                                "actions": [
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "Global",
                                        "url": "https://www.who.int/emergencies/diseases/novel-coronavirus-2019"
                                    },
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "India",
                                        "url": "https://www.covid19india.org/"
                                    },
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "Vaccination",
                                        "url": "https://www.cowin.gov.in/home"
                                    },
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "Covid Help",
                                        "url": "https://www.mohfw.gov.in/"
                                    }
                                ],
                                "horizontalAlignment": "Center",
                                "spacing": "Small"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Cisco Support",
                                "wrap": True
                            },
                            {
                                "type": "ActionSet",
                                "actions": [
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "Quarantine",
                                        "url": "https://cisco.sharepoint.com/:w:/r/sites/PeopleCommunities-India/Cisco%20Wellbeing/India%20COVID-19%20Pandemic%20Support/Quarantine%20%26%20Isolation%20Support%20Resources/Hotel%20Quarantine%20Facility%20with%20Apollo%20Hospitals.docx?d=w11a744e1ca304ff7aa6958f4103166fe&csf=1&web=1&e=IiVlHM&CT=1620075127294&OR=Outlook-Body&CID=A299CC6E-F5FF-4714-9FC5-C625413BC067&wdLOR=c1FA74577-8D35-44BE-B482-ACDBB8F3144A"
                                    },
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "Home Care",
                                        "url": "https://cisco.sharepoint.com/sites/PeopleCommunities-India/Cisco%20Wellbeing/Forms/AllItems.aspx?id=%2Fsites%2FPeopleCommunities%2DIndia%2FCisco%20Wellbeing%2FIndia%20COVID%2D19%20Pandemic%20Support%2FPreventive%20Support%20Resources%2FVaccination%20Support%20Service%2Epdf&parent=%2Fsites%2FPeopleCommunities%2DIndia%2FCisco%20Wellbeing%2FIndia%20COVID%2D19%20Pandemic%20Support%2FPreventive%20Support%20Resources"
                                    },
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "Financial Assistance",
                                        "url": "https://cisco.sharepoint.com/:b:/r/sites/PeopleCommunities-India/Cisco%20Wellbeing/India%20COVID-19%20Pandemic%20Support/Additional%20Resources/FINANCIAL%20ASSISTANCE%20DURING%20COVID-19.pdf?csf=1&web=1&e=MMFhWx&CT=1620075207211&OR=Outlook-Body&CID=B4E099DD-D56E-4DB8-B58B-96A5EFBC215E&wdLOR=c86541D13-65FF-4859-8EC0-270C084D92D5"
                                    },
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "Covid Exposure",
                                        "url": "https://app.smartsheet.com/b/form/f45a0d6dc34e4e328fcd0d85b0a9de34"
                                    },
                                    {
                                        "type": "Action.OpenUrl",
                                        "title": "Pandemic Planning Site",
                                        "url": "https://cisco.sharepoint.com/sites/PeopleCommunities-India/SitePages/India-COVID-Pandemic-Support.aspx"
                                    }
                                ],
                                "horizontalAlignment": "Center",
                                "spacing": "Small"
                            }
                        ]
                    }
                }
            ],
            "horizontalAlignment": "Center",
            "separator": True
        }
    ]
}


def gettingStarted(userEmail,token):
    url="https://webexapis.com/v1/messages"

    headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}

    card={
     "toPersonEmail": userEmail,
      "markdown": "Cicso Covid Support, Needs more detail !!",
      "attachments": [
        {
          "contentType": "application/vnd.microsoft.card.adaptive",
          "content": body
        }
      ]
    }

    payload=json.dumps(card)
    response = requests.request("POST", url, data=payload, headers=headers)
    # send_message=response.json()
    return response.status_code
