from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Icebreakers(db.Model):
    __tablename__ = 'icebreakers'
    id = db.Column(db.Integer, primary_key=True)
    imo = db.Column(db.String(30))
    ice_class = db.Column(db.String(500))
    speed = db.Column(db.String(500))


class Ships(db.Model):
    __tablename__ = 'ships'
    id = db.Column(db.Integer, primary_key=True)
    imo = db.Column(db.String(30))
    formRoute = relationship("FormForRoute", back_populates="ship")


class Points(db.Model):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    coord = db.Column(db.String(500))
    formRoute1 = relationship("FormForRoute", back_populates="point")


class Kar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_icebreaker = db.Column(db.Integer)
    ships = db.Column(db.Text) #[id, id, id] of ships


class FormForRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ship = db.Column(db.ForeignKey("ships.id"), nullable=False)
    a = db.Column(db.ForeignKey("points.id"), nullable=False)
    b = db.Column(db.ForeignKey("points.id"), nullable=False)
    a_time = db.Column(db.DateTime, default=datetime.utcnow)
    b_time = db.Column(db.DateTime, default=datetime.utcnow)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    ship = relationship("Ships", back_populates="formRoute")
    point = relationship("Point", back_populates="formRoute1")

#+json  с погодными условиями 
