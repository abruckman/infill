from flask import render_template, redirect, request, session
from app import app
import scripts.get_zoom_token
from config import CLIENT_ID, REDIRECT_URI

@app.route('/')
@app.route('/index')
def index():
    if session.get('access_token'):
        authorized = True
    else:
        authorized = False
    return render_template('index.html', authorized=authorized)

@app.route('/get_token')
def get_token():
    redirect_url = "https://zoom.us/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}"
    redirect_url = redirect_url.format(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI)
    return redirect(redirect_url)

@app.route('/oauth_return')
def oauth_return():
    print(request.args)
    code = request.args.get('code')
    scripts.get_zoom_token.get_zoom_token(code)
    return redirect('/')
