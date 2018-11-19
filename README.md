# Infill


Infill is a web-based widget for batch invinting users to the Zoom video conferencing service.

  - Authorization handled by oauth
  - CSV processed in the server
  - Detailed feedback on query results

## Live now

  - View it [live on Heroku](https://abruckman-infill.herokuapp.com/)
  - Usage instructions online

### Local Installation

Infill is built on Python 3.7.1. You will need python, venv and pip to run this app locally.

1. Clone the repo to you local machine
``` 
$ git clone https://github.com/abruckman/infill.git
```
2. Activate your virtual environment and install the dependencies
```
$ venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

3. Obtain your own API credentials for ZOOM. Go to the [ZOOM developer website](https://developer.zoom.us/) and open an account. Create an app and give it a name. Go into the app dashboard and make note of your Client ID and Client Secret.
4. Add your local OAuth return to you the app credentials
```
http://127.0.0.1:5000/oauth_return
```
5. Go to the scopes tab and add the scope for managing users, which is needed for the create users endpoint. (users:write:admin)
6. Go back to your local app's home directory and create a .env file
```
$ touch .env
```
7. Load your environemnt variables into the .env file 
```
CLIENT_ID=[YOUR CLIENT ID]
CLIENT_SECRET=[YOUR CLIENT SECRET]
REDIRECT_URI=http://127.0.0.1:5000/oauth_return
```
8. Export the app name variable.
```
$ export FLASK_APP=microblog.py
```
9. The app is now ready to run 
```
$ flask run
```

Enjoy! and thank you for using the app.
