#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:28:01 2022

@author: riddhiekajain
"""

from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("600x400")


list_name = ["Mickey mouse", "Elsa", "Anna", "Donald duck"]
dict_student = {"name" : "Shinchan",
                "age": "5"}
try:
    print(list_name[5])
  
    print(dict_student["mom"])
    
except IndexError :
        messagebox.showinfo("Error", "This index does not exist")
except KeyError :
        messagebox.showinfo("Error", "This key does not exist")
    
root.mainloop()