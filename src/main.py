"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['POST'])#functional
def post_user():
    
    new_user = User(username= 'SampleUsername', email='SampleEmail@email.com', password= 'SamplePassword')
    db.session.add(new_user)
    db.session.commit()
    allusers = User.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

@app.route('/people', methods=['POST'])#functional
def post_character():
    #body = request.get_json()
    #new_user = User(username= body["username"], email=body["email"], password= body["password"])
    new_user1 = Character(character_name = "Chewbacca")
    new_user2 = Character(character_name = "Han Solo")
    new_user3 = Character(character_name = "Darth Vader")
    db.session.add(new_user1)
    db.session.add(new_user2)
    db.session.add(new_user3)
    db.session.commit()
    allusers = Character.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

@app.route('/planets', methods=['POST']) #functional
def post_planet():
    #body = request.get_json()
    #new_user = User(username= body["username"], email=body["email"], password= body["password"])
    new_user1 = Planet(planet_name = "Alderaan")
    new_user2 = Planet(planet_name = "Naboo")
    new_user3 = Planet(planet_name = "Mandalore")
    db.session.add(new_user1)
    db.session.add(new_user2)
    db.session.add(new_user3)
    db.session.commit()
    allusers = Planet.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

@app.route('/user', methods=['GET'])#functional
def get_users():

    allusers = User.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

    return jsonify(allusers), 200

@app.route('/people', methods=['GET'])#functional
def get_people():

    allusers = Character.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

    return jsonify(allusers), 200

@app.route('/planet', methods=['GET'])#functional
def get_planets():

    allusers = Planet.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

    return jsonify(allusers), 200

# @app.route('/onechar', methods=['GET'])
# def char():

#     allusers = Character.query.get(1)
#     allusers.favorited_by = 1
#     db.session.add(allusers)
#     db.session.commit()
#     return jsonify(allusers.serialize())

    




    








    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
