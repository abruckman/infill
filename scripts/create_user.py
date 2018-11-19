import requests
from flask import session
from config import CLIENT_ID, CLIENT_SECRET
import json
from scripts import refresh_token

def create_user(info):

    params={
        "access_token":session['access_token']

    }
    headers= { 'content-type': "application/json" }

    create_response = requests.post('https://api.zoom.us/v2/users', params=params, headers=headers, data=json.dumps(info) )
    status = create_response.status_code
    content = json.loads(create_response.content)


    result = dict()
    result['email']= info['user_info']['email']
    result['message']= ''
    if 'email' in content:
        result['success']= 'success'
    elif status == 401:
        refresh_token.refresh_token()
        result = create_user(info)
    else:
        message = content.get('message')
        if message == "Validation Failed.":
            result['success'] = "Field Invalid"
            for error in content['errors']:
                result['message'] += (error['field'])
        elif message == "Invalid api key or secret.":
            result['success'] = "Invalid login"
            result['message'] += '<a href="/get_token">Log in Again</a>'
        elif "User already in the account" in message:
            result['success'] = "Failed"
            result['message'] = message
        elif message == 'No privilege.':
            result['success'] = "Failed"
            result['message'] = 'ensure that your account has <a href="https://zoom.us/account/user">capability to add users</a>. You may have to enter your credit card.'
        else:
            ressult['message']= message
            result['success'] = "Failed"
    return result
