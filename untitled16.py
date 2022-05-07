#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:08:55 2022

@author: riddhiekajain
"""

dictionary = {"fruit": "mango", "color": "pink", "bird": "sparrow"}
try:
   print(dictionary["animal"])
except(KeyError):
    print("key animal is not present in dictionary")
