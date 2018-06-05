#!/usr/bin/env python

# Copyright (c) {{current_year}} Cisco and/or its affiliates.

# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of the
# License at
# 
               # https://developer.cisco.com/docs/licenses
# 
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
# 

from __future__ import print_function
import requests
import sys
import json
import os.path, sys
from flask import Flask, json, request
from pprint import pprint
#change path to allow import from parent directory
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from dnac import get_auth_token, create_url, wait_on_deploy
import csv

def ledON():
    token = get_auth_token()
    print("TOKEN : %s" % token)

    url = create_url(path="template-programmer/template/deploy")
    #payload = "{\"name\": project_name,\"tags\":[]}"
    payload = {"templateId":"bfb3ea5f-61a0-4ca4-9d57-5fd8dc03e41a","targetInfo":[{"id":"172.20.228.71","type":"MANAGED_DEVICE_IP", "params":{"apname":"APCC16.7EDB.6C5E","duration":"60"}}] }

    print("LED ON : Posting to %s" % url)
    print("BODY: Posting %s" % json.dumps(payload))
    headers= { 'x-auth-token': token['token'],
    	       'Content-Type': "application/json"}
    try:
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
        print (response.status_code)
        print (response.json())
        deploymentId = response.json()['deploymentId']
        print ("Waiting for deploymentId %s" % deploymentId)
        #deployment_result = wait_on_deploy(deploymentId, token)
        #print("LED ON RESULT: %s" % deployment_result)
        
    except requests.exceptions.RequestException  as cerror:
        print("Error processing request", cerror)
        sys.exit(1)
    return 200




# init a flash web app
app = Flask(__name__)

# validate web server from meraki
@app.route('/', methods=['GET'])
def get_base():
    return "Do nothing"
@app.route('/api', methods=['POST'])
def get_api_base():
    return "Do nothing"
@app.route('/api/v1', methods=['POST'])
def get_api_v1_base():
    return "Do nothing"

# receive location data
@app.route('/api/v1/getPowerLevels', methods=['GET'])
def get_all_power_levels():
    return "200"

# receive location data
@app.route('/api/v1/setPowerLevelHigh', methods=['POST'])
def set_power_level_high():
    return "200"

# receive location data
@app.route('/api/v1/setPowerLevelLow', methods=['POST'])
def set_power_level_low():
    response = ledON()
    return "200"

# receive location data
@app.route('/api/v1/setledON', methods=['POST'])
def set_power_level_normal():
    response = ledON()

    return "200"

app.run(port=3000, debug=False)
