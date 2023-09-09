from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()



class Ships(db.Model):
    __tablename__ = 'ships'
    id = db.Column(db.Integer, primary_key=True)
    imo = db.Column(db.String(30))
    ice_class = db.Column(db.String(500))
    speed = db.Column(db.String(500))
    formRoute = relationship("FormForRoute", back_populates="ship")


class Points(db.Model):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    coord = db.Column(db.String(500))
    ice_situation = db.Column(db.Text)
    formRoute1 = relationship("FormForRoute", back_populates="point")


class Kar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_icebreaker = db.Column(db.Integer)
    ships = db.Column(db.Text) #[id, id, id] of ships


class FormForRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ship = db.Column(db.ForeignKey("ships.id"), nullable=False)
    id_a = db.Column(db.ForeignKey("points.id"), nullable=False)
    id_b = db.Column(db.ForeignKey("points.id"), nullable=False)
    a_time = db.Column(db.DateTime, default=datetime.utcnow)
    b_time = db.Column(db.DateTime, default=datetime.utcnow)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    ship = relationship("Ships", back_populates="formRoute")
    point = relationship("Point", back_populates="formRoute1")


#class Ice(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    coord = db.Column(db.Text) #[[57.74414062500001,70.4367988185464],[66.20361328125,73.53462847039683]]
#    ice_situation = db.Column(db.Text)

#+json  с погодными условиями

@app.route('/form',methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        return ''
    else:
        try:
            id_ship = request.json['id_ship']
            id_a = request.json['id_a']
            id_b = request.json['id_b']
            a_time = request.json['a_time']
            b_time = request.json['b_time']

            form = FormForRoute(id_ship=id_ship, id_a=id_a, id_b=id_b, a_time=a_time, b_time=b_time)
            try:
                db.session.add(form)
                db.session.commit()
                return '2'
            except:
                return '4'
        except:
            return ''


@app.route('/add_ship', methods=['POST', 'GET'])
def add_ship():
    if request.method == 'POST':
        return ''
    else:
        try:
            name =  request.json['name']
            imo = request.json['imo']
            ice_class = request.json['ice_class']
            speed = request.json['speed']

            ship = Ships(name=name, imo=imo, ice_class=ice_class, speed=speed)
            try:
                db.session.add(ship)
                db.session.commit()
                return '2'
            except:
                return '4'
        except:
            return ''


@app.route('/weather', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        return ''
    else:
        try:
            id_point =  request.json['id_point']
            coord = request.json['coord']
            ice_situation = request.json['ice_situation']


            editedship = db.session.query(Points).filter_by(coord=coord).one()
            editedship.ice_situation = ice_situation

            try:
                db.session.add(editedship)
                db.session.commit()
                return '2'
            except:
                return '4'
        except:
            return ''

if __name__=='__main__':
    app.run(debug=True)
