import os
import tkinter as tk
import tkinter.messagebox
import speech_recognition as sr
import pyttsx3
import random
import pyaudio
import wave
from tkinter import *

root = Tk()
root.title("Идентификация и аутентификация")
root.geometry('300x300')
r = sr.Recognizer()
strVar = tk.StringVar()
usrVar = tk.StringVar()
voice = "1"
words = ["привет", "мартышка", "огурец", "платье", "футболка", "абрикос", "корзина"]
wts = ""
n = 5


def SpeakText(command):
    enigne = pyttsx3.init()
    enigne.say(command)
    enigne.runAndWait()


for i in range(n):
    wts += str(random.choice(words))
    wts += " "
wts = wts[:-1]
print(wts)


def voiceRec():
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source)
        Txt = r.recognize_google(audio2, language="ru-RU")
        Txt = Txt.lower()
        print(Txt)
        voice = Txt
        voice.replace('-',' ')
        print(voice)
        if voice == wts:
            tk.messagebox.showinfo("Аутентификация", "Пройдено")
        return Txt


def voiceWindow():
    voiceWin = Toplevel(root)
    voiceWin.title('Аутентификация по голосу')
    voiceWin.geometry("300x300")
    voiceWin.resizable(0, 0)
    getVoicePrompt()
    voicePrompt = tk.Label(voiceWin, textvariable=strVar)
    voicePrompt.pack()
    text = Text(voiceWin, font=12, height=3, width=30)
    text.pack()
    getVoiceBtn = tk.Button(voiceWin, text="Считать голос", command=voiceRec)
    getVoiceBtn.pack()
    usrVoice = tk.Label(voiceWin, textvariable=usrVar)
    usrVoice.pack()
    setVoiceBtn = tk.Button(voiceWin, text="Сравнить запись \n голоса ", command=setUsrVoice)
    setVoiceBtn.pack()


def getVoicePrompt():
    strVar.set(wts)


def setUsrVoice():
    usrVar.set(voice)


def appExit():
    root.destroy()


def emoRecog():
    test = os.system('python emoRecogV3.py')
    if test == 200:
        tkinter.messagebox.showinfo("Аутентификация", "Аутентификация пройдена!")


extBtn = Button(text="Выход", command=appExit)
extBtn.place(x=200, y=250)
btn2 = Button(compound="bottom", text="Пройти идентификацию и \n аутентфикацию \n по лицу и эмоции", command=emoRecog)
btn2.place(x=70, y=80)
voiceBtn = Button(compound="bottom", text="Пройти аутентификацию \n по голосу", command=voiceWindow)
voiceBtn.place(x=73, y=150)

root.mainloop()
