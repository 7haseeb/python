# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 22:16:08 2025

@author: M Haseeb Shah
"""

#---------------------------<temperature converter>--------------------------

temp = float(input("Enter the temperature : "))
unit = input("Is this temperature is in celsius or fahrenheit (C/F) ? : ")

if unit == "C" :
    temp = round(((9 * temp)/5 +32),1)
    print(f"The temp in fahrenheit is {temp} f")
elif unit == "F" :
    temp = round(((temp-32)*5/9),1)
    print(f"The temp in celsius is {temp} C")
else:
    print(f"{unit} is an invalid unit.")