from flask import Flask, jsonify, request, render_template, redirect
import dictionary
import os
from classes import Instrument, User
import requests
import json


app = Flask(__name__)

instrument_data = {}
users_data = {}

@app.route('/')
def welcome():
    return "<h1>Welcome to my instrument project</h1><p>To view all the instruments, go to /instruments/all</p>"

@app.route("/instruments/all", methods=['GET'])
def get_instruments():
    response = app.response_class(
        response=json.dumps(instrument_data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/users/all", methods=['GET'])
def get_users():
    response = app.response_class(
        response=json.dumps(users_data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/instruments/<inst_id>')
def get_instrument_by_id(inst_id):
    results =[]
    for item in instrument_data.values():
        if item['id'] == inst_id:
            results.append(item)
    response = app.response_class(
        response=json.dumps(results),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/users/<user>')
def get_instruments_by_user(user):
    userList =[]
    for item in users_data.values():
        if item['name'] == user:
            user_info = (user , "is playing" , item['playing'])
            userList.append(user_info)
    response = app.response_class(
        response=json.dumps(userList),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/users/<userId>/<instrumentId>', methods=['GET', 'POST'])
def add_instrument_to_user(userId, instrumentId):
    for i in users_data.values():
        if i['id'] == userId:
            for item in instrument_data.values():
                if item['id'] == instrumentId:
                    i['playing'] = item['name']
                else:
                    return "no such instrument id"
        else:
            return "no such name id"

    response = app.response_class(
        response=json.dumps(users_data),
        status=200,
        mimetype='application/json'
    )
    return response



@app.route('/users/create/<newuser>', methods=['GET', 'POST'])
def add_user(newuser):
    value = User.create_id()
    play = {}
    new_user = User(newuser, value, play)
    user_data = {value: new_user.__dict__}
    users_data.update(user_data)
    response = app.response_class(
        response=json.dumps(user_data),
        status=200,
        mimetype='application/json'
    )
    print(response)
    return response

@app.route('/instruments/create/<new>', methods=['GET', 'POST'])
def add_instrument(new):
    value = Instrument.create_id()
    new_instrument = Instrument(new, value)
    id_for_dict = {value: new_instrument.__dict__}
    instrument_data.update(id_for_dict)
    response = app.response_class(
        response=json.dumps(id_for_dict),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/instruments/<id>/<link>', methods=['GET', 'POST'])
def add_video_to_instrument(id, link):
    for i in instrument_data.values():
        if i['id'] == id:
            i['video'] = 'https://www.youtube.com/watch?v=' + link
            return "success!"
        else:
            return "Instrument doesnt exist!"


@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            return redirect(request.url)
    return render_template("upload_image.html")


@app.route("/users/delete/<userId>", methods=['GET', "DELETE"])
def delete_user(userId):
    if userId in users_data:
        del users_data[userId]
        return "deleted!"

    return "ID not found"

@app.route("/users/delete/<userId>/<instrument>", methods=['GET', "DELETE"])
def delete_instrument_from_user(userId, instrument):
    if userId in users_data:
        if instrument in userId['playing']:
            del userId['play': instrument]
            return "deleted!"
        return "no such instrument"
    return "no such user"



if __name__ == "__main__":
    app.run()

# @app.route("/instruments/all", methods=['GET'])
# def get_instruments():
#     return jsonify(instrumentDict)

# @app.route('/instruments')
# def get_instrument_by_id():
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."
#     results = []
#     for item in instrumentDict:
#         if item['id'] == id:
#             results.append(item)
#     return jsonify(results)