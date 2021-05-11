import requests
import json
import flask
from flask import request,jsonify
from CovidSupport import startToken
from sender import send_message as sendIN
from sender import direct_message as sendOUT
from sender import delete_message as deleteIN
from sender import updateMessage as updateIN
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

def get_requester_detail(user_id):
    url="https://webexapis.com/v1/people/{}".format(user_id)
    response=requests.request("GET", url, headers=headers)
    profileDetail=response.json()
    return profileDetail

def UserValidator(raw_data):
    if raw_data['data']['roomType']=='direct' and raw_data['data']["personEmail"]!="covid_support@webex.bot":
        gettingStarted(raw_data['data']['personEmail'],token)
        

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

        elif " " not in ReqDetails['contactname']:
            message="\ud83e\udd16 : Please provide Full Contact Name, Eg: John A !! !!"
            status=False
            sendIN(token,raw_data,message)

        elif " " not in ReqDetails['contactnamesecondary'] and ReqDetails['contactnamesecondary']!="":
            message="\ud83e\udd16 : Please provide Full Contact Name, Eg: John A !!"
            status=False
            sendIN(token,raw_data,message)

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
    if raw_data['data']['roomType']=='direct' and raw_data['data']["personEmail"]!="covid_support@webex.bot":
        message = '''__Disclaimer :__ This BOT is a best effort project initiated to help user to check and contribute from the Public Information Database that can help in the recent Covid Crisis.
        To continue, Please type anything and BOT will assist you further'''
        sendOUT(token,raw_data,message)



def FurtherAssistanceNeeded(raw_data):
    ReqDetails=raw_data['data']['inputs']
    user_info=get_requester_detail(raw_data['data']['personId'])
    if ReqDetails['access']==True:
        deleteIN(token,raw_data)
        message="Your request has been processed !!!"
        non_urgent_message_chain(token,raw_data,message,ReqDetails['parentId'])
        InformationRequestCard(ReqDetails,user_info,token)
    else:
        deleteIN(token,raw_data)
        print("send it over to DB by default")