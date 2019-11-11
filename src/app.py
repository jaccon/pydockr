#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request
from flask import Response
import os
import sys
import urllib, json
import requests
import time
import datetime


reload(sys)  
sys.setdefaultencoding('utf8')

appVersion = "0.1.0"
appListen = 8080 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Wellcome to PyDockr"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=appListen, debug=False, use_reloader = True)


