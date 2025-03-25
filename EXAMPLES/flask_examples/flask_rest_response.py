#
from datetime import date
import xml.etree.ElementTree as ET
from flask import Flask, request, render_template, jsonify
from flask_bootstrap import Bootstrap

from president import President

app = Flask(__name__)
Bootstrap(app)


def pres_to_dict(pres):
    """Convert one president object to a dictionary"""
    pres_dict = {}
    for prop_name in dir(pres):
        if not prop_name.startswith('_'):
            prop_value = getattr(pres, prop_name)
            if isinstance(prop_value, date):
                prop_value = '{0.year:4d}-{0.month:02d}-{0.day:02d}'.format(prop_value)
            pres_dict[prop_name] = prop_value
    return pres_dict


def pres_list_to_xml(pres_list):
    """Convert list of presidents to XML"""
    root_element = ET.Element('presidents')
    for pres in pres_list:
        pres_element = ET.Element('president')
        fname = ET.Element('firstname')
        fname.text = pres.first_name
        pres_element.append(fname)
        lname = ET.Element('lastname')
        lname.text = pres.last_name
        pres_element.append(lname)
        root_element.append(pres_element)
    return ET.tostring(root_element)

@app.route('/president')
def index():
    """Main page; returns list of all presidents"""
    presidents = []
    for i in range(1, 46):
        presidents.append(President(i))
    accept_type = request.headers.get('ACCEPT')
    response = ''
    print("Accept type:", accept_type)
    if accept_type.startswith('text/html'):
        response = render_template('president_list_bs.html', presidents=presidents)
    elif accept_type.startswith('application/xml'):
        response = pres_list_to_xml(presidents)
    elif accept_type == 'application/json':
        presidents_as_dicts = [pres_to_dict(p) for p in presidents]
        response = jsonify(presidents=presidents_as_dicts)
    # handle error here if non-expected type

    return response



if __name__ == '__main__':
    app.run(debug=True)
