# Modules used 
from flask import Flask, jsonify
from config import Dbconfig
from pymongo import MongoClient

#creating the app
# Initiate Flask api
api = Flask(__name__)


dbconfig=Dbconfig()

# Get MongoDB Client
def get_db():
    client = MongoClient(host=dbconfig.host,
                         port=dbconfig.port, 
                         username=dbconfig.username, 
                         password=dbconfig.passaword,
                         authSource=dbconfig.authSource)
# dbconfig)
    
    db = client["animal_db"]
    return db
