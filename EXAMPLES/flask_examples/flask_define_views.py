"""
Demo of route mapping
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():  # home page view
    """Default page view"""
    return '''<h1>Welcome to the App!</h1>
    <h3>This is the index page, provided by the index() view function</h3>
    '''

if __name__ == '__main__':
    app.run(debug=True)
