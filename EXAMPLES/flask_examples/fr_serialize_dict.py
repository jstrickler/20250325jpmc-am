import json
from flask import Flask
from flask_restful import fields, Resource, marshal_with, Api, reqparse

app = Flask(__name__)
api = Api(app)

president_fields = {  # Define fields to be marshalled. Anything can be added here. Select fields to be exposed in API.
    'termnum': fields.Integer,
    'firstname': fields.String,
    'lastname': fields.String,
    'birth_state': fields.String(attribute="birthstate"),
    'party': fields.String,
    'url': fields.Url('presidents'),  # Get the URL for this resource
}

with open('presidents.json') as pres_in:  # Read presidents data from a JSON file
    PRESIDENTS = json.load(pres_in)

president_count = len(PRESIDENTS['presidents'])  # Get the number of presidents for later validation

error_data = {'error': 'invalid term number'}  # Define a default error payload

def invalid_term_number(term_number):  # Function to determine whether term number is valid
    return not (1 <= term_number <= (president_count + 1))

class InvalidAPIRequest(Exception):  # New exception type to be raised in case of error

    def __init__(self, message, status_code=400, data=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self._data = data

    def to_dict(self):
        return_value = dict(self.data or ())
        return_value['message'] = self.message
        return  return_value

class Presidents(Resource):  # Resource which expects unique ID (for GET, PUT, PATCH, and DELETE only)
    """
    Handle GET, PUT, PATCH, and DELETE posts.

    GET is only handled if a record number is specified.
    """

    @marshal_with(president_fields, envelope='president')  # Use the defined field list, president_fields, to control what gets returned; wrap data in a JSON object whose key is 'president'
    def get(self, termnum):  # Term number is passed into GET handler from URL
        """Retrieve one record"""
        if invalid_term_number(termnum):  # Check for invalid term number
            raise ValueError(f"Invalid term number: {termnum}")

        p = PRESIDENTS['presidents'][termnum - 1]
        return p  # Return dictionary of presidents; it is marshalled (serialized) into a dictionary (and later converted to JSON)

    def put(self, termnum):  # Implement PUT handler
        """Replace one record"""
        if invalid_term_number(termnum):
            raise ValueError("Invalid term number")
        return {}

    def delete(self, termnum):
        """Delete one record"""
        if invalid_term_number(termnum):
            raise ValueError("Invalid term number")
        return {}

class PresidentsList(Resource):  # Resource which does __not__ expect unique ID (for GET and POST only)
    """
    Handle GET and POST requests.

    GET is only handled if no ID is specified.
    """

    @marshal_with(president_fields, envelope='presidents')  # Use field list for each resource
    def get(self):
        """List all records"""
        presidents = PRESIDENTS['presidents']
        return presidents

    @marshal_with(president_fields, envelope='president')  # POST handler should return newly posted data using field list
    def post(self):
        """Add a new record"""
        parser = reqparse.RequestParser()  # Create new resource (as a dictionary here -- IRL would usually create a database record via ORM)
        parser.add_argument('termnum', type=int)
        parser.add_argument('firstname', type=str)
        parser.add_argument('lastname', type=str)
        parser.add_argument('birthstate', type=str)
        parser.add_argument('party', type=str)
        args = parser.parse_args()

        new_president = dict(  # Add new resource to dict (again, would add to database)
            termnum=args['termnum'],
            firstname=args['firstname'],
            lastname=args['lastname'],
            birthstate=args['birthstate'],
            party=args['party'],
        )

        PRESIDENTS['presidents'].append(new_president)  # Return marshalled data and HTTP status code

        return new_president, 201  # HTTP status 201 means "record added"

api.add_resource(PresidentsList, '/api/presidents')
api.add_resource(Presidents, '/api/presidents/<int:termnum>')

if __name__ == '__main__':
    app.run(debug=True)

