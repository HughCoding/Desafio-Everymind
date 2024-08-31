# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a_secret_key')
    MYSQL_HOST = 'localhost'
    MYSQL_USER = '*****'
    MYSQL_PASSWORD = '******'
    MYSQL_DB = 'everymind'
