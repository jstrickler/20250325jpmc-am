from flask import Flask
from flask_restful import fields, Resource, marshal_with, Api, reqparse
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
api = Api(app)

CONN_STR ='sqlite:///../DATA/airports.db'

engine = create_engine(CONN_STR, echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True)
print("Classes:", Base.classes)

Airport = Base.classes.airport

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)

airport_fields = {
    'id': fields.Integer,
    'code': fields.String,
    'location': fields.String,
}

airport_count = len(session.query(Airport).all())

error_data = {'error': 'invalid airport ID'}

def invalid_id_number(id_number):
    return not (1 <= id_number <= airport_count)

class InvalidAPIRequest(Exception):

    def __init__(self, message, status_code=400, data=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self._data = data

    def to_dict(self):
        return_value = dict(self.data or ())
        return_value['message'] = self.message
        return  return_value

class AirportByID(Resource):

    @marshal_with(airport_fields, envelope='airport')
    def get(self, id):
        """Retrieve one record"""
        try:
            p = session.query(Airport).filter(Airport.id == id).one()
        except:
            raise InvalidAPIRequest("Invalid id number")
        return p

    def put(self, id):
        """Replace one record"""
        if invalid_id_number(id):
            raise InvalidAPIRequest("Invalid id number")
        # code for PUT request here ...
        return {}

    def delete(self, termnum):
        """Delete one record"""
        if invalid_id_number(termnum):
            raise InvalidAPIRequest("Invalid term number")
        # code for DELETE request here ...
        return {}


class AirportByCode(Resource):
    """Retrieve airport record by 3-letter IATA code"""
    @marshal_with(airport_fields, envelope='airport')
    def get(self, code):
        """Retrieve one record"""
        try:
            p = session.query(Airport).filter(Airport.code == code.upper()).one()
        except:
            raise InvalidAPIRequest("Invalid code")
        return p

class AirportList(Resource):

    @marshal_with(airport_fields, envelope='airports')
    def get(self):
        """List all records"""
        airports = session.query(Airport).all()
        return airports

    @marshal_with(airport_fields, envelope='airport')
    def post(self):
        """Add a new record"""
        parser = reqparse.RequestParser()
        parser.add_argument('code', type=str)
        parser.add_argument('location', type=str)
        args = parser.parse_args()

        p = Airport(
            code=args.get('code'),
            location=args.get('location'),
        )

        session.add(p)
        session.commit()

        return p, 201

api.add_resource(AirportByID, '/api/airport/<int:id>')
api.add_resource(AirportByCode,'/api/airport/<string:code>')
api.add_resource(AirportList, '/api/airport')



if __name__ == '__main__':
    app.run(debug=True)

