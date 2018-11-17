import requests
from flask import session
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import json
from requests.auth import HTTPBasicAuth

def get_zoom_token(code):
    headers={"Content-Type":"application/json"}
    auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    print(CLIENT_ID)

    data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":REDIRECT_URI
    }


    getting_token = requests.post('https://zoom.us/oauth/token',headers=headers, params=data, auth=auth )
    print (getting_token)
    print (getting_token.content)
    data = json.loads(getting_token.content)
    session['access_token'] = data.get('access_token')
    session['refresh_token'] = data.get('refresh_token')
    print (session['access_token'])
