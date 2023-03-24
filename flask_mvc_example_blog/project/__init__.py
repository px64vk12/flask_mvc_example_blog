# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
from pymongo import MongoClient

#test
users = {'admin': {'password': '1234'}}


app = Flask('project')
app.config['SECRET_KEY'] = 'random'

url = "mongodb+srv://pbh980915:<password>!@cluster0.bnqo3en.mongodb.net/test"
client = MongoClient(url)
mongodb = client['flask_example_blog']

app.debug = True
from project.controllers import *
