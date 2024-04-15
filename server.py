from os.path import dirname, realpath
from detector import *
from flask import Flask, request,send_file,url_for
from flask_restful import Resource, Api
from TextToSpeech import ToMP3
import os
import uuid
AudioPath = (dirname(realpath(__file__))+ '/API/Audio/')
app = Flask(__name__)
api = Api(app)
class AuthFace(Resource):
    def post(self):
        status:bool
        UPLOADS_PATH = (dirname(realpath(__file__))+ '/API/img')
        wallpaper = request.files['file']
        subject= request.values['subject']
        if wallpaper.filename != '':
            image = request.files['file']
            arrName = image.filename.split('\.')
            ext = arrName[len(arrName)-1]
            normalizedName = str(uuid.uuid4()) + '.' +ext
            image.save(os.path.join(UPLOADS_PATH, normalizedName))
            #print(os.path.join(UPLOADS_PATH, normalizedName))
            stuCode,name = validate(os.path.join(UPLOADS_PATH, normalizedName))
            print(stuCode)
            pathAudio =""
            if stuCode==None:
                cause = 0
                name = None
                status =False
                pathAudio=None
            elif stuCode=="Unknown":
                cause=1
                name=None
                status = False
                pathAudio = None
            else:
                cause=1
                status = True
                pathAudio = 'http://' + request.remote_addr + ':5000/download/Audio/' + str(ToMP3(stuCode,name,subject)) + '.mp3'

        return {'isTrue': status,
                'cause':cause,
                'stuCode': stuCode,
                'name': name,
                'audioUrl':pathAudio
                }
class index(Resource):
    def get(self):
        return {'isConnect': True,
                'ip':request.remote_addr,
                }

api.add_resource(AuthFace, '/AuthFace')  # Route_1
@app.route('/download/<folder_name>/<filename>')
def download(folder_name,filename):
    if '/' in filename or '\\' in filename:
        return 'Not Found'
    else:
        #path = "/API/"+str(folder_name)+"/"+str(filename)
        path = (dirname(realpath(__file__)) + '/API/'+folder_name+'/'+filename)
        return send_file(path, as_attachment=True)
api.add_resource(index, '/')  # Route_1
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
