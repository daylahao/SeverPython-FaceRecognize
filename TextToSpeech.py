from gtts import gTTS
import os
language = 'vi'
def ToMP3(name):
    mytext = "Chào mừng "+name+" đến với lớp học"
    myobj = gTTS(text=mytext, lang=language, slow=False)
    path_str = "API/Audio/"+str(name)+".mp3"
    myobj.save(path_str)
    #os.system("Audio "+str(mytext)+".mp3")
    return name
#ToMP3("Chào mừng N20DCPT021 đến với lớp học")
