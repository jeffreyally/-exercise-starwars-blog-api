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


@app.route('/user', methods=['POST'])#generates the sample user
def post_user():
    
    new_user = User(username= 'SampleUsername', email='SampleEmail@email.com', password= 'SamplePassword', is_active=True)
    db.session.add(new_user)
    db.session.commit()
    allusers = User.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

@app.route('/people', methods=['POST'])#generates 3 sample starwars characters
def post_character():
    #body = request.get_json()
    #new_user = User(username= body["username"], email=body["email"], password= body["password"])
    new_user1 = Character(character_name = "Chewbacca")
    new_user2 = Character(character_name = "Yoda")
    new_user3 = Character(character_name = "R2-D2")
    db.session.add(new_user1)
    db.session.add(new_user2)
    db.session.add(new_user3)
    db.session.commit()
    allusers = Character.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

@app.route('/planet', methods=['POST']) #generates 3 sample starwars planets
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

@app.route('/user', methods=['GET'])#returns all users
def get_users():

    allusers = User.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

    return jsonify(allusers), 200

@app.route('/user/<int:id>', methods=['GET'])#returns one user
def get_one_user(id):

    oneUser = User.query.get(id)
    

    return jsonify(oneUser.serialize()), 200

@app.route('/people', methods=['GET'])#returns all starwars characters
def get_people():

    allusers = Character.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

    return jsonify(allusers), 200

@app.route('/people/<int:id>', methods=['GET'])#returns one starwars characters
def get_one_character(id):

    oneCharacter = Character.query.get(id)
    

    return jsonify(oneCharacter.serialize()), 200



@app.route('/planet', methods=['GET'])#returns all starwars planets
def get_planets():

    allusers = Planet.query.all()
    allusers = list(map(lambda x: x.serialize(), allusers))
    return jsonify(allusers)

    return jsonify(allusers), 200


@app.route('/planet/<int:id>', methods=['GET'])#returns one starwars planet
def get_one_planet(id):

    onePlanet = Planet.query.get(id)
    

    return jsonify(onePlanet.serialize()), 200

@app.route('/users/favorites', methods=['GET'])#returns favorites from the user
def user_favorites():
    theUser = User.query.get(1)

    
    return jsonify(theUser.favorites), 200



@app.route('/favorite/planet/<int:planet_id>', methods=['POST']) #adds a planet to favorites
def add_planet_to_favorite(planet_id):
    planetToAdd = Planet.query.get(planet_id)
    active_user = User.query.get(1)
    #active_user = User.query.filter_by(is_active=True).first()
    # if planetToAdd.planet_name in active_user.favorites:
    #     return "This favorite already exists in the favorites list", 400
    if active_user.favorites == None:
        active_user.favorites = planetToAdd.planet_name

    elif active_user.favorites == "":
        active_user.favorites = planetToAdd.planet_name

    else:
        active_user.favorites = active_user.favorites + ' ' + planetToAdd.planet_name
    
    db.session.add(active_user)
    db.session.commit()
    
    return jsonify(active_user.serialize())

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE']) #deletes the planet from favorites
def delete_planet_from_favorites(planet_id):
    planetToDelete = Planet.query.get(planet_id)
    active_user = User.query.filter_by(is_active=True).first()
    if planetToDelete.planet_name in active_user.favorites:
         PlanetRemoved = active_user.favorites.replace(planetToDelete.planet_name,'',1)
         
         active_user.favorites = PlanetRemoved
    # if planetToDelete.planet_name+' ' in active_user.favorites:
    #      newFavorites = active_user.favorites.replace(planetToDelete.planet_name+' ','',1)
    #      active_user.favorites = newFavorites
    db.session.add(active_user)
    db.session.commit()
    
    return jsonify(active_user.serialize())

@app.route('/favorite/people/<int:people_id>', methods=['POST']) #adds a character to favorites
def add_character_to_favorite(people_id):
    CharacterToAdd = Character.query.get(people_id)
    active_user = User.query.filter_by(is_active=True).first()
    #active_user = User.query.filter_by(is_active=True).first()
    # if planetToAdd.planet_name in active_user.favorites:
    #     return "This favorite already exists in the favorites list", 400
    if active_user.favorites == None:
        active_user.favorites = CharacterToAdd.character_name

    elif active_user.favorites == "":
        active_user.favorites = CharacterToAdd.character_name
    
    else:
        active_user.favorites = active_user.favorites + ' ' + CharacterToAdd.character_name
    
    db.session.add(active_user)
    db.session.commit()
    
    return jsonify(active_user.serialize())

@app.route('/favorite/people/<int:people_id>', methods=['DELETE']) #deletes character from favorites
def delete_character_from_favorites(people_id):
    CharacterToDelete = Character.query.get(people_id)
    active_user = User.query.filter_by(is_active=True).first()

    if CharacterToDelete.character_name in active_user.favorites:
         active_user.favorites = active_user.favorites.replace(CharacterToDelete.character_name,'',1)

    if ' '+CharacterToDelete.character_name in active_user.favorites:
         characterRemoved = active_user.favorites.replace(' '+CharacterToDelete.character_name,'',1)
         active_user.favorites = characterRemoved
    # if planetToDelete.planet_name+' ' in active_user.favorites:
    #      newFavorites = active_user.favorites.replace(planetToDelete.planet_name+' ','',1)
    #      active_user.favorites = newFavorites
    
    db.session.add(active_user)
    db.session.commit()
    
    return jsonify(active_user.serialize())




    








    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
