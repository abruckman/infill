from flask import render_template, redirect
from app import app
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_token')
def get_token():
    redirect_url = "https://zoom.us/oauth/authorize?client_id={client_id} \
    &response_type=code&redirect_uri={redirect_uri}"
    print (redirect_url)
    redirect_url = redirect_url.format(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI)
    print (redirect_url)
    return redirect(redirect_url)
