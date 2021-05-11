from pprint import pprint
import requests
import json
import pickle


def perform_mongo_db_insert(input_json, resource, action):
    json_payload = {
        "printLogs": True,
        "dev": True,
        "input": {
            "payload": {
                "resource": resource,
                "verb": action,
                "params": input_json
            }},
    }
    r = requests.post('https://scripts.cisco.com/api/v2/jobs/coverified_backend',
                            data=json.dumps(json_payload),
                            cookies=get_sso_cookie(),
                            headers={'Content-Type': 'application/json'})
    pprint(r.text)
    server_response = json.loads(r.text)
    print(server_response)
    response_array = server_response["data"]["variables"]["_0"]["json_out"]
    response_array_json = json.loads(response_array)
    return response_array_json["description"]

def compiling_data_insert(input_json):
    input_status = input_json["status"]
    response_array_json = None
    if input_status == "insert":
        help_type = input_json["res1"]
        state = input_json["state"]
        city = input_json["city"]
        contact_name = input_json["contactname"]
        contact_number = input_json["contactnumber"]
        contact_name_secondary = input_json["contactnamesecondary"]
        contact_number_secondary = input_json["contactnumbersecondary"]
        pin_code = input_json["pincode"]
        request_comments = input_json["resourceElaborate"]
        user_id = input_json["user_id"]


        insert_json = {
            "leadType": help_type,
            "leadCity": city,
            "leadState": state,
            "contactName": contact_name,
            "contactNumber": contact_number,
            "additionalContacts":contact_name_secondary,
            "additionalContactNumber":contact_number_secondary,
            "pinCode": pin_code,
            "additionalComments": request_comments,
            "userId": user_id
        }
        
        json_payload = {
            "printLogs": True,
            "dev": True,
            "input": {
                "payload": {
                    "resource": "leads",
                    "verb": "post_quick",
                    "params": insert_json,
                    "test" : True
                }},
        }
        r = requests.post('https://scripts.cisco.com/api/v2/jobs/coverified_backend',
                                data=json.dumps(json_payload),
                                cookies=get_sso_cookie(),
                                headers={'Content-Type': 'application/json'})
        pprint(r.text)
        server_response = json.loads(r.text)
        print(server_response)
        response_array = server_response["data"]["variables"]["_0"]["json_out"]
        response_array_json = json.loads(response_array)
        return response_array_json["description"]

def perform_mongo_db_search(input_json):
    input_status = input_json["status"]
    response_array_json = None
    if input_status == "request":
        help_type = input_json["req1"]
        state = input_json["state"]
        city = input_json["city"]
        contact_name = input_json["contactname"]
        contact_number = input_json["contactnumber"]
        pin_code = input_json["pincode"]
        request_comments = input_json["RequestElaborate"]
        severity = input_json["sev"]
        user_id = input_json["user_id"]

        insert_json = {
            "helpType": help_type,
            "helpCity": city,
            "helpState": state,
            "contactName": contact_name,
            "contactNumber": contact_number,
            "pinCode": pin_code,
            "requestComments": request_comments,
            "severity": severity,
            "userId": user_id
        }
        res = perform_mongo_db_insert(insert_json, "help", "post_quick")
        pprint(res)
        nearby_cities = get_nearby_cities(city, state)
        if len(nearby_cities) == 0:
            nearby_cities.append(city)
        input_json = {
            "query": {"leadState": state, "leadType": help_type, "leadCity": {"$in": nearby_cities}},
            "limit": 0,
            "skip": 0
        }

        json_payload = {
            "input": {
                "payload": {
                    "test":True,
                    "resource": "leads",
                    "verb": "get",
                    "params": input_json
                }},

        }
        print(json_payload)
        req = requests.post('https://scripts.cisco.com/api/v2/jobs/coverified_backend',
                            data=json.dumps(json_payload),
                            cookies=get_sso_cookie(),
                            headers={'Content-Type': 'application/json'})
        server_response = json.loads(req.text)
        print(server_response)
        response_array = server_response["data"]["variables"]["_0"]["json_out"]
        response_array_json = json.loads(response_array)

    return response_array_json


def get_sso_cookie():
    with open('oreo', 'rb') as cookie:
        return pickle.load(cookie)

def get_nearby_cities(city, state):
    r = requests.get('http://10.105.217.238:30400/api/v1/getNearbyCities?rangeInKilometer=50&country=IND&searchText='
                     + city + " " + state)
    response_json = json.loads(r.text)
    description = response_json["status_description"]
    if description == "Invalid SearchText!":
        return []
    nearby_cities = response_json["result"]
    nearby_cities_array = [city]
    for x in nearby_cities:
        nearby_cities_array.append(x.replace(" Sub-District", ""))
    pprint(nearby_cities_array)
    return nearby_cities_array


def insert_lead(input_json):
    insert_json = {
        "leadType": input_json["res1"],
        "leadCity": input_json["city"],
        "leadState": input_json["state"],
        "contactName": input_json["contactname"],
        "contactNumber": input_json["contactnumber"],
        "pinCode": input_json["pinCode"],
        "userId": input_json["user_id"],
    }
    return perform_mongo_db_insert(insert_json, "leads", "post_quick")
