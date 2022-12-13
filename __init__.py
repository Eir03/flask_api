from flask import Flask, jsonify, request
from Backend.Query import Query
from Backend.Models import *

app = Flask(__name__)

query = Query()

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

@app.route("/posts", methods=['GET'])
def get_posts():
    try:
        data = []
        query_data = query.get_posts()
        if type(query_data) == list:
            for item in query_data:
                data.append(item.as_dict())
            return jsonify(data), 200
        else:
            return jsonify({"message":"Error in request"}), 400
    except Exception as ex: 
        return jsonify({"message":str(ex)}), 400

@app.route("/posts", methods=['POST'])
def add_post():
    try:
        query_data = query.add_post(request.get_json())
        if type(query_data) == PostModel:
            return jsonify(query_data.as_dict()), 201
        else:
            return jsonify({"message":"Error in request"}), 400
    except Exception as ex: 
        return jsonify({"message":str(ex)}), 400

@app.route("/post", methods=['POST'])
def get_post():
    try:
        query_data = query.get_post(request.get_json())
        if type(query_data) == PostModel:
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