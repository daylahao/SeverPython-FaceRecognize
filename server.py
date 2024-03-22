from os.path import dirname, realpath
from detector import *
from flask import Flask, request
from flask_restful import Resource, Api
import os
import uuid

app = Flask(__name__)
api = Api(app)

class AuthFace(Resource):
    def post(self):
        status:bool
        UPLOADS_PATH = (dirname(realpath(__file__))+ '/API/img')
        wallpaper = request.files['file']
        if wallpaper.filename != '':
            image = request.files['file']
            arrName = image.filename.split('\.')
            ext = arrName[len(arrName)-1]
            normalizedName = str(uuid.uuid4()) + '.' +ext
            image.save(os.path.join(UPLOADS_PATH, normalizedName))
            #print(os.path.join(UPLOADS_PATH, normalizedName))
            name = validate(os.path.join(UPLOADS_PATH, normalizedName))
            if name==None or name=="Unknown":
                status =False
            else:
                status = True
        return {'isTrue': status,
                'stuCode': name
                }
class index(Resource):
    def get(self):
        return {'isConnect': True}

api.add_resource(AuthFace, '/AuthFace')  # Route_1
api.add_resource(index, '/')  # Route_1
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
