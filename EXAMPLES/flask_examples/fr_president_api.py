from flask import Flask
from flask_restful import fields, Resource, marshal_with, Api, reqparse
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
api = Api(app)

CONN_STR ='sqlite:///presidents.db'

engine = create_engine(CONN_STR, echo=False)
Base = automap_base()
Base.prepare(engine)

President = Base.classes.presidents

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)

president_fields = {
    'termnum': fields.Integer,
    'firstname': fields.String,
    'lastname': fields.String,
    'birthstate': fields.String,
    'party': fields.String,
}

president_count = len(session.query(President).all())

error_data = {'error': 'invalid term number'}

def invalid_term_number(term_number):
    return not (1 <= term_number <= president_count)

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

class Presidents(Resource):

    @marshal_with(president_fields, envelope='president')
    def get(self, termnum):
        """Retrieve one record"""
        try:
            p = session.query(President).filter(President.termnum == termnum).one()
        except:
            raise ValueError("Invalid term number")
        return p

    def put(self, termnum):
        """Replace one record"""
        if invalid_term_number(termnum):
            raise ValueError("Invalid term number")
        return {}

    def delete(self, termnum):
        """Delete one record"""
        if invalid_term_number(termnum):
            raise ValueError("Invalid term number")
        return {}

class PresidentsList(Resource):

    def __init__(self):
        super().__init__()
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('termnum', type=int)
        self.reqparser.add_argument('firstname', type=str)
        self.reqparser.add_argument('lastname', type=str)
        self.reqparser.add_argument('birthstate', type=str)
        self.reqparser.add_argument('party', type=str)


    @marshal_with(president_fields, envelope='presidents')
    def get(self):
        """List all records"""

        args = self.reqparser.parse_args()
        presidents = session.query(President)
        firstname = args.get('firstname')
        lastname = args.get('lastname')
        birthstate = args.get('birthstate')
        party = args.get('party')

        if firstname:
            presidents = presidents.filter(President.firstname.like(f"%{firstname}%"))
        if lastname:
            presidents = presidents.filter(President.lastname.like(f"%{lastname}%"))
        if birthstate:
            presidents = presidents.filter(President.birthstate.like(f"%{birthstate}%"))
        if party:
            presidents = presidents.filter(President.party.like(f"%{party}%"))
        return presidents.all()

    @marshal_with(president_fields, envelope='president')
    def post(self):
        """Add a new record"""
        args = self.reqparser.parse_args()

        p = President(
            termnum=args.get('termnum'),
            firstname=args.get('firstname'),
            lastname=args.get('lastname'),
            birthstate=args.get('birthstate'),
            party=args.get('party'),
        )

        session.add(p)
        session.commit()

        return args, 201

api.add_resource(PresidentsList, '/api/presidents')
api.add_resource(Presidents, '/api/president/<int:termnum>')

if __name__ == '__main__':
    app.run(debug=True)

