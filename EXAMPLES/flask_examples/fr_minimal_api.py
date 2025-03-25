import json
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)  # Create instance of Flask
api = Api(app)  # Initialize Flask-RESTful extension

class Student(Resource):  # Create resource as class
    def get(self):  # Define method to handle HTTP GET requests
        return {'name': 'Jane Student'}  # Return data (will be converted to JSON response with status code 200)

# Configure route within API
# GET requests to URL /api/student will call Student.get
api.add_resource(Student,'/api/student')  

if __name__ == '__main__':
    app.run(debug=True)  # Launch development server with Flask app

