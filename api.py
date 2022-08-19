import json
from distutils.log import debug

from flask import Flask, Response, jsonify
from pymongo import MongoClient

#mongodb://root:pass@test_mongodb:27017
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
    return jsonify({"welcome": "Welcome to the world of Mongo!"})

@api.route('/animals')
def get_stored_animals():
    db = ""
    try:
        db = get_db()
        _animals = list(db.animal_tb.find())
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animal": animals})
        #return Response(jsonify(**_animals))
    except:
        return jsonify({"message": "your request doesn't return any animal."})
    finally:
        if type(db)==MongoClient:
            db.close()

@api.route('/animals/wild')
def get_wild_animals():
    try:
        db = get_db()
        _animals = db.animal_tb.find({type: "Wild"})
        return Response(jsonify(**_animals))
    except:
        return jsonify({"error": "there's no one wild animal registered."})

if __name__=='__main__':
    api.run(host="0.0.0.0", port=5000, debug=True)
