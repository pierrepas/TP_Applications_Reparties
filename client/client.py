#!/usr/bin/env python3
# -*- coding: utf-8 -*
from tkinter import *


class GUI_SNCF:

    def __init__(self, master):
        self.master = master
        master.title("Trouves Ton Train!")

        self.label = Label(
            master, text="  La SNCF vous souhaite bienvenue!  ")
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
        try:
            print("Coordonnées ville 1: Latitude = ", float(
                self.lat1.get()), " Longitude = ", float(self.long1.get()))
            print("Coordonnées ville 2: Latitude = ", float(
                self.lat2.get()), " Longitude = ", float(self.long2.get()))
            print("Envoi des donnees au serveur...")
            print("Désolé, la SNCF n'a pas encore implemente cette fonction")
        except:
            print("Veuillez entrer des coordonnées valides, petit malin!")
        print("")



root = Tk()
g = GUI_SNCF(root)
root.mainloop()
