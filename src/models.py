from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    hair_color = db.Column(db.String(80))
    eye_color = db.Column(db.String(80))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    gender = db.Column(db.String(80))
    birth_year = db.Column(db.String)
    skin_color = db.Column(db.String)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "height": self.height,
            "mass": self.mass,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "skin_color": self.skin_color,
            # do not serialize the password, its a security breach
        }
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(80))
    gravity = db.Column(db.String(80))
    terrain = db.Column(db.String(80))
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
            # do not serialize the password, its a security breach
        }
class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80))
    manufacturer = db.Column(db.String(80))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(80))
    vehicle_class = db.Column(db.String(80))


    def __repr__(self):
        return '<Vehicles %r>' % self.model

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "vehicle_class": self.vehicle_class,
            

            # do not serialize the password, its a security breach
        }