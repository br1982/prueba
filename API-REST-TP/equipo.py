# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:32:52 2019

@author: Balta
"""

"""from flask_api import status"""
from flask import request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///C:\\Users\\Balta\\PythonTest\\API-REST-TP\\chinook.db')

class Equipo(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM teams")
        return query.cursor.fetchall(),  '200'
            
    def post(self):
        conn = db_connect.connect()
        nombre = request.json['nombre']
        cuit = request.json['cuit']
        direccion = request.json['direccion']
        email = request.json['email']
        phone = request.json['phone']
        
        query = conn.execute("INSERT INTO teams values(null, '{0}', '{1}', '{2}', '{3}', '{4}')".format(nombre, cuit, direccion, email, phone))
        
        return {'201': 'Equipo guardado con éxito!'}


class EquipoData(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM teams WHERE idteam =%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)
    def delete(self, id):
        conn = db_connect.connect()
        query = conn.execute("DELETE FROM teams WHERE idteam = %d" % int(id))
        return {'201': 'Se eliminó con éxito el equipo'}

    def patch(self, id):
        setear = ''
        for field in request.json:
            setear += field + " = '" + request.json[field] + "' AND "
            
        conn = db_connect.connect()
        query = conn.execute("UPDATE teams SET %s WHERE idteam = %d" % (setear[0:len(setear)-4], int(id)))
        
        return {'201': 'Se actualizó correctamente los siguientes campos: '}