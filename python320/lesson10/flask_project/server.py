from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine, text
from flask import jsonify

class Employees(Resource):
    def get(self):
        conn = db_connect.connect()
        text_query = "select * from employees"
        query = conn.execute(text(text_query))
        results = {"employees": [i[1] for i in query.cursor.fetchall()]}
        conn.close()
        return jsonify(results)
    
class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        text_query = "select trackid, name, composer, unitprice from tracks"
        query = conn.execute(text(text_query))
        result = {
            "data": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        }
        conn.close()
        return jsonify(result)
    
class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        #text_query = "select * from employees where EmployeeId ='%s'" % str(employee_id)
        text_query = f"select * from employees where EmployeeId = '{str(employee_id)}'"
        query = conn.execute(text(text_query))
        result = {
            "data": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        }
        conn.close()
        return jsonify(result)

db_connect = create_engine("sqlite:///chinook.db")

app = Flask(__name__)

api = Api(app)
api.add_resource(Employees, "/employees")
api.add_resource(Tracks, "/tracks")
api.add_resource(Employees_Name, "/employees/<employee_id>")

if __name__ == "__main__":
    app.run(port="5002")

    db_connect.dispose()