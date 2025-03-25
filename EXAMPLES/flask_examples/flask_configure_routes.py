from flask import Flask

from president import President

MAX_TERM = 47

app = Flask(__name__)

@app.route('/')
def index():
    """Default page for this site"""
    return '''<h1>President Information</h1>
    <h2>try .../president/term#</h1>
    <h2>try .../president/last-name</h1>
    '''

@app.route('/president/<int:termnum>/')
def president_by_term(termnum):
    """Retrieve president information for a specified term number"""
    if 0 < termnum < MAX_TERM:
        return format_html_for_president(termnum)
    else:
        html_content = '<h2>Sorry,  {} is not a valid term number</h2>'.format(termnum)
    return html_content

@app.route('/president/<last_name>/')
def president_by_last_name(last_name):
    """Retrieve president information for a specified last name;
        May return info for more than one president
    """
    html_content = ""
    for i in range(1, MAX_TERM):
        p = President(i)
        if p.last_name.lower() == last_name.lower():
            html_content += format_html_for_president(i)

    if html_content:
        return html_content
    else:
        return '<h2>Sorry,  {} not found</h2>'.format(last_name)

@app.route('/presidents/')
def president_list():
    html = ""
    for i in range(1, MAX_TERM):
        p = President(i)
        html += f"{i} -- {p.first_name} {p.last_name}<br/>"
    return html

def format_html_for_president(term_num):
    """Return HTML for one president by term number"""
    p = President(term_num)
    return  f'''
    <h1>{term_num}: {p.first_name} {p.last_name}</h1>
    <h2>Born in: {p.birth_state}</h2>
    <h2>Lived: {p.birth_date} to {p.death_date}</h2>
    <h2>Party: {p.party}</h2>
    '''


if __name__ == '__main__':
    app.run(debug=True)
