from flask import render_template, redirect, request, session
from app import app
from scripts import get_zoom_token
from scripts.create_user import create_user
from scripts.dictify_csv import dictify_csv
from config import CLIENT_ID, REDIRECT_URI
from app.forms import FileForm
import csv

@app.route('/')
@app.route('/index')
def index():
    form = FileForm()
    if session.get('access_token'):
        authorized = True
    else:
        authorized = False
    print('hits index')
    return render_template('index.html', authorized=authorized, form=form)

@app.route('/get_token')
def get_token():
    redirect_url = "https://zoom.us/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}"
    redirect_url = redirect_url.format(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI)
    return redirect(redirect_url)

@app.route('/oauth_return')
def oauth_return():
    print(request.args)
    code = request.args.get('code')
    get_zoom_token.get_zoom_token(code)
    return redirect('/')

@app.route('/create_accounts', methods=['POST'])
def create_accounts():
    if session.get('access_token'):
        authorized = True
    else:
        authorized = False

    f = request.files['fileupload']
    successes = list()
    failures = list()
    message=""
    if f.filename[-4:] == '.csv':
        csv_dict = dictify_csv(f)
        for row in csv_dict:
            if row.get("email"):
                info = {
                  "action": "create",
                  "user_info": {
                    "email": row.get("email"),
                    "type": 1,
                    "first_name": row.get("first_name"),
                    "last_name": row.get("last_name")
                  }
                }
                result = create_user(info)
                if result['success']=='success':
                    successes.append(result)
                else:
                    failures.append(result)

    else:
        message= 'file must be a csv'
    return render_template("index.html",
                    successes = successes,
                    failures=failures,
                    message=message,
                    authorized = authorized)

@app.route('/logout')
def logout():
    session['access_token'] = None
    session['refresh_token']= None
    return redirect('/')
