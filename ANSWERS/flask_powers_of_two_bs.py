from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    powers = get_powers_of_two()
    print(f"{powers = }")

    return render_template(
        'powers_of_two.html', 
        title="Powers of Two", 
        powers_of_two=powers
    )

def get_powers_of_two():
    powers = []
    for i in range(32):
        element = i, 2 ** i
        powers.append(element)
    return powers

if __name__ == '__main__':
    app.run(debug=True)
