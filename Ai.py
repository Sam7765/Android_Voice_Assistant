import pyttsx3 
import datetime
import speech_recognition as sr
import os
import cv2
import random
import requests 
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtCore import QObject, QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui, QtWidgets
from AndroiBot import Ui_Androidio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
engine.setProperty('voices', voices[len(voices) - 1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
   hour = int(datetime.datetime.now().hour)

   if hour >= 0 and hour <= 12:
      speak("Good Moring ,")
      speak("How may I help You Today..!")
   elif hour >= 12 and hour <= 18:
      speak("Good AfterNoon,")
      speak("Anything that I Can Help U with...!")
   else:
      speak("Good Evening")
      #speak(f"How Can i help You..., {tt}")
   speak("I'm android 2 point O! is There anyThing You want me da Help You With..!")



class MainThread(QThread):
   def __init__(self):
      super(MainThread,self).__init__()

   def run(self):
      self.TaskExecution()
   

   def takecommand(self):
      r = sr.Recognizer()
      with sr.Microphone() as source:
        print("Listennng......")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=6)

      try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"your commnad: {query}\n")

      except Exception as e:
        print(e)
        #speak("can You that Again Please....!")
        return "none"
      query = query.lower()
      return query
   

   #if __name__ == "__main__":
   def TaskExecution(self):
       wish()
       while True:
            self.query = self.takecommand()

            if "open chrome" in self.query:
               speak("Openning Google Chrome..")
               npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
               os.startfile(npath)
        
            elif "open note test" in self.query:
               speak("Openning Note Pad..")
               apath = "C:\\Windows\\notepad.exe"
               os.startfile(apath)
        
            elif "open command prompt" in self.query:
               speak("openning command prompt..")
               os.system("start cmd")

            elif "open camera" in self.query:
               cap = cv2.VideoCapture(0)
               while True:
                  ret, img = cap.read()
                  cv2.imshow('webcam', img)
                  k = cv2.waitKey(50)
                  if k==27:
                     break;
                  cap.release()
                  cv2.destroyAllWindows()

            elif "play music" in self.query:
                  speak("Playing Music, Hope You will enjoy...")
                  music_dir = "C:\\Users\\Shubham\\Downloads\\Documents\\music"
                  songs = os.listdir(music_dir)
                  #rd = random.choice(songs)
                  for song in songs:
                     if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))#rd


            elif "wikipedia" in self.query:
                  speak("searching wikipedia.....")
                  query = query.replace("wikipedia", "")
                  results = wikipedia.summary(query, sentences=2)
                  speak("According to wikipedia..")
                  speak(results)
           #print(results)

            elif "open youtube" in self.query:
                  speak("Openning YouTube , Here you go...")
                  webbrowser.open("www.youtube.com")

            elif "open google" in self.query:
                  speak("Here I go, What do you want me to serach on google..")
                  cm = self.takecommand().lower()
                  webbrowser.open(f"{cm}")

            elif "play songs on youtube" in self.query:
                  kit.playonyt("Goku singing")

            elif "no thanks" in self.query:
                  speak("Good to see that i was able to help you...")
                  speak("have a great day..")
                  sys.exit()

            speak("Anything else You want da Help you With. ")
            speak("in Case, you goT any qyuestion need to be")
            speak("i'd be really really quick with it...")
            
startExecution = MainThread()

class Main(QMainWindow):
   def __init__(self):
      super().__init__()
      self.ui = Ui_Androidio()
      self.ui.setupUi(self)
      self.ui.pushButton.clicked.connect(self.startTask)
      self.ui.pushButton_2.clicked.connect(self.close)
   def startTask(self):
      self.ui.movie = QtGui.QMovie("C:\\Users\\Shubham\\Desktop\\pics\\backgrunds.gif")
      self.ui.label.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie = QtGui.QMovie("C:\\Users\\Shubham\\Desktop\\andro00\\robot.png")
      self.ui.label_2.setMovie(self.ui.movie)
      self.ui.movie.start()
      timer = QTimer(self)
      timer.timeout.connect(self.showTime)
      timer.start(1000)
      startExecution.start()

   def showTime(self):
      current_time = QTime.currentTime()
      current_date = QDate.currentDate()
      label_time = current_time.toString('hh:mm:ss')
      label_date = current_date.toString(Qt.ISODate)
      self.ui.textBrowser.setText(label_date)
      self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
Androoid2O = Main()
Androoid2O.show()
exit(app.exec_())



