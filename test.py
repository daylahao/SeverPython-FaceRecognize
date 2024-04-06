from pathlib import Path
import pickle
import face_recognition
from collections import Counter
from PIL import Image, ImageDraw

DEFAULT_ENCODINGS_PATH  = Path("output/encoding.pkl")

Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

def Openfile(model: str = "hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH) -> None:
    if encodings_location.exists():
        with encodings_location.open(mode="rb") as f:
            name_encodings = pickle.load(f)
            names = name_encodings["names"]
            encodings = name_encodings["encodings"]
        print(names)
Openfile()