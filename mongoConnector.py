from pprint import pprint
import requests
import json


def perform_mongo_db_insert(input_json, resource, action):
    access_token = get_bdb_token()

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
    api_endpoint = "https://scripts.cisco.com/api/v2/jobs/coverified_backend"
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer {}'.format(access_token)}
    r = requests.post(url=api_endpoint, data=json.dumps(json_payload), headers=headers)
    pprint(r.text)
    server_response = json.loads(r.text)
    response_array = server_response["data"]["variables"]["_0"]["json_out"]
    response_array_json = json.loads(response_array)
    return response_array_json["description"]


def perform_mongo_db_search(input_json):
    access_token = get_bdb_token()
    input_status = input_json["status"]
    response_array_json = None
    if input_status == "request":
        help_type = input_json["req1"]
        state = input_json["state"]
        city = input_json["city"]
        contact_name = input_json["contactname"]
        contact_number = input_json["contactnumber"]
        # pincode = input_json["pincode"]
        # request_elaborate = input_json["RequestElaborate"]
        # sev = input_json["sev"]


        insert_json = {
            "helpType": help_type,
            "helpCity": city,
            "helpState": state,
            "contactName": contact_name,
            "contactNumber": contact_number
            # "pinCode":pincode,
            # "requestComments":request_elaborate,
            # "severity":sev
        }
        # res = perform_mongo_db_insert(insert_json, "help", "post_quick")
        # pprint(res)
        nearby_cities = get_nearby_cities(city, state)
        if len(nearby_cities) == 0:
            nearby_cities.append(city)
        input_json = {
            "query": {"leadState": state, "leadType": help_type, "leadCity": { "$in": nearby_cities}},
            "limit": 0,
            "skip": 0
        }

        json_payload = {
            "input": {
                "payload": {
                    "resource": "leads",
                    "verb": "get",
                    "params": input_json
                }},

        }
        api_endpoint = "https://scripts.cisco.com/api/v2/jobs/coverified_backend"
        headers = {'Content-type': 'application/json', 'Authorization': 'Bearer {}'.format(access_token)}
        r = requests.post(url=api_endpoint, data=json.dumps(json_payload), headers=headers)
        server_response = json.loads(r.text)
        # print(server_response)
        response_array = server_response["data"]["variables"]["_0"]["json_out"]
        response_array_json = json.loads(response_array)

    return response_array_json


def get_bdb_token():
    r = requests.get('https://scripts.cisco.com/api/v2/auth/login', auth=("",""))
    print(r.headers["access_token"])
    return r.headers["access_token"]


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
        nearby_cities_array.append(x[0].replace(" Sub-District", ""))
    pprint(nearby_cities_array)
    return nearby_cities_array


def insert_lead(input_json):
    insert_json = {
        "helpType": input_json["res1"],
        "helpCity": input_json["city"],
        "helpState": input_json["state"],
        "contactName": input_json["contactname"],
        "contactNumber": input_json["contactnumber"]
    }
    return perform_mongo_db_insert(insert_json, "leads", "post_quick")

perform_mongo_db_search({'state': 'Rajasthan', 'status': 'request', 'city': 'Jaipur', 'req1': 'Hospitalization (ICU)', 'RequestElaborate': 'Need Help', 'sev': 'Emergency', 'res1': '', 'resourceElaborate': '', 'pincode': '302019', 'contactname': '', 'contactnumber': '', 'verified': 'false', 'notverified': 'false'})