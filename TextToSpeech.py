from gtts import gTTS
import binascii
import os
language = 'vi'
PathAudio = "API/Audio/"
FileExtend = ".Wav"
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
    print(path_str)
    #os.system("Audio "+str(mytext)+".mp3")
    return MP3toHEX(path_str)
#ToMP3("Chào mừng N20DCPT021 đến với lớp học")
def MP3toHEX(pathAudioServer):
    hexString = ""
    with open(pathAudioServer, 'rb') as f:
        content = f.read()
    hexString = binascii.hexlify(content)
    return hexString