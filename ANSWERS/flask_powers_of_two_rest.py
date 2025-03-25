from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/powers')
def index():
    powers_list = []
    for i in range(32):
        element = i, 2 ** i
        powers_list.append(element)
    return jsonify(powers_list)

if __name__ == '__main__':
    app.run(debug=True)
