
from distutils.log import debug
from flask import Flask, jsonify
from pymongo import MongoClient
import os
import subprocess

# Initiate Flask api
api = Flask(__name__)

# Get MongoDB Client
def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    
    db = client["animal_db"]
    return db

# Routes
@api.route('/')
def ping_server():
    return "Welcome to the world of Mongo!"

@api.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _animals = db.animal_tb.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@api.route('/times')
def get_times():
    # Copy output.txt from simulator into api
    contents = subprocess.run(["sshpass","-p","admin","scp","-o","StrictHostKeyChecking=no","admin@simulator:/app/output.txt","/api/output_copy.txt"])

    # Open the file and read its contents
    os.getcwd()
    with open('/api/output_copy.txt', 'r') as f:
        contents = f.read()

    # Return the contents of the file as a JSON response
    return jsonify({'contents': contents})

if __name__=='__main__':
    api.run(host="0.0.0.0", port=5000, debug=True)