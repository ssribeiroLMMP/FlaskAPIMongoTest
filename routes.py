from server import api, get_db
from flask import jsonify
from pymongo import MongoClient


# Routes
@api.route('/')
def ping_server():
    return_txt="Welcome to the world of Mongo!"
    return jsonify({"welcome": return_txt})

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

@api.route('/animals/wild')
def get_wild_animals():
    db=""
    try:
        db = get_db()
        _animals = db.animal_tb.find({"type":"Wild"})
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()