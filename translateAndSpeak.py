from tkinter import *
import os
from gtts import gTTS
import pyttsx3
from englisttohindi.englisttohindi import EngtoHindi

root = Tk()
root.resizable(False, False)


def removeWidgets():
    frame1.destroy()
    frame2.destroy()


def back():
    frame3.destroy()
    frame4.destroy()
    mainPage()


def mainPage():
    global frame1
    frame1 = Frame(root, bg="black", height="150")
    frame1.pack(fill=X)
    global frame2
    frame2 = Frame(root, bg="brown", height="750")
    frame2.pack(fill=X)

    label = Label(frame1, text="Welcome", font="bold, 30", bg="brown")
    label.place(x=230, y=70)

    btn = Button(frame2, text="TEXT TO SPEECH", width="18", pady=12,
                 font="bold, 15", command=textToSpeech, bg='yellow')
    btn.place(x=130, y=130)

    btn = Button(frame2, text="TRANSLATE", width="18", pady=12,
                 font="bold, 15", command=translate, bg='yellow')
    btn.place(x=350, y=130)


def textToSpeech():
    removeWidgets()
    global frame3
    frame3 = Frame(root, bg="black", height="150")
    frame3.pack(fill=X)
    global frame4
    frame4 = Frame(root, bg="brown", height="750")
    frame4.pack(fill=X)

    label = Label(frame3, text="ENTER A TEXT", font="bold, 30", bg="brown")
    label.place(x=180, y=70)

    entry = Entry(frame4, width=45, bd=4, font=14)
    entry.place(x=130, y=52)
    entry.insert(0, "")

    def play():
        language = "hi"
        english = entry.get()
        res = EngtoHindi(english)
        a = res.convert
        print(a)
        myobj = gTTS(text=a, lang=language, slow=False)
        myobj.save("convert.wav")
        os.system("convert.wav")

    def Reset():
        entry.delete(0, END)

    btn = Button(frame4, text="SPEAK IN HINDI", width="15", pady=12,
                 font="bold, 15", command=play, bg='yellow')
    btn.place(x=130, y=130)

    btn = Button(frame4, text="RESET", width="15", pady=12,
                 font="bold, 15", command=Reset, bg='yellow')
    btn.place(x=370, y=130)

    btn = Button(frame4, text="Back", width="5", pady=12,
                 font="bold, 15", command=back, bg='yellow')
    btn.place(x=0, y=10)


def translate():
    def play():
        # language = "hi"
        english = entry.get()
        res = EngtoHindi(english)
        a = res.convert
        translateBox.insert(END, a)
        entry.delete(0, END)
        # myobj = gTTS(text=a, lang=language, slow=False)
        # myobj.save("convert.wav")
        # os.system("convert.wav")

    removeWidgets()
    global frame3
    frame3 = Frame(root, bg="black", height="150")
    frame3.pack(fill=X)
    global frame4
    frame4 = Frame(root, bg="brown", height="750")
    frame4.pack(fill=X)

    label = Label(frame3, text="ENTER A TEXT", font="bold, 30", bg="brown")
    label.place(x=180, y=70)

    entry = Entry(frame4, width=46, bd=4, font=14)
    entry.place(x=130, y=52)
    entry.insert(0, "")

    btn = Button(frame4, text="Translate In Hindi", width="15", pady=12,
                 font="bold 15", command=play, bg='yellow')
    btn.place(x=250, y=250)

    translateBox = Listbox(frame4, height=5, width=38,
                           bg="white", font="bold 15")
    translateBox.place(x=130, y=100)

    btn = Button(frame4, text="Back", width="5", pady=12,
                 font="bold, 15", command=back, bg='yellow')
    btn.place(x=0, y=10)


mainPage()
root.title("text_to_speech_convertor")
root.geometry("700x500")
root.mainloop()
