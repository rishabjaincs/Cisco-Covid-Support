import requests
import json
import flask
from flask import request,jsonify
from CovidSupport import startToken
from sender import send_message as sendIN
from sender import direct_message as sendOUT
from sender import delete_message as deleteIN
from CovidBuddy import InformationRequestCard
from UserConsentCard import BuddyAssistApproval
from sender import non_urgent_message_chain
import stdiomask

# token=stdiomask.getpass(prompt='Enter the Access Token:', mask="*") 
token=""


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
        startToken(raw_data['data']['personEmail'])
        


def AttachmentValidator(raw_data):
    status=True
    ReqDetails=raw_data['data']['inputs']
    user_info=get_requester_detail(raw_data['data']['personId'])
    if ReqDetails['status']=='request':
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
        if status==True:
            search_result={}
            if bool(search_result)==False:      
                BuddyAssistApproval(ReqDetails,user_info,raw_data['data']['messageId'])
            else:
                print("Share search result")

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
        InformationRequestCard(ReqDetails,user_info)
    else:
        deleteIN(token,raw_data)
        print("send it over to DB by default")