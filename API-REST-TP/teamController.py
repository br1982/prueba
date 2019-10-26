# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:54:40 2019

@author: Balta
"""
from equipo import Equipo, EquipoData
from flask import Flask
from flask_restful import Api

app = Flask(__name__)


api = Api(app)        

api.add_resource(Equipo, '/team')  # Route_1     
api.add_resource(EquipoData, '/team/<id>')  # Route_2"""


if __name__ == '__main__':
    app.run();   
    