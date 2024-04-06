from pathlib import Path
import pickle
import face_recognition
from collections import Counter
from PIL import Image, ImageDraw

DEFAULT_ENCODINGS_PATH  = Path("output/encoding.pkl")

Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

def encode_known_faces(model: str = "hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH) -> None:
    folderIgnore=[]
    if encodings_location.exists():
        with encodings_location.open(mode="rb") as f:
            name_encodings = pickle.load(f)
        names = name_encodings["names"]
        encodings = name_encodings["encodings"]
        for filepath in Path("training").glob("*/*"):
            name = filepath.parent.name
            if( name in names):
                folderIgnore.append(name)
    else:
        names = []
        encodings = []
    for filepath in Path("training").glob("*/*"):
        name = filepath.parent.name
        if name in folderIgnore:
            pass
        else:
            print(filepath)
            image = face_recognition.load_image_file(filepath)
            face_locations = face_recognition.face_locations(image, model=model)
            face_encodings = face_recognition.face_encodings(image, face_locations)

            for encoding in face_encodings:
                names.append(name)
                encodings.append(encoding)
            name_encodings = {"names": names, "encodings": encodings}
    with encodings_location.open(mode="wb") as f:
        pickle.dump(name_encodings, f)
# encode_known_faces()
def recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)
    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )
    pillow_image = Image.fromarray(input_image)
    # draw = ImageDraw.Draw(pillow_image)
    i=0
    name = "Unknown"
    for bounding_box, unknown_encoding in zip(input_face_locations, input_face_encodings):
        i=i+1
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
        # _display_face(draw, bounding_box, name)
    if i>1:
        name = None
        return name
    else:
        return name
        # return name
    # del draw
    #pillow_image.show()
    # print(name, bounding_box)
def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(name
                    for match, name in zip(boolean_matches, loaded_encodings["names"])
                    if match
                    )
    if votes:
        return votes.most_common(1)[0][0]

# BOUNDING_BOX_COLOR = "blue"
# TEXT_COLOR = "white"
# def _display_face(draw, bounding_box, name):
#     top, right, bottom, left = bounding_box
#     draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)
#     text_left, text_top, text_right, text_bottom = draw.textbbox(
#         (left, bottom), name
#     )
#     draw.rectangle(
#         ((text_left, text_top), (text_right, text_bottom)),
#         fill="blue",
#         outline="blue",
#     )
#     draw.text(
#         (text_left, text_top),
#         name,
#         fill="white",
#     )
def validate(image_file,model: str = "hog"):
    #for filepath in Path("validation").rglob("*"):
    #     if filepath.is_file():
    #         recognize_faces(
    #             image_location=str(filepath.absolute()), model=model
    #         )
    name = recognize_faces(image_location=str(image_file), model=model)
    print(name)
    return name



# Removed recognize_faces("unknown.jpg")
# validate(str(""))
# recognize_faces("unknown.jpg")