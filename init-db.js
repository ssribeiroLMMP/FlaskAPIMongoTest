// Runs only after Database creation: populates database

db = db.getSiblingDB('animal_db')

// Drop Existing Animal "Table"
db.animal_tb.drop()

// Recreate Animal "Table"
db.animal_tb.insertMany([
    {
        "id":1,
        "name":"Lion",
        "type":"Wild"
    },
    {
        "id":2,
        "name":"Cow",
        "type":"Domestic"
    }
]);
