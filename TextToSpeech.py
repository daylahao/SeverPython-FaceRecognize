from gtts import gTTS
import os
language = 'vi'
PathAudio = "API/Audio/"
FileExtend = ".mp3"
def ToMP3(stuCode,name,subject):
    if(name =="Unknown"):
        mytext = "Khuôn mặt không phù hợp"
        path_str = PathAudio + str(stuCode) + FileExtend
        if os.path.isdir(path_str):
            return name
    else:
        mytext = "Chào mừng "+name+" đến với môn học"+str(subject)
    myobj = gTTS(text=mytext, lang=language, slow=False)
    path_str = PathAudio+str(stuCode)+FileExtend
    myobj.save(path_str)
    #os.system("Audio "+str(mytext)+".mp3")
    return stuCode
#ToMP3("Chào mừng N20DCPT021 đến với lớp học")
