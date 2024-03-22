import os

import cv2
import numpy as np
from pathlib import Path
import pickle
import face_recognition
from PIL import Image, ImageDraw
def Crop_Image():
    return
def recognize_faces(
    image_location: str,
    model: str = "hog",
) -> None:
    PathTraining = "./training/"
    input_image = face_recognition.load_image_file(image_location)
    pathfile,extend = image_location.split('.')
    listfile = pathfile.split('\\')
    filename  = listfile[len(listfile)-1]
    foldername = listfile[len(listfile)-2]
    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    pillow_image = Image.fromarray(input_image)
    # width, height = pillow_image.size
    print(input_face_locations)
    if  input_face_locations!=[]:
        top, right, bottom, left = input_face_locations[0]
        img2 = pillow_image.crop((left-((right-left)/2), top-((bottom-top)/2), right+((right-left)/2), bottom+((bottom-top)/2)))
        # img2.show()
        print(PathTraining+foldername)
        if not os.path.isdir(PathTraining+foldername):
            os.mkdir(PathTraining+foldername)
        img2.save(PathTraining+foldername+"/"+filename+"."+extend, "JPEG")
def run(model: str = "hog"):
    for filepath in Path("cropfile").glob("*/*"):
        # print(filepath)
        # recognize_faces(image_location=str(""), model=model)
        recognize_faces(image_location=str(filepath.absolute()), model=model)
run()