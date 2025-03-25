from datetime import date
from flask import Flask, request, jsonify
from flask_bootstrap import Bootstrap

from president import President

app = Flask(__name__)
Bootstrap(app)

@app.route('/president/')
def president_list():
    """Return list of all presidents"""
    presidents = get_presidents()
    presidents_as_dicts = [pres_to_dict(p) for p in presidents]
    response = jsonify(presidents=presidents_as_dicts)
    return response

@app.route('/president/<int:term>/')
def president(term):
    return jsonify(pres_to_dict(President(term)))

def pres_to_dict(president):
    """Convert president object to a dictionary"""
    pres_dict =  president.__dict__
    return {field_name.removeprefix('_'): value for field_name, value in pres_dict.items()}

def get_presidents():
    presidents = []
    for i in range(1, 46):
        presidents.append(President(i))
    return presidents

if __name__ == '__main__':
    app.run(debug=True)
