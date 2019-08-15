import os

MODE = 'LOCAL'

ROOT_URL = 'api_v1.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = {
    'SECRET_KEY': 'ABCDEFGASD'
}

DATABASE = {
    'database': 'mysql',
    'account': 'root',
    'password': 'test123',
    'db_name': 'test',
    'host': 'localhost',
    'port': '3306'
}

