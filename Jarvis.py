from tkinter import *
import datetime
import pyttsx3
import wikipedia
import random
import os
import webbrowser
root=Tk()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def go():
    string=k.get()
    string.lower()
    if "hi" in string:
        speak("hello")
        Entry(root,textvariable=k).grid(row=2)
        string=""
    elif "wikipedia" in string:
        search=string
        search=search.replace("wikipedia","")
        speak("searching....")
        result=wikipedia.summary(search,sentences=2)
        print(result)
        speak(result)
        string=""
    elif "open google" in string:
        webbrowser.open("google.com",new=2)
        string=""
    elif "play music" in string:
        music='D:\\Music'
        songs=os.listdir(music)
        num=random.randint(0,34) 
        os.startfile(os.path.join(music,songs[num]))
    elif "time" in string:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        speak(time)
    elif 'open code'  in string:
        codepath="C:\\Users\\kanha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
def wishme():
    time=int(datetime.datetime.now().hour)
    if time<=12:
        speak("good morning sir I am your desktop assistant Jarvis")
    elif time>12 and time<16:
        speak("good afternoon sir I am your desktop assistant Jarvis")
    elif time>16 :
        speak("good evening sir I am your desktop assistant Jarvis")
wishme()
k=StringVar()
root.geometry("666x344")
Label(text="J.A.R.V.I.S.",font=("comocsansm",19,"bold")).grid(row=0,column=1)
Label(text="enter what you want to do sir").grid(row=1)
Entry(root,textvariable=k).grid(row=2)
Button(root,text="send",command=go).grid(row=3)
Label(text="commands:",font=("comicsnsm",9,"bold")).grid(row=4)
Label(text="time::::: time").grid(row=6)
Label(text="open google:::: open google").grid(row=7)
Label(text="open vscode:::: open code").grid(row=8)
Label(text="music::::: play music").grid(row=9)
Label(text="wikipedia search:::: wikipedia (what you want to search)").grid(row=5)
root.mainloop()

