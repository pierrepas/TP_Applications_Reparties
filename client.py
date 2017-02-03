#!/usr/bin/env python
# -*- coding: utf-8 -*
from tkinter import *


class GUI_SNCF:

    def __init__(self, master):
        self.master = master
        fm = Frame(master)
        master.title("Trouves Ton Train!")

        self.label = Label(
            fm, text="   La SNCF vous souhaite bienvenue!   ")
        self.label.pack()
        self.lV1 = Label(master, text="Ville 1:")
        self.lV2 = Label(master, text="Ville 2:")

        self.lat1 = Entry(master)
        self.lat1.insert(0, "45.5646")
        self.long1 = Entry(master)
        self.long1.insert(0, "5.9178")

        self.lat2 = Entry(master)
        self.lat2.insert(0, "45.8992")
        self.long2 = Entry(master)
        self.long2.insert(0, "6.1294")


        self.lV1.pack()
        self.lat1.pack()
        self.long1.pack()
        self.lV2.pack()
        self.lat2.pack()
        self.long2.pack()
        self.calc_button = Button(
            master, text="Calculer la distance", command=self.calculDist)
        self.calc_button.pack(fill=X)

        self.close_button = Button(master, text="Quitter", command=master.quit)
        self.close_button.pack(fill=X)

    def calculDist(self):
        print("Envoi des données au serveur...")
        print("Désolé, la SNCF n'a pas encore implémenté cette fonction")

root = Tk()
g = GUI_SNCF(root)
root.mainloop()
