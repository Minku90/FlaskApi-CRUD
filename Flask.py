from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import requests
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app)  # Enable CORS for the entire app

data_arg = reqparse.RequestParser()
data_arg.add_argument("ID", type=int, help="Enter ID")
data_arg.add_argument("Name", type=str, help="Enter Name")
data_arg.add_argument("Language", type=str, help="Enter Language")
data_arg.add_argument("Age", type=int, help="Enter Age")



class read_Delete(Resource):
    def __init__():
        data = pd.read_csv('data.csv')

@app.route('/<int:ID>', methods=['GET'])
def get(ID):
    try:
        data = pd.read_csv('data.csv')
        args = data_arg.parse_args()    
        data_found = data.loc[data['ID'] == ID].to_json(orient="records")
        return jsonify({'message': data_found, 'status_code': 200}), 200
    
    except Exception as e:        
        return jsonify({'message': 'An error occurred', 'status_code': 500}), 500

@app.route('/<int:ID>', methods=['DELETE'])
def delete(ID):
    try:
        data = pd.read_csv('data.csv')
        # args = data_arg.parse_args()     
        if ((data['ID'] == ID).any()):
            data = data.drop(data["ID"].loc[data["ID"] == ID].index)
            data.to_csv("data.csv", index=False)
            return jsonify({"message": 'Deleted successfully', 'status_code': 200}), 200
        else:
            return jsonify({"message": 'Not Present','status_code': 410}), 410
        
    except Exception as e:        
        return jsonify({'message': 'An error occurred', 'status_code': 500}), 500   

class Create_Update(Resource):
    def __init__():
        data = pd.read_csv('data.csv')

@app.route('/', methods=['POST'])
def post():
    try:       
        data = pd.read_csv('data.csv')
        args = data_arg.parse_args()
        request_data = request.get_json()
        if ((args.ID == data.ID).any()):
            return jsonify({'message': 'Duplicate data found', 'status_code': 409}), 409
        else:
             data = data.append(args, ignore_index=True)
             data.to_csv("data.csv", index=False)
             return jsonify({"message": 'Done', 'status_code': 200}), 200     

    except Exception as e:        
        return jsonify({'message': 'An error occurred', 'status_code': 500}), 500

@app.route('/', methods=['PUT'])
def put():
    try:
        data = pd.read_csv('data.csv')
        args = data_arg.parse_args()
        request_data = request.get_json()
        if ((args.ID == data.ID).any()):
            # data = data.drop(data.ID.loc.data.ID == args.ID.index)
            data = data.drop(data["ID"].loc[data["ID"] == args.ID].index)
            data = data.append(args, ignore_index=True)
            data.to_csv("data.csv", index=False)
            return jsonify({'message': 'Updated successfully', 'status_code': 200}), 200
        else:
            data = data.append(args, ignore_index=True)
            data.to_csv("data.csv", index=False)
            return jsonify({"message": 'Successfully Created', 'status_code': 200}), 200
        
    except Exception as e:        
        return jsonify({'message': 'An error occurred', 'status_code': 500}), 500

        
class ReadData(Resource):
    def __init__():
        data = pd.read_csv('data.csv')

@app.route('/get_data', methods=['GET'])
def get_data():
    try:    
        data = pd.read_csv('data.csv')
        data_records = data.to_dict(orient='records')
        # print(data_records)
        return jsonify({'message': data_records, 'status_code': 200}),200
    
    except Exception as e:        
        return jsonify({'message': 'An error occurred', 'status_code': 500}), 500


api.add_resource(read_Delete, '/<int:ID>')
api.add_resource(Create_Update, '/')
api.add_resource(ReadData, '/get_data')

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=5000)
