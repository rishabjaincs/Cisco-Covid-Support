import requests
import json



def directMessage(parentId,roomId,message):
    payload={
     "parentId":parentId,
     "roomId": roomId,
      "markdown": message
    }
    return payload

def direct_personalEmail(token,personalEmail,message):
    url="https://webexapis.com/v1/messages"
    payload={
     "toPersonEmail": personalEmail,
      "markdown": message
    }

    headers={
      'content-type': "application/json; charset=utf-8",
      'authorization':"Bearer "+token,
      'accept':"application/json"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    print(response.content)
    print("Here's the message status:")
    print(response.status_code)  

def send_message(token,raw_data,message):
    url="https://webexapis.com/v1/messages"
    payload=json.dumps(directMessage(raw_data['data']['messageId'],raw_data['data']['roomId'],message))

    headers={
      'content-type': "application/json; charset=utf-8",
      'authorization':"Bearer "+token,
      'accept':"application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.content)
    print("Here's the message status:")
    print(response.status_code)


def delete_message(token,raw_data):
    headers={
      'content-type': "application/json; charset=utf-8",
      'authorization':"Bearer "+token,
      'accept':"application/json"
    }
    url="https://webexapis.com/v1/messages/{}".format(raw_data['data']['messageId'])
    response = requests.request("DELETE", url, headers=headers)
    if response.status_code==204:
        print('Successfully Deleted !!')
    else:
        print("========================================================================================")
        print('Error Detected !!')
        print(response.json())
        print("========================================================================================")


def direct_message(token,raw_data,message):
    url="https://webexapis.com/v1/messages"
    payload={
     "roomId": raw_data['data']['roomId'],
      "markdown": message
    }

    headers={
      'content-type': "application/json; charset=utf-8",
      'authorization':"Bearer "+token,
      'accept':"application/json"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    print(response.content)
    print("Here's the message status:")
    print(response.status_code)  


def non_urgent_message_chain(token,raw_data,message,parentId):
    url="https://webexapis.com/v1/messages"
    payload=json.dumps(directMessage(parentId,raw_data['data']['roomId'],message))

    headers={
      'content-type': "application/json; charset=utf-8",
      'authorization':"Bearer "+token,
      'accept':"application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.content)
    print("Here's the message status:")
    print(response.status_code)

def updateMessage(roomId,parentId,token,message):
    url="https://webexapis.com/v1/messages/{}".format(parentId)

    headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}

    card={
     "roomId": roomId,
      "markdown": message,
    }


    payload=json.dumps(card)
    response = requests.request("PUT", url, data=payload, headers=headers)
    # send_message=response.json()
    return response.status_code