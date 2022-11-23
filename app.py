from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Testing a Flask Application using CLoud Build!</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
