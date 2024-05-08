import os
from flask import Flask

app = Flask(__name__)

with open('zip_code.txt') as file:
    zipcodes = {}
    for line in file.readlines():
        data = line.strip().split(',')  # ["78256","29.622289"," -98.626164"]
        zipcodes[data[0].strip()] = data[1:] # { "78256": ["29.622289"," -98.626164"]}

@app.route('/<zipcode>/')
def get_coordinates(zipcode):
    return str(zipcodes[zipcode])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 50001))
    app.run(host='0.0.0.0', port=port)