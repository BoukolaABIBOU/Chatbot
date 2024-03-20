# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 04:27:21 2022

@author: ABIBOU Boukola
"""

from tkinter import *
import datetime


root=Tk()

def envoi():
    envoi="Moi : " + e.get()
    txt.insert(END, "\n" + envoi) 
    if 'Bonjour' in e.get():
        txt.insert(END, "\n" + "Abibou:Bonjour,comment ça va? Comment puis-je vous aider?")
        
    elif 'heure' in e.get():
        heure=datetime.datetime.now().strftime("%H:%M")
        txt.insert(END, "\n" +"Abibou : Il est " +heure)
    
    elif 'nom' in e.get():
        txt.insert(END, "\n" +"Abibou : Je me nomme Abibou")
    
    elif 'appelles' in e.get():
        txt.insert(END, "\n" +"Abibou : Je me nomme Abibou")
        
    elif 'Abibou' in e.get():
        txt.insert(END, "\n" +"Abibou : Je suis un ChatBot")
        
    elif 'robot' in e.get():
        txt.insert(END, "\n" +"Abibou : Non, je suis un ChatBot")
        
    elif 'ChatBot' in e.get():
        txt.insert(END, "\n" +"Abibou : Les informaticiens m'appellent Chatbot, mais la plupart des autres me surnomme d' assistant virtuelle en ligne")
    
    else:
       txt.insert(END, "\n" +"Abibou: Désolé, mais je ne comprends pas.")
    
    
    e.delete(0,END)
    
    
    
txt=Text(root, font=("times new roman", 15))
txt.grid(row=0, column=0, columnspan=2)
e=Entry(root,width=100)
e.grid(row=1, column=0)
envoyer=Button(root, text="Envoyer", command=envoi).grid(row=1,column=1)

root.title("Abibou")
root.mainloop()