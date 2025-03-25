from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    page = '<h1>Powers of two </h1>\n'
    for i in range(32):
        line = f'2^{i} = {2 ** i}<br/>\n'
        page += line
    return page

if __name__ == '__main__':
    app.run(debug=True)
