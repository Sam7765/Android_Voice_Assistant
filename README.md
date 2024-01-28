# Android_voice_Assistant

## Features

It can do a lot of cool things, some of them being:

- Greet user
- Tell current time and date
- Launch applications/softwares 
- Open any website
- Tells about weather of any city
- Open location of any place plus tells the distance between your place and queried place
- Tells your current system status (RAM Usage, battery health, CPU usage)
- Tells about your upcoming events (Google Calendar)
- Tells about any person (via Wikipedia)
- Can search anything on Google 
- Can play any song on YouTube
- Tells top headlines (via Times of India)
- Plays music
- Send email (with subject and content)
- Calculate any mathematical expression (example: Jarvis, calculate x + 135 - 234 = 345)
- Answer any generic question (via Wolframalpha)
- Take important note in notepad
- Tells a random joke
- Tells your IP address
- Can switch the window
- Can take screenshot and save it with custom filename
- Can hide all files in a folder and also make them visible again
- Has a cool Graphical User Interface



## Basic Info On Android Assistant

- Pyttsx3:- This module is used for the conversion of text to speech in a program it works offline. To install this module type the below command in the terminal.
pip install pyttsx3

- Wikipedia:- As we all know Wikipedia is a great source of knowledge just like GeeksforGeeks we have used the Wikipedia module to get information from Wikipedia or to perform a Wikipedia search. To install this module type the below command in the terminal.

- Speech Recognition:- Since we’re building an Application of voice assistant, one of the most important things in this is that your assistant recognizes your voice (means what you want to say/ ask). To install this module type the below command in the terminal.

- Datetime:- Date and Time are used to showing Date and Time. This module comes built-in with Python.

  # Implementation

  Import the below libraries.

- import pyttsx3 
- import datetime
- import speech_recognition as sr
- import os
- import cv2
- import random
- import requests 
- import wikipedia
- import webbrowser
- import pywhatkit as kit
- import sys
- from PyQt5 import QtWidgets,QtCore, QtGui
- from PyQt5.QtCore import QObject, QTimer, QTime, QDate, Qt
- from PyQt5.QtGui import QMovie
- from PyQt5.QtCore import *
- from PyQt5.QtGui import *
- from PyQt5.QtWidgets import *
- from PyQt5.uic import loadUiType
- from PyQt5 import QtCore, QtGui, QtWidgets
- from AndroiBot import Ui_Androidio


