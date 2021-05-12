import requests
import json
import flask
from flask import request,jsonify
from CovidSupport import startToken
from sender import send_message as sendIN
from sender import direct_message as sendOUT
from sender import delete_message as deleteIN
from sender import updateMessage as updateIN
from sender import direct_personalEmail as personalOUT
from CovidBuddy import InformationRequestCard
from UserConsentCard import BuddyAssistApproval
from LeadFeedbackCollector import LeadFeedback
from CovidHelp import gettingStarted
from sender import non_urgent_message_chain
from mongoConnector import perform_mongo_db_search,compiling_data_insert,compiling_data_vote
import stdiomask
import pandas as pd
from tabulate import tabulate

token=stdiomask.getpass(prompt='Enter the Access Token:', mask="*") 


#This is a global header declared that will be used by all the API calls
headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}

def get_mention_id(person_id):
    url="https://webexapis.com/v1/people/{}".format(person_id)

    headers={
      'content-type': "application/json; charset=utf-8",
      'authorization':"Bearer "+token,
      'accept':"application/json"
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()['emails'][0]
    print("Here's the message statue")
    print(response.status_code)

def message_details(message_ID):
    headers = {
        'content-type': "application/json; charset=utf-8",
        'authorization': "Bearer " + token,
        'accept': "application/json"
    }
    messageID="https://webexapis.com/v1/messages/{}".format(message_ID)
    response = requests.request("GET", messageID, headers=headers)
    data=response.json()
    return data['mentionedPeople']

def get_requester_detail(user_id):
    url="https://webexapis.com/v1/people/{}".format(user_id)
    response=requests.request("GET", url, headers=headers)
    profileDetail=response.json()
    return profileDetail




def UserValidator(raw_data):
    if raw_data['data']['roomType']=='direct' and raw_data['data']["personEmail"]!="coverified@webex.bot":
        gettingStarted(raw_data['data']['personEmail'],token)
    else:
        if raw_data['data']['roomType']=='group' and ((raw_data['data']['markdown']).lower()).startswith("coverified support"):
            mentionedIDs = message_details(raw_data['data']['id'])
            if len(mentionedIDs)>1:
                for person_id in mentionedIDs[1:]:
                    message = '''__Disclaimer :__ _This BOT is a best effort project initiated to help user to check and contribute from the Public Information Database that can help in the recent Covid Crisis._
        <br> __To continue__, Please type __help__ and BOT \ud83e\udd16 will assist you further.'''
                    personalEmail=get_mention_id(person_id)
                    print("The user mentioned :")
                    print(personalEmail)
                    personalOUT(token,personalEmail,message)
                
            else:
                cecIDs=(((raw_data['data']['markdown']).lower()).replace("coverified support","")).split(" ")
                for cec in cecIDs:
                    print("The user mentioned :")
                    print(cec)
                    personalEmail=(cec.replace(" ",""))+"@cisco.com"
                    message = '''__Disclaimer :__ _This BOT is a best effort project initiated to help user to check and contribute from the Public Information Database that can help in the recent Covid Crisis._
            <br> __To continue__, Please type __help__ and BOT \ud83e\udd16 will assist you further.'''
                    personalOUT(token,personalEmail,message)




def AttachmentValidator(raw_data):
    status=True
    ReqDetails=raw_data['data']['inputs']
    user_info=get_requester_detail(raw_data['data']['personId'])
    ReqDetails['user_id']=user_info['emails'][0].replace("@cisco.com","")
    userDisplayName = user_info['firstName']
    if ReqDetails['status']=='start':
        if ReqDetails['state']=='':
            message="\ud83e\udd16 : Please Select the Appropriate State !!"
            sendIN(token,raw_data,message)
        else:
            startToken(raw_data['data']['roomId'],raw_data['data']['messageId'],token,ReqDetails['state'])

    elif ReqDetails['status']=='request':
        # will send this request further to check if we have any data related to it available or not.
        message = "\ud83e\udd16 : Please wait while we are processing the requested lead under 100 KM radius !!"
        sendIN(token,raw_data,message)
        if ReqDetails['state']=='':
            message="\ud83e\udd16 : Please Select the Appropriate State !!"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['req1']=='':
            message="\ud83e\udd16 : Please Select the Appropriate Requirement !!"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['sev']=='':
            message="\ud83e\udd16 : Please Select the Appropriate Criticality !!"
            status=False
            sendIN(token,raw_data,message)
        if status==True:
            search_result=perform_mongo_db_search(ReqDetails)
            if search_result['total']== 0: 
                BuddyAssistApproval(ReqDetails,user_info,raw_data['data']['messageId'],token)
            else:
                for lead in range(0,search_result['total']):
                    # del search_result["rows"][lead]["_id"]
                    # message = dataFormatter(search_result["rows"][lead])
                    # sendIN(token,raw_data,message)
                    LeadFeedback(raw_data['data']['roomId'],raw_data['data']['messageId'],token,search_result["rows"][lead])

    elif ReqDetails['status']=='insert':

        # will send this request further to check if we have any data related to it available or not.
        if ReqDetails['state']=='':
            message="\ud83e\udd16 : Please Select the Appropriate State !!"
            status=False
            sendIN(token,raw_data,message)

        elif ReqDetails['city']=='':
            message="\ud83e\udd16 : Please Select the Appropriate City !!"
            status=False
            sendIN(token,raw_data,message)

        elif ReqDetails['res1']=='':
            message="\ud83e\udd16 : Please Select the Appropriate Response !!"
            status=False
            sendIN(token,raw_data,message)
        
        elif ReqDetails['contactname']=='':
            message="\ud83e\udd16 : Please enter the Primary Contact Name !!"
            status=False
            sendIN(token,raw_data,message)

        elif ReqDetails['contactname']==ReqDetails['contactnamesecondary']:
            message="\ud83e\udd16 : Primary and Secondary contact names cannot be same !!"
            status=False
            sendIN(token,raw_data,message)

        # elif " " not in ReqDetails['contactname']:
        #     message="\ud83e\udd16 : Please provide Full Contact Name, Eg: John A !! !!"
        #     status=False
        #     sendIN(token,raw_data,message)

        # elif " " not in ReqDetails['contactnamesecondary'] and ReqDetails['contactnamesecondary']!="":
        #     message="\ud83e\udd16 : Please provide Full Contact Name, Eg: John A !!"
        #     status=False
        #     sendIN(token,raw_data,message)

        elif ReqDetails['contactnumber']=='' or len(ReqDetails['contactnumber'])!=10:
            message="\ud83e\udd16 : Please Enter the correct Primary Contact Number !!"
            status=False
            sendIN(token,raw_data,message)  

        elif ReqDetails['contactnumbersecondary']!='' and len(ReqDetails['contactnumbersecondary'])!=10:
            message="\ud83e\udd16 : Please Enter the correct Secondary Contact Number !!"
            status=False
            sendIN(token,raw_data,message)

        elif ReqDetails['contactnumber']==ReqDetails['contactnumbersecondary']:
            message="\ud83e\udd16 : Primary and Secondary Contact Number cannot be same !!"
            status=False
            sendIN(token,raw_data,message)

        elif ReqDetails['verified']=='false':
            message="\ud83e\udd16 : We currently does not support unverified lead !!"
            status=False
            sendIN(token,raw_data,message)

        if status==True:
            result=compiling_data_insert(ReqDetails)
            if result['status']=='success':
                if "Successfully added" in result['description']:
                    message="___Thanks {} for providing the lead, This will help multiple peers in need !!___".format(userDisplayName)
                    status=False
                    sendIN(token,raw_data,message)
            elif result['status']=='danger':
                if "Duplicate values detected" in result['description']:
                    message="___Thanks {} for your support, but seems like the same lead has been already captured !!___".format(userDisplayName)
                    status=False
                    sendIN(token,raw_data,message)
                elif "Bad data submitted for creation" in result['description']:
                    message="\ud83e\udd16 : Provided lead seems to have incorrect Information like __Numbers in Contact Name__ or __Characters in Contact Number__ !!"
                    status=False
                    sendIN(token,raw_data,message)



    elif ReqDetails['status']=='helpful':
        compiling_data_vote(ReqDetails)
        message="___Thanks {} for your Feedback, It will help us to provide better leads !!___".format(userDisplayName)
        updateIN(raw_data['data']['roomId'],raw_data['data']['messageId'],token,message)

    print(ReqDetails)

# def dataFormatter(getInfo):
#     requestedLead = pd.DataFrame(getInfo)
#     print(requestedLead)
#     requestedLead = requestedLead[['leadType','leadState','contactName','contactNumber','additionalContacts','additionalContactNumber','additionalComments','pinCode','leadRegion','contactType','contactLocation','contactAddress']].set_index('leadType')
#     return '```python\n{}'.format(tabulate(requestedLead, headers=['Lead Type','State','Contact Name','Contact Number','Additional Contact','Additional Contact Number','Additional Comments','PinCode','Region','Contact Type','Location','Address'],tablefmt="psql"))
        


def DisclaimerInfo(raw_data):
    if raw_data['event']=='created':
        if raw_data['data']['personEmail']=='coverified@webex.bot' and raw_data['data']['roomType']=='group':
            message = '''Hi There, I am here to assist you to find and share leads and to get information that can help you to track Covid Related Resources.
            __Disclaimer :__ _This BOT \ud83e\udd16 is a best effort project initiated to help user to check and contribute from the Public Information Database that our volunteers are continuously adding and verifying everyday._
            <br>`Here are the things that I can do:`<br>
            <h3>In a Group:</h3>
            ___@Coverified___ support ___@Mention User___ or ___CCID___<br>
            __Example:__ @Coverified support rajatag esramasa rishabj
            __Example:__ @Coverified support @Rajat @Eswaramoorthy @Rishab<br>
            __Note:__ _Current Version supports multiple CCID or Mentions but not a mix of both !!!_<br>
            <h3>Direct:</h3>
            Please type __help__ and The BOT \ud83e\udd16 will assist you further.'''

            sendOUT(token,raw_data,message)

        elif raw_data['data']['personEmail']!='coverified@webex.bot' and raw_data['data']['roomType']=='group':
            message='''Hi {}, I am Coverified BOT \ud83e\udd16. I can assist you in searching lead for your near and dear, all across India. You can also share new leads via ADD Information Section.
            <br> __To continue__, Please type __help__ and I \ud83e\udd16 will assist you further.'''.format((raw_data['data']['personDisplayName']).split(" ")[0])
            personalOUT(token,raw_data['data']['personEmail'],message)



def FurtherAssistanceNeeded(raw_data):
    ReqDetails=raw_data['data']['inputs']
    user_info=get_requester_detail(raw_data['data']['personId'])
    ReqDetails['user_id']=user_info['emails'][0].replace("@cisco.com","")
    userDisplayName = user_info['firstName']
    if ReqDetails['access']==False:
        # deleteIN(token,raw_data)
        # message="Your request has been processed !!!"
        # non_urgent_message_chain(token,raw_data,message,ReqDetails['parentId'])
        if ReqDetails['sev']=='Emergency':
            InformationRequestCard(ReqDetails,user_info,token)
        message="___Hi {}, We are trying to add more leads everyday. If you have any helpful lead for any resource, consider sharing via ADD Information !!___".format(userDisplayName)
        updateIN(raw_data['data']['roomId'],raw_data['data']['messageId'],token,message)

    else:
        deleteIN(token,raw_data)
        print("send it over to DB by default")