
from distutils.log import debug
from flask import Flask, jsonify
from pymongo import MongoClient

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

if __name__=='__main__':
    api.run(host="0.0.0.0", port=5000, debug=True)