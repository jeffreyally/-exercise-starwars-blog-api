from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    # favorite_characters = db.relationship('Character', backref = 'user')
    # favorite_planets = db.relationship('Planet', backref = 'user')
    favorites = db.Column(db.String(999), unique=False, nullable=True)
    
    def __repr__(self):
        return '<Planets %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password":self.password,
            "username":self.username,
            "favorites": self.favorites,
            "is_actve": self.is_active
            #"favorite_characters": self.favorite_characters,
            #"favorite_planets": self.favorite_planets,
            
        }


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(40))
    # favorited_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return '<Planets %r>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            # "favorited_by":self.favorited_by
            
            
        }
    

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(40))
    # favorited_by = db.Column(db.Integer,db.ForeignKey('user.id'))
    

    def __repr__(self):
        return '<Planets %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.planet_name,
            # "favorited_by": self.favorited_by,
            
            
        }


