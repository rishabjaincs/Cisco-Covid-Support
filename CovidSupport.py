import requests
import json
import flask
from flask import request,jsonify

token=""

headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}

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
            "type": "Container"
        },
        {
            "type": "Input.ChoiceSet",
            "choices": [
                {
                    "title": "All India",
                    "value": "All India"
                },
                {
                    "title": "Karnataka",
                    "value": "Karnataka"
                },
                {
                    "title": "Delhi",
                    "value": "Delhi"
                },
                {
                    "title": "Tamil Nadu",
                    "value": "Tamil Nadu"
                },
                {
                    "title": "Maharashtra",
                    "value": "Maharashtra"
                },
                {
                    "title": "Andhra Pradesh",
                    "value": "Andhra Pradesh"
                },
                {
                    "title": "Arunachal Pradesh",
                    "value": "Arunachal Pradesh"
                },
                {
                    "title": "Assam",
                    "value": "Assam"
                },
                {
                    "title": "Bihar",
                    "value": "Bihar"
                },
                {
                    "title": "Chandigarh",
                    "value": "Chandigarh"
                },
                {
                    "title": "Chhattisgarh",
                    "value": "Chhattisgarh"
                },
                {
                    "title": "Daman and Diu",
                    "value": "Daman and Diu"
                },
                {
                    "title": "Goa",
                    "value": "Goa"
                },
                {
                    "title": "Gujarat",
                    "value": "Gujarat"
                },
                {
                    "title": "Jammu and Kashmir",
                    "value": "Jammu and Kashmir"
                },
                {
                    "title": "Puducherry",
                    "value": "Puducherry"
                },
                {
                    "title": "Haryana",
                    "value": "Haryana"
                },
                {
                    "title": "Himachal Pradesh",
                    "value": "Himachal Pradesh"
                },
                {
                    "title": "Jharkhand",
                    "value": "Jharkhand"
                },
                {
                    "title": "Kerala",
                    "value": "Kerala"
                },
                {
                    "title": "Madhya Pradesh",
                    "value": "Madhya Pradesh"
                },
                {
                    "title": "Maharashtra",
                    "value": "Maharashtra"
                },
                {
                    "title": "Manipur",
                    "value": "Manipur"
                },
                {
                    "title": "Meghalaya",
                    "value": "Meghalaya"
                },
                {
                    "title": "Mizoram",
                    "value": "Mizoram"
                },
                {
                    "title": "Nagaland",
                    "value": "Nagaland"
                },
                {
                    "title": "Odisha",
                    "value": "Odisha"
                },
                {
                    "title": "Punjab",
                    "value": "Punjab"
                },
                {
                    "title": "Rajasthan",
                    "value": "Rajasthan"
                },
                {
                    "title": "Sikkim",
                    "value": "Sikkim"
                },
                {
                    "title": "Telangana",
                    "value": "Telangana"
                },
                {
                    "title": "Sikkim",
                    "value": "Sikkim"
                },
                {
                    "title": "Tripura",
                    "value": "Tripura"
                },
                {
                    "title": "Uttar Pradesh",
                    "value": "Uttar Pradesh"
                },
                {
                    "title": "Uttarakhand",
                    "value": "Uttarakhand"
                },
                {
                    "title": "West Bengal",
                    "value": "West Bengal"
                },
                {
                    "title": "Ladakh",
                    "value": "Ladakh"
                },
                {
                    "title": "Lakshadweep",
                    "value": "Lakshadweep"
                },
                {
                    "title": "Other",
                    "value": "Other"
                }
            ],
            "placeholder": "Select the State",
            "id": "state"
        },
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "PIN Code",
                            "wrap": True,
                            "color": "Dark",
                            "weight": "Bolder",
                            "fontType": "Default",
                            "isSubtle": True
                        }
                    ],
                    "verticalContentAlignment": "Center",
                    "width": 20
                },
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "Input.Text",
                            "placeholder": "560001",
                            "id": "pincode",
                            "maxLength": 6
                        }
                    ],
                    "width": 80
                }
            ]
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.ShowCard",
                    "title": "GET Information",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": "Fill in below details to get better visibility from community",
                                "wrap": True,
                                "isSubtle": True
                            },
                            {
                                "type": "ColumnSet",
                                "columns": [
                                    {
                                        "type": "Column",
                                        "width": 100,
                                        "items": [
                                            {
                                                "type": "Input.ChoiceSet",
                                                "choices": [
                                                    {
                                                        "title": "Hospitalization (Non-ICU)",
                                                        "value": "Hospitalization (Non-ICU)"
                                                    },
                                                    {
                                                        "title": "Hospitalization (ICU)",
                                                        "value": "Hospitalization (ICU)"
                                                    },
                                                    {
                                                        "title": "Oxygen",
                                                        "value": "Oxygen"
                                                    },
                                                    {
                                                        "title": "Medicine",
                                                        "value": "Medicine"
                                                    },
                                                    {
                                                        "title": "Ambulance",
                                                        "value": "Ambulance"
                                                    },
                                                    {
                                                        "title": "Food and Bevergaes",
                                                        "value": "Food and Bevergaes"
                                                    },
                                                    {
                                                        "title": "Vaccine",
                                                        "value": "Vaccine"
                                                    },
                                                    {
                                                        "title": "Plasma",
                                                        "value": "Plasma"
                                                    }
                                                ],
                                                "placeholder": "Requirements",
                                                "id": "req1"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "TextBlock",
                                "text": "Elaborate the Details to help in coordinating better",
                                "wrap": True,
                                "spacing": "ExtraLarge",
                                "horizontalAlignment": "Center",
                                "size": "Small",
                                "color": "Light",
                                "isSubtle": True
                            },
                            {
                                "type": "Input.Text",
                                "placeholder": "Enter the details here",
                                "isMultiline": True,
                                "separator": True,
                                "id": "RequestElaborate"
                            },
                            {
                                "type": "ColumnSet",
                                "columns": [
                                    {
                                        "type": "Column",
                                        "width": 30,
                                        "items": [
                                            {
                                                "type": "TextBlock",
                                                "text": "Severity",
                                                "wrap": True,
                                                "horizontalAlignment": "Center"
                                            }
                                        ],
                                        "horizontalAlignment": "Center",
                                        "verticalContentAlignment": "Center"
                                    },
                                    {
                                        "type": "Column",
                                        "width": 70,
                                        "items": [
                                            {
                                                "type": "Input.ChoiceSet",
                                                "choices": [
                                                    {
                                                        "title": "Emergency",
                                                        "value": "Emergency"
                                                    },
                                                    {
                                                        "title": "Critical",
                                                        "value": "Critical"
                                                    },
                                                    {
                                                        "title": "Moderate",
                                                        "value": "Moderate"
                                                    }
                                                ],
                                                "placeholder": "Select Severity",
                                                "id": "sev"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "ActionSet",
                                "actions": [
                                    {
                                        "type": "Action.Submit",
                                        "title": "Search",
                                        "data":{"status":"request"}
                                    }
                                ],
                                "horizontalAlignment": "Center",
                                "spacing": "Small"
                            }
                        ]
                    }
                },
                {
                    "type": "Action.ShowCard",
                    "title": "ADD Information",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": "Fill in below details to help easy search",
                                "wrap": True,
                                "isSubtle": True
                            },
                            {
                                "type": "ColumnSet",
                                "columns": [
                                    {
                                        "type": "Column",
                                        "width": 100,
                                        "items": [
                                            {
                                                "type": "Input.ChoiceSet",
                                                "choices": [
                                                    {
                                                        "title": "Hospitalization (Non-ICU)",
                                                        "value": "Hospitalization (Non-ICU)"
                                                    },
                                                    {
                                                        "title": "Hospitalization (ICU)",
                                                        "value": "Hospitalization (ICU)"
                                                    },
                                                    {
                                                        "title": "Oxygen",
                                                        "value": "Oxygen"
                                                    },
                                                    {
                                                        "title": "Medicine",
                                                        "value": "Medicine"
                                                    },
                                                    {
                                                        "title": "Ambulance",
                                                        "value": "Ambulance"
                                                    },
                                                    {
                                                        "title": "Food and Bevergaes",
                                                        "value": "Food and Bevergaes"
                                                    },
                                                    {
                                                        "title": "Vaccine",
                                                        "value": "Vaccine"
                                                    },
                                                    {
                                                        "title": "Plasma",
                                                        "value": "Plasma"
                                                    }
                                                ],
                                                "placeholder": "Responses",
                                                "id": "res1"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "TextBlock",
                                "text": "Elaborate the resource details",
                                "wrap": True,
                                "spacing": "ExtraLarge",
                                "horizontalAlignment": "Center",
                                "size": "Small",
                                "color": "Light",
                                "isSubtle": True
                            },
                            {
                                "type": "Input.Text",
                                "placeholder": "Enter the details",
                                "isMultiline": True,
                                "separator": True,
                                "id": "resourceElaborate"
                            },
                            {
                                "type": "ColumnSet",
                                "columns": [
                                    {
                                        "type": "Column",
                                        "width": 40,
                                        "items": [
                                            {
                                                "type": "TextBlock",
                                                "text": "Contact Person",
                                                "wrap": True,
                                                "horizontalAlignment": "Center"
                                            }
                                        ],
                                        "horizontalAlignment": "Center",
                                        "verticalContentAlignment": "Center"
                                    },
                                    {
                                        "type": "Column",
                                        "width": 60,
                                        "items": [
                                            {
                                                "type": "Input.Text",
                                                "placeholder": "John A",
                                                "id": "contactname"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "ColumnSet",
                                "columns": [
                                    {
                                        "type": "Column",
                                        "width": 40,
                                        "items": [
                                            {
                                                "type": "TextBlock",
                                                "text": "Contact Information",
                                                "wrap": True,
                                                "horizontalAlignment": "Center"
                                            }
                                        ],
                                        "horizontalAlignment": "Center",
                                        "verticalContentAlignment": "Center"
                                    },
                                    {
                                        "type": "Column",
                                        "width": 60,
                                        "items": [
                                            {
                                                "type": "Input.Text",
                                                "placeholder": "9876543210",
                                                "style": "Tel",
                                                "id": "contactnumber"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "ColumnSet",
                                "columns": [
                                    {
                                        "type": "Column",
                                        "width": "stretch",
                                        "items": [
                                            {
                                                "type": "Input.Toggle",
                                                "title": "Verified",
                                                "id": "verified"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "Column",
                                        "width": "stretch",
                                        "items": [
                                            {
                                                "type": "Input.Toggle",
                                                "title": "Not Verified",
                                                "id": "notverified"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "ActionSet",
                                "actions": [
                                    {
                                        "type": "Action.Submit",
                                        "title": "Submit",
                                        "data":{"status":"insert"}
                                    }
                                ],
                                "horizontalAlignment": "Center",
                                "spacing": "Small"
                            }
                        ]
                    }
                },
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
            "horizontalAlignment": "Center"
        }
    ]
}



def startToken(userEmail):
    url="https://webexapis.com/v1/messages"

    card={
     "toPersonEmail": userEmail,
      "markdown": "Token Master Form to get the Consent Response !!",
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