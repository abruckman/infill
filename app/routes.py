from flask import render_template, redirect, request, session
from app import app
from scripts import get_zoom_token
from scripts.create_user import create_user
from config import CLIENT_ID, REDIRECT_URI
from app.forms import FileForm


@app.route('/')
@app.route('/index')
def index():
    form = FileForm()
    if session.get('access_token'):
        authorized = True
    else:
        authorized = False

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
    # form = FileForm()
    # if session.get('access_token'):
    #     authorized = True
    # else:
    #     authorized = False
    # if form.validate_on_submit():
    file = request.files['fileupload']
    fstring = f.read()
    print (fstring)
    # print ("hello")
    return redirect('/index')
    # print("failed validation")
    # return render_template('index.html', authorized=authorized, form=form)
    # info = {
    #   "action": "create",
    #   "user_info": {
    #     "email": "abruckman09+2@gmail.com",
    #     "type": 1,
    #     "first_name": "QALT",
    #     "last_name": "JGEOZL"
    #   }
    # }
    #
    # result = create_user(info)
    # print(result)

    return "hello"
