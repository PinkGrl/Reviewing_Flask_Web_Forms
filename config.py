import os 

class Config(object):
    """Define App Configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'

