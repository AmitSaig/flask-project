from flask import Flask, jsonify, request
import instrument
import requests
import json


instrumentDict = instrument.instruments
userDict = instrument.users
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome to my instrument project</h1><p>To view all the instruments, go to /instruments</p>"

@app.route("/instruments/all", methods=['GET'])
def get_instruments():
    response = app.response_class(
        response=json.dumps(instrumentDict),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/instruments/<inst_id>')
def get_instrument_by_id(inst_id):
    results =[]
    for item in instrumentDict:
        if item['id'] == int(inst_id):
            results.append(item)
    response = app.response_class(
        response=json.dumps(results),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/instruments/users/<user>')
def get_instruments_by_user(user):
    userList =[]
    for item in userDict:
        if item['name'] == str(user):
            user_info = (user , "is playing" , item['instruments'])
            userList.append(user_info)
    response = app.response_class(
        response=json.dumps(userList),
        status=200,
        mimetype='application/json'
    )
    return response

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