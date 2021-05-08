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
from mongoConnector import perform_mongo_db_search
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
    ReqDetails['user_id']=user_info
    if ReqDetails['status']=='start':
        if ReqDetails['state']=='':
            message="\ud83d\udd34 **Please Select the Appropriate State !!** \ud83d\udd34"
            sendIN(token,raw_data,message)
        else:
            startToken(raw_data['data']['roomId'],raw_data['data']['messageId'],token,ReqDetails['state'])

    elif ReqDetails['status']=='request':
        # will send this request further to check if we have any data related to it available or not.
        message = "Please wait as we are processing the requested lead !!"
        sendIN(token,raw_data,message)
        if ReqDetails['state']=='':
            message="\ud83d\udd34 **Please Select the Appropriate State !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['req1']=='':
            message="\ud83d\udd34 **Please Select the Appropriate Requirement !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['sev']=='':
            message="\ud83d\udd34 **Please Select the Appropriate Criticality !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        if status==True:
            search_result=perform_mongo_db_search(ReqDetails)
            if "status" in search_result.keys():
                if search_result['status']=="danger":      
                    BuddyAssistApproval(ReqDetails,user_info,raw_data['data']['messageId'],token)
            else:
                for lead in range(0,search_result['total']):
                    del search_result["rows"][lead]["_id"]
                    message = dataFormatter(search_result["rows"][lead])
                    sendIN(token,raw_data,message)
                    LeadFeedback(raw_data['data']['roomId'],raw_data['data']['messageId'],token,search_result["rows"][lead]["leadId"])

    elif ReqDetails['status']=='insert':

        # will send this request further to check if we have any data related to it available or not.
        if ReqDetails['state']=='':
            message="\ud83d\udd34 **Please Select the Appropriate State !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['req1']=='':
            message="\ud83d\udd34 **Please Select the Appropriate Requirement !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['sev']=='':
            message="\ud83d\udd34 **Please Select the Appropriate Criticality !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['contactname']=='':
            message="\ud83d\udd34 **Please Enter the Contact Name !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['contactnumber']=='' and len(ReqDetails['contactnumber'])<10:
            message="\ud83d\udd34 **Please Enter the Contact Number !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        elif ReqDetails['verified']==ReqDetails['notverified']:
            message="\ud83d\udd34 **Please Select Either the mentioned lead is verified or not !!** \ud83d\udd34"
            status=False
            sendIN(token,raw_data,message)
        if status==True:
            search_result=perform_mongo_db_search(ReqDetails)
            if "status" in search_result.keys():
                if search_result['status']=="danger":      
                    BuddyAssistApproval(ReqDetails,user_info,raw_data['data']['messageId'],token)
            else:
                for lead in range(0,search_result['total']):
                    del search_result["rows"][lead]["_id"]
                    message=str(search_result["rows"][lead]["additionalComments"])
                    sendIN(token,raw_data,message)

    elif ReqDetails['status']=='helpful':
        message="___Thanks for your Feedback, It will help us to provide better leads !!___"
        updateIN(raw_data['data']['roomId'],raw_data['data']['messageId'],token,message)


def dataFormatter(getInfo):
    requestedLead = pd.DataFrame(getInfo)
    print(requestedLead)
    requestedLead = requestedLead[['leadType','leadState','contactName','contactNumber','additionalContacts','additionalContactNumber','additionalComments','pinCode','leadRegion','contactType','contactLocation','contactAddress']].set_index('leadType')
    return '```python\n{}'.format(tabulate(requestedLead, headers=['Lead Type','State','Contact Name','Contact Number','Additional Contact','Additional Contact Number','Additional Comments','PinCode','Region','Contact Type','Location','Address'],tablefmt="psql"))
        


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