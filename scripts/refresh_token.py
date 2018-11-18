import requests
from flask import session
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import json
from requests.auth import HTTPBasicAuth
def refresh_token():
    headers={"Content-Type":"application/json"}

    auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    data={
        "grant_type":"refresh_token",
        "refresh_token":session["refresh_token"],
        "redirect_uri":REDIRECT_URI
    }

    refresh_request = requests.post('https://zoom.us/oauth/token',headers=headers, params=data, auth=auth )

    data = json.loads(refresh_request.content)
    session['access_token'] = data.get('access_token')
    session['refresh_token'] = data.get('refresh_token')
