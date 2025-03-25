from flask import Flask

app = Flask(__name__)  # create Flask application object


@app.route('/')  # assign this view function to '/' (i.e., the "root: of the web site)
def index():  # define the view function
    return '<h1>Hello, Flask world!</h1>' # return HTML for the page to display

# app.register_route(index, '/')

if __name__ == '__main__':
    app.run(debug=True) # start the development server
