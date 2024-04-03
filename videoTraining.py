import cv2
from pathlib import Path
import pickle
import face_recognition
import os
from collections import Counter
from PIL import Image, ImageDraw
FileVideo  ="training/v_Hammering_g06_c05.avi"
PATH_FOLDER_ROOT = "./Cropfile/"
video_capture = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    #for (x, y, w, h) in faces:
    return faces
def getVideoCamera():
    print('Enter your student code:')
    idcode = input()
    i=0
    pathfolder = str(PATH_FOLDER_ROOT + idcode)
    if not os.path.isdir(pathfolder):
        os.mkdir(pathfolder)
    while(True):
        result, video_frame = video_capture.read()  # read frames from the video
        faces = detect_bounding_box(video_frame)  # apply the function we created to the video frame
        if(len(faces)>0):
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(video_frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            #     print('width: '+str(w)+"|| Height: "+str(h)+"||X: "+str(x)+"||Y: "+str(y)+"\n")
            #     video_frame = video_frame[y:y+h, x:x+w]
            filename = str(idcode)+'-'+str(i)+'.jpg'
            cv2.imwrite(pathfolder+'/'+filename,video_frame)
            i=i+1
        cv2.imshow("View", video_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video_capture.release()
    cv2.destroyAllWindows()
getVideoCamera()