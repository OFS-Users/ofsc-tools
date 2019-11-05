import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
load_dotenv(os.path.join(basedir, '.env.secret'))

class Config(object):
    MONGO_URL = os.environ.get('MONGO_URL') or 'mongodb://database'
    OFSC_CLIENT_ID = os.environ.get('OFSC_CLIENT_ID') or '__token__'
    OFSC_CLIENT_SECRET = os.environ.get('OFSC_CLIENT_SECRET') or '__your_secret_goes_here_'
    OFSC_COMPANY = os.environ.get('OFSC_COMPANY') or 'sunrise'
    OFSC_ROOT = os.environ.get('OFSC_ROOT') or ''