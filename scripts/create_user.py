import requests
from flask import session
from config import CLIENT_ID, CLIENT_SECRET
import json

def create_user(info):

    params={
        "access_token":session['access_token']
    }
    headers= { 'content-type': "application/json" }

    create_response = requests.post('https://api.zoom.us/v2/users', params=params, headers=headers, data=json.dumps(info) )
    print(create_response.content)
