from flask import Flask
import pymongo, json
from bson import ObjectId
from bson import json_util
import software_configuration as cfg
from user import User
from utils.weather_information import weather_information

from datetime import timedelta
from flask import Flask, render_template, url_for, redirect, request, session
from authlib.integrations.flask_client import OAuth
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

'''
Required App, Oauth, Session Management Initializations
'''

app = Flask(__name__, static_url_path='',
                  static_folder='build',
                  template_folder='templates')


oauth = OAuth(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.needs_refresh_message = (u"Session timedout, please re-login")
login_manager.needs_refresh_message_category = "info"


'''
Read credentials from the configuration file
'''
app.config['SECRET_KEY'] = "THIS SHOULD BE SECRET"



'''
Initialize google oauth registration details
'''
google = oauth.register(
    name = 'google',
    client_id = app.config["GOOGLE_CLIENT_ID"],
    client_secret = app.config["GOOGLE_CLIENT_SECRET"],
    access_token_url = 'https://accounts.google.com/o/oauth2/token',
    access_token_params = None,
    authorize_url = 'https://accounts.google.com/o/oauth2/auth',
    authorize_params = None,
    api_base_url = 'https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint = 'https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs = {'scope': 'openid email profile'},
)


@login_manager.user_loader
def loadUser(user_id):
    
    #Load current user on the basis of the Unique ID
    return User('116296017614486242589', 'Rohit Lokwani', 'rlokwani@uw.edu')
#     return User.get(user_id)


@app.route("/logout")
@login_required
def logout():
    
    #If the user clicks on the logout link
    
    logout_user()
    return redirect(url_for("index"))


@app.before_request
def beforeRequest():
    
    #Setting logout time
    
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

    
@app.route("/")
def index():
    '''
    Link to the homepage. This is what the UI will be calling.
    '''
    
    print (current_user.is_authenticated)
    if current_user.is_authenticated:
        
        return (
            "<p>Hello, {}! You're logged in! We would like to take you on a optimized ride! Email: {}</p>"
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'

    
@app.route('/login')
def googleLogin():
    '''
    Google login route
    '''
    
    google = oauth.create_client('google')
    redirected_url = url_for('googleAuthorize', _external=True)
    return google.authorize_redirect(redirected_url)


@app.route('/login/google/authorize')
def googleAuthorize():
    '''
    Google authorization route
    '''
    
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()
    print (user_info["id"], user_info['name'], user_info['email'])
    
    if user_info.get("verified_email"):
        unique_id = user_info["id"]
        user_email = user_info["email"]
        user_name = user_info["name"]
    else:
        return "User email not available or not verified by Google.", 400
    
    
    
    #Check for user's existence in the database, insert one if not already in the database
    
    user = User.get(unique_id)
    
    if user is not None:
        login_user(user)
    else:
        print ("Ignore")
        user=User(unique_id, user_name, user_email)
        user_created = user.create(unique_id, user_name, user_email)
        if user_created == False:
            return "User creation in the database failed"
    
    login_user(user)
    print ("Google Login Successful")
    # Send user to the required page
    return redirect(url_for("index"))


###Get parameters and make things work
@app.route("/get_cab_price")
def run_main():
    source = request.args.get('source')
    destination = request.args.get('destination')
    type_of_car = request.args.get('cab_type')
    
    # Call google maps API - Get code from Shubha
    
    source_latitude='10.25'
    source_longitude='100.25'
    destination_latitude='12.5'
    destination_longitude='1000'
    distance='0.2'
    ETA=15
    
    cab_rides_original_df=pd.read_csv('cab_rides.csv')
    cab_rides_current_df=all_the_above_parameters
    
    #preprocess cab_rides_csv, save and run the code
    cab_rides_original_df.append(cab_rides_current_df, ignore_index=True)
    cab_rides_original_df.to_csv('cab_rides.csv')
    
    # Call uber and lyft API
    uber_original_surge='1.5'
     
    
    # Lyft not available
    lyft_original_surge = '1.0'
    
    # Call weather API
    weather_current_df=weather_information(latitude, longitude)
    
    weather_original_df=pd.read_csv('weather.csv')
    
    #preprocess(weather_current_df), save and run the code
    weather_current_df['surge_price']=[uber_original_surge]
    weather_original_df.append(weather_current_df, ignore_index=True)
    weather_original_df.to_csv('weather.csv')
    
    return json_object




if __name__ == '__main__':
    app.run()
