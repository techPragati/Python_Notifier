import pyttsx3 #pip install pyttsx3==2.6
import datetime
import time
from win10toast import ToastNotifier#pip install win10toast
toaster = ToastNotifier()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def nowtime():
    strTime = datetime.datetime.now().strftime("%H") 
    return strTime
nowtime=nowtime()
#print(nowtime)


query = {
  "brush":6 ,
  "Take bath":7,
  "have your breakfast ":8,
  "take your lunch":15,
  "take rest":15,
  "join class ":20

}

#print(tuple(query.items())[i]][0])

while True:
    for i in range(0,len(query)):
        task=tuple(query.items())[i][0]
        y=int(query.get(task))
        #print(task)
        #print(y)

        
        if y==int(nowtime):
            speak("it is,"+str(nowtime)+",now"+str(task))
            toaster.show_toast(str(task),"It is "+str(nowtime),duration=10) 

    time.sleep(3600)