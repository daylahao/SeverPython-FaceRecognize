from gtts import gTTS
import os
language = 'vi'
PathAudio = "API/Audio/"
FileExtend = ".mp3"
def ToMP3(name):
    if(name =="Unknown"):
        mytext = "Khuôn mặt không phù hợp"
        path_str = PathAudio + str(name) + FileExtend
        if os.path.isdir(path_str):
            return name
    else:
        mytext = "Chào mừng "+name+" đến với lớp học"
    myobj = gTTS(text=mytext, lang=language, slow=False)
    path_str = PathAudio+str(name)+FileExtend
    myobj.save(path_str)
    #os.system("Audio "+str(mytext)+".mp3")
    return name
#ToMP3("Chào mừng N20DCPT021 đến với lớp học")
