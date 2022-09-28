import os
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    '0.0.0.0',
    'todolist42.herokuapp.com', # your herokuapp url
    'https://todolist42.herokuapp.com',
    '127.0.0.1'
]
