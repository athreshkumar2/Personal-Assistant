"""Athresh Assistant"""
# This Is a virtual Speech to work based Python project
""" It is developed by Athresh Kumar Labde
For any queries contact me : Instagram-athresh_jr """

from typing import Text
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')                                    #it has inbuild voice which can be used,it is developed by Microsoft
voices = engine.getProperty('voices')                             #getting details of current voice
#print(voices[0].id)                                              #it will print the present Voices in this PC

engine.setProperty('voice',voices[0].id)                          #for setting any voice from this PC ([0]for David,[1] for Zara)

print("\nHey Welcome!")
print("I am Athresh Your Personal Voice Assistant\n")
print("You can exit by saying 'Bye'\n \n ")
print("Just ask : 'Sushant According to Wikipedia'")
print("         : 'What is The Time'")
print("         : 'Open Chrome'")
print("         : 'Open Youtube'\n")



def speak(audio):
    engine.say(audio)
    engine.runAndWait()                                           #Without this command, speech will not be audible to us.


def wishMe():                                                     #This is used to wish the user.We will not use print instead we will use speak because we are speaking rather than printing.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("I am Athresh Sir. Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()                                          # this class will help in recognizition of the audio.
    with sr.Microphone() as source:                              # this will use Microphone and listen we are printing it below to know that it is listening.
        print("I am Listening Athresh....")
        r.pause_threshold = 1                                    # this is the time duration when speach is complited it will take speech.
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')      #Using google for voice recognition.
        print(f"User said: {query}\n")                           #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")                        #Say that again will be printed in case of improper voice 
        return "None"                                            #None string will be returned
    return query






if __name__=="__main__" :
    wishMe()
    while True:                                                 #Don't declare while for wishMe() because it will ru wish function many times.
        query = takeCommand().lower()
        
        # Logic foe executing task based on Various Queries
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")              #we are removing wikipedia from the query because while searching it will take blank "" replacing "wikipedia"
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Athresh, the time is {strTime}")
        elif 'open calculator' in query:
            calpath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(calpath)
        elif 'open chrome' in query:
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        elif 'open document' in query:
            documentpath = "C:\\Users\\athre\\Documents"
            os.startfile(documentpath)
        elif 'open downloads' in query:
            downloadspath = "C:\\Users\\athre\\Downloads"
            os.startfile(downloadspath)
        elif 'bye' in query:
            speak("Have a Good day Athresh")
            print("Created by Athresh Kumar Labde")
            print("For Improvements/queries/suggestions \n Contact me via Instagram - athresh_jr\n\n")
            break

            
        
        
        
        
        
