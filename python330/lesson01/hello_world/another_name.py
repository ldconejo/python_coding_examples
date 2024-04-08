import os
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World'

@app.route('/hello/<name>/')
def hello_name(name):
    return 'Hello, {}'.format(name)

@app.route('/goodbye/<name>/<times>/')
def goodbye_name(times, name):
    try:
        return(f"Goodbye {name}!")*int(times)
    except ValueError:
        return f"Goodbye {name}!"

@app.route('/')
def home():
    print("The root route was called!")
    return "Welcome to my sample Flask server!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)