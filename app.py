from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()



class Ships(db.Model):
    __tablename__ = 'ships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    imo = db.Column(db.Integer)
    iceClass = db.Column(db.String(30))
    speed = db.Column(db.String(30))



class Points(db.Model):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    coord = db.Column(db.String(500))
    ice_situation = db.Column(db.Integer)




class Kar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_icebreaker = db.Column(db.Integer)
    ships = db.Column(db.Text) #[id, id, id] of ships


class FormForRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ship = db.Column(db.String(50))
    id_a = db.Column(db.Integer, nullable=False)
    id_b = db.Column(db.Integer, nullable=False)
    a_time = db.Column(db.String(50))
    b_time = db.Column(db.String(50))


class Ice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coord = db.Column(db.Text) #[[57.74414062500001,70.4367988185464],[66.20361328125,73.53462847039683]]
    name = db.Column(db.Text)
    ice_situation = db.Column(db.Text)

#+json  с погодными условиями

@app.route('/form',methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        return ''
    else:
            name_ship = request.json['name']
            id_a = request.json['startPoint']
            id_b = request.json['endPoint']
            a_time = request.json['startTime']
            b_time = request.json['endTime']

            form = FormForRoute(name_ship=name_ship, id_a=id_a, id_b=id_b, a_time=a_time, b_time=b_time)
            try:
                db.session.add(form)
                db.session.commit()
                return '2'
            except:
                return '4'



@app.route('/forform',methods = ['POST', 'GET'])
def forform():
    if request.method == 'GET':
        try:
            ships = Ships.query.order_by(Ships.id).all()
            points = Points.query.order_by(Points.id).all()
            name_ships = []
            for i in ships:
                name_ships.append(i.name)
            name_points = []
            for i in points:
                name_points.append(i.name)
            rep = {"names": name_ships, "points": name_points}
            js = json.dumps(rep, ensure_ascii=False)
            return js

        except:
            return 'oh no'



@app.route('/add_ship', methods=['POST', 'GET'])
def add_ship():
    if request.method == 'GET':
            name = request.json['name']
            imo = request.json['imo']
            ice_class = request.json['iceClass']
            speed = request.json['speed']


            ship = Ships(name=name, imo=imo, iceClass=ice_class, speed=speed)
            try:
                db.session.add(ship)
                db.session.commit()
                return '2'
            except:
                return '4'



@app.route('/forweather', methods=['POST', 'GET'])
def forweather():
    if request.method == 'POST':
        return ''
    else:
        try:
            points = Points.query.order_by(Points.id).all()
            name_points = []
            for i in points:
                name_points.append(i.name)
            rep = {"points": name_points}
            js = json.dumps(rep, ensure_ascii=False)
            return js
        except:
            return ''


@app.route('/weather', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        return ''
    else:
        try:
            coord = request.json['points']
            points = Ice.query.order_by(Points.id).all()
            name_points = []
            for i in points:
                name_points.append(i.name)
            for i in range(len(name_points)-1):
                ice = Ice(name=str([name_points[i], name_points[i+1]]), ice_situation=coord[i])
                db.session.add(ice)
                db.session.commit()
            
        except:
            return ''

if __name__=='__main__':
    app.run(debug=True)
