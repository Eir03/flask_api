from flask import Flask, jsonify, request
from Backend.Query import Query
from Backend.Models import UserModel
from flask_jwt_extended import JWTManager
from Backend.Config import secret_key

app = Flask(__name__)

query = Query()

app.config["JWT_SECRET_KEY"] = secret_key
jwt = JWTManager(app)

@app.route("/users", methods=['GET'])
def get_users():
    try:
        data = []
        query_data = query.get_users()
        if type(query_data) == list:
            for item in query_data:
                item.id = None
                item.password = None
                data.append(item.as_dict())
            return jsonify(data), 200
        else:
            return jsonify({"message":"Error in request"}), 400
    except Exception as ex: 
        return jsonify({"message":str(ex)}), 400

@app.route("/users", methods=['POST'])
def add_user():
    try:
        query_data = query.add_user(request.get_json())
        if type(query_data) == UserModel:
            return jsonify(query_data.as_dict()), 201
        else:
            return jsonify({"message":"Error in request"}), 400
    except Exception as ex: 
        return jsonify({"message":str(ex)}), 400

@app.route("/user", methods=['POST'])
def get_user():
    try:
        query_data = query.get_user(request.get_json())
        if type(query_data) == UserModel:
            query_data.password = None
            return jsonify(query_data.as_dict()), 201
        else:
            return jsonify({"message":"Error in request"}), 400
    except Exception as ex: 
        return jsonify({"message":str(ex)}), 400

#Обязательно в самом конце
#Запуск программы
if __name__ == '__main__':
    app.run(debug=True )