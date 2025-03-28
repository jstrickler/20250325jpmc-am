import json
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)  # Create instance of Flask
api = Api(app)  # Initialize Flask-RESTful extension

class Student(Resource):  # Create resource as class
    def get(self, id):  # Define method to handle HTTP GET requests
        # IRL: access DB to get data....
        # cursor.execute(...)
        # data = cursor.fetchall()
        return {'name': 'Jane Student', 'id': id, 'method': 'GET'}  # Return data (will be converted to JSON response with status code 200)

    def post(self, id):  # Define method to handle HTTP GET requests
        # IRL: access DB to get data....
        return {'name': 'Jane Student', 'id': id, 'method': 'POST'}  # Return data (will be converted to JSON 


# Configure route within API
# GET requests to URL /api/student will call Student.get
api.add_resource(Student,'/api/student/<int:id>')  

if __name__ == '__main__':
    app.run(debug=True)  # Launch development server with Flask app

