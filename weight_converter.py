# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:43:16 2025

@author: M Haseeb Shah
"""

#-----------------------------<Wigth-converter>------------------------------

weight = float(input("Enter your wight : "))
unit = input("Kilograms or pounds? (K or L) : ")

if unit == "K" :
    weight = weight * 2.205
    unit = "LBS"
    print(f"your weight is : {round(weight,3)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit= "Kgs"
    print(f"your weight is : {round(weight,3)} {unit}")
else :
    print(f"{unit} is not a valid unit.")

