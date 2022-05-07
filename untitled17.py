#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:20:17 2022

@author: riddhiekajain
"""

mylist = [10, 20, 30, 40]
try:
   print(mylist[5])
except IndexError:
    print("Index out of range")