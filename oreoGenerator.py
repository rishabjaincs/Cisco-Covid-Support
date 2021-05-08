import requests
import json
import datetime
from cryptography.fernet import Fernet
import pickle
import stdiomask
import time
import schedule

def cookieGenerator():
    print("Making some oreo cookies for everyone {}".format(str(datetime.datetime.now())))
    up=open(r"coverified.key", "rb").read()
    x = Fernet(up)
    b_key = bytes(key, 'utf-8')
    decrip = x.decrypt(b_key)
    decriv=decrip.decode()
    decreep=decriv.split(":")
    req = requests.get(url='https://scripts.cisco.com/api/v2/auth/login',
                       auth=(decreep[0], decreep[1]),
                       timeout=15)
    req.raise_for_status()
    time.sleep(5)
    print(req.cookies)
    with open('oreo', 'wb') as cookie:
        pickle.dump(req.cookies, cookie)

key = stdiomask.getpass(prompt='Enter your private key:', mask="#")
cookieGenerator() 
schedule.every(6).hours.do(cookieGenerator)  

while True:
    schedule.run_pending()
    time.sleep(60)