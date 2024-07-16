# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:42:10 2024

@author: occup
"""

from tkinter import *
root = Tk()
root.geometry("1000x500")
root.title("Shopping List")

label_country = Label(root)
label_city = Label(root)


entry_country = Entry(root)
entry_city = Entry(root)


list_1 = []
list_city = []

def add_country():
    
        country_name = entry_country.get()
        list_1.append(country_name)
        label_country ["text"] = "Country list : " +  str(list_1)
        i = i - 1

  
def add_city():
    city_name = entry_city.get()
    list_city.append(city_name)
    label_city ["text"] = "City list  : " + str(list_city)
    

btn2 = Button(root, text = "Add country", command = add_country)
btn = Button(root, text = "Add city", command = add_city)

entry_country.place(relx = 0.5, rely = 0.2,  anchor = CENTER)
btn2.place(relx = 0.5, rely = 0.3,  anchor = CENTER)
entry_city.place(relx = 0.5, rely = 0.4,  anchor = CENTER)
btn.place(relx = 0.5, rely = 0.5,  anchor = CENTER)
label_city.place(relx = 0.5, rely = 0.6,  anchor = CENTER)
label_country.place(relx = 0.5, rely = 0.7,  anchor = CENTER)
root.mainloop()