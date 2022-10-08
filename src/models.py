from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(120), unique=True, nullable=False)
    species = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    origin = db.Column(db.String(80), unique=False, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    image = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=False, nullable=False)
    created = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "type": self.type,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "image": self.image,
            "url": self.url,
            "created": self.created,
            
            # do not serialize the password, its a security breach
        }  
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(120), unique=True, nullable=False)
    dimension = db.Column(db.String(120), unique=True, nullable=False)
    residents = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Planet %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension,
            "residents": self.residents,
            "url": self.url,
            "created": self.created,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
        
       

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            # do not serialize the password, its a security breach
        }                              