# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 14:33:15 2022

@author: rithi
"""
from flask import Flask, render_template, request
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
API_KEY = "3430c217-4809-4c66-8865-83f9547c178c"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()['access_token']
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__,static_url_path='')
'''model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))'''
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/71547275-5076-442b-8559-57f19ed6680e/predictions?version=2022-11-05', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    predictions = response_scoring.json()
    output=predictions(prediction[0],2)
    if output<0:
        return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
    else:
        return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))

if __name__=="__main__":
    app.run(debug=True)

