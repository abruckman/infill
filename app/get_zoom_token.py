import requests
from flask import session
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def get_zoom_token(code):
    headers={"Content-Type":"application/json"}

    auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":REDIRECT_URI
    }


    getting_token = requests.post('https://zoom.us/oauth/token',headers=headers, params=data, auth=auth )

    print (getting_token.content)
    session['access_token'] = getting_token.contet['access_token']
    session['refresh_token'] = getting_token.content['refresh_token']
    print (session['access_token'])
