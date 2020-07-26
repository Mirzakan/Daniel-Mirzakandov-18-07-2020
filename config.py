import os

class Config(object):
    #key check against a cookie file that was created by this application
    #If it's been altered the session file is no longer valid for security reasons.
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    # MONGODB = { 'db' : 'mongodb+srv://daniel:1234@mirz.wmqfv.mongodb.net/Mirz?retryWrites=true&w=majority'}
    