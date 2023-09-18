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
from models import db, User, Characters, Planets, Vehicles

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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

@app.route('/characters', methods=['GET'])
def get_all_characters():

    characters = Characters.query.all() 
    total_characters = list(map(lambda item: item.serialize(), characters))

    return jsonify(total_characters), 200


@app.route('/planets', methods=['GET'])
def get_all_planets():

    planets = Planets.query.all() 
    total_planets = list(map(lambda item: item.serialize(), planets))

    return jsonify(total_planets), 200

@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():

    vehicles = Vehicles.query.all() 
    total_vehicles = list(map(lambda item: item.serialize(), vehicles))

    return jsonify(total_vehicles), 200



@app.route('/character/<int:character_id>', methods=['GET'])
def get_character(character_id):

    character = Characters.query.filter_by(id=character_id).first()

    return jsonify(character.serialize()), 200



@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planet(planets_id):

    planet = Planets.query.filter_by(id=planets_id).first()

    return jsonify(planet.serialize()), 200


@app.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def get_vehicle(vehicles_id):

    vehicle = Vehicles.query.filter_by(id=vehicles_id).first()

    return jsonify(vehicle.serialize()), 200




@app.route('/users', methods=['GET'])
def get_users():

    users = User.query.all() 
    total_users = list(map(lambda item: item.serialize(), users))

    return jsonify(total_users), 200

@app.route('/users', methods=['POST'])
def create_user():
    body = json.loads(request.data) 
    

    query_user = User.query.filter_by(email=body["email"]).first() 
    
    if query_user is None:
        new_user = User(name=body["name"], email=body["email"], password=body["password"])
        db.session.add(new_user)
        db.session.commit()

        response_body = {
            "msg": "Created user"
        }
        return jsonify(response_body), 200

    response_body = {
            "msg": "existed user"
        }
    return jsonify(response_body), 400

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):

    user = User.query.filter_by(id=user_id).first()

    return jsonify(user.serialize()), 200

@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_favorite(user_id):

    
    favorite = Favorites.query.filter_by(user_id=user_id).all()
    total_favorite = list(map(lambda item: item.serialize(), favorite))

    return jsonify(total_favorite), 200


@app.route('/users/<int:user_id>/favorite/planet', methods=['POST'])
def create_favorite_planet(user_id):
    body = json.loads(request.data) 
    
    query_favorite_planet = Favorites.query.filter_by(favorite_planet_id=body["favorite_planet_id"], user_id=body["user_id"]).first() 
    print(query_favorite_planet)
    
    if query_favorite_planet is None:
        new_favorite_planet = Favorites(user_id=body["user_id"], favorite_planet=body["favorite_planet_id"], favorite_characters=body["favorite_characters_id"], favorite_vehicle=body["favorite_vehicle_id"])
        db.session.add(new_favorite_planet)
        db.session.commit()

        response_body = {
            "msg": "Created favorite planet"
        }
        return jsonify(response_body), 200

    response_body = {
            "msg": "existed favorite planet"
        }
    return jsonify(response_body), 400



@app.route('/users/<int:user_id>/favorite/character', methods=['POST'])
def create_favorite_character(user_id):
    body = json.loads(request.data) 

    query_favorite_people = Favorites.query.filter_by(favorite_character_id=body["people_id"], user_id=body["user_id"]).first() 
    print(query_favorite_people)
    
    if query_favorite_character is None:
        new_favorite_character = Favorites(user_id=body["user_id"], favorite_planet_id=body["planet_id"], favorite_character_id=body["people_id"], favorite_vehicle_id=body["vehicle_id"])
        db.session.add(new_favorite_character)
        db.session.commit()

        response_body = {
            "msg": "Created favorite character"
        }
        return jsonify(response_body), 200

    response_body = {
            "msg": "existed favorite character"
        }
    return jsonify(response_body), 400


@app.route('/users/<int:user_id>/favorite/vehicle', methods=['POST'])
def create_favorite_vehicle(user_id):
    body = json.loads(request.data) 

    query_favorite_vehicle = Favorites.query.filter_by(favorite_vehicle_id=body["vehicle_id"], user_id=body["user_id"]).first() 
    print(query_favorite_vehicle)
    
    if query_favorite_vehicle is None:
        new_favorite_vehicle = Favorites(user_id=body["user_id"], favorite_planet_id=body["planet_id"], favorite_character_id=body["people_id"], favorite_vehicle_id=body["vehicle_id"])
        db.session.add(new_favorite_vehicle)
        db.session.commit()

        response_body = {
            "msg": "Created favorite vehicle"
        }
        return jsonify(response_body), 200

    response_body = {
            "msg": "existed favorite vehicle"
        }
    return jsonify(response_body), 400

@app.route('/users/<int:user_id>/favorite/planet', methods=['DELETE'])
def delete_favorite_planet(user_id):
    body = json.loads(request.data) 
    
    query_favorite_planet = Favorites.query.filter_by(favorite_planet_id=body["planet_id"], user_id=body["user_id"]).first() 
    print(query_favorite_planet)
    
    if query_favorite_planet is not None:
        delete_planet_favorite = query_favorite_planet 
        db.session.delete(delete_planet_favorite)
        db.session.commit()

        response_body = {
            "msg": "Deleted favorite planet"
        }
        return jsonify(response_body), 200

    response_body = {
            "msg": "favorite planet does not exist"
        }
    return jsonify(response_body), 400



@app.route('/users/<int:user_id>/favorite/character', methods=['DELETE'])
def delete_favorite_character(user_id):
    body = json.loads(request.data) 

    query_favorite_character = Favorites.query.filter_by(favorite_character_id=body["people_id"], user_id=body["user_id"]).first() 
    print(query_favorite_character)
    
    if query_favorite_character is not None:
        delete_character_favorite = query_favorite_character 
        db.session.delete(delete_character_favorite)
        db.session.commit()

        response_body = {
            "msg": "Deleted favorite character"
        }
        return jsonify(response_body), 200

    response_body = {
            "msg": "favorite character does not exist"
        }
    return jsonify(response_body), 400


@app.route('/users/<int:user_id>/favorite/vehicle', methods=['DELETE'])
def delete_favorite_vehicle(user_id):
    body = json.loads(request.data) 

    query_favorite_vehicle = Favorites.query.filter_by(favorite_vehicle_id=body["vehicle_id"], user_id=body["user_id"]).first() 
    print(query_favorite_vehicle)
    
    if query_favorite_vehicle is not None:
        delete_vehicle_favorite = query_favorite_vehicle
        db.session.delete(delete_vehicle_favorite)
        db.session.commit()

        response_body = {
            "msg": "Deleted favorite vehicle"
        }
        return jsonify(response_body), 200

    response_body = {
            "msg": "favorite vehicle does not exist"
        }
    return jsonify(response_body), 400



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
