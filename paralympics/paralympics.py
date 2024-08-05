from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello and welcome to my paralympics app'

@app.route('/hello/<username>')
def hello(username):
    return f'Hello {(username)} and welcome to my paralympics app'

if __name__ == '__main__':
    app.run(debug=True)

