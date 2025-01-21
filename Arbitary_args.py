# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:56:35 2025

@author: M Haseeb Shah
"""

"""
*args== allows you to pass multiple  non key arguments
**Kwargs==allows you to pass multiple keyword arguments
* is an unpacking operators
""" 
"""
def add(*args):
    total =  0
    for x in args:
        total += x
    return total

print(add(1,6,9,7 ))"""
"""
def display(*args):
    for arg in args:
        print(arg, end=" ")
    
display("Haseeb","Shah","Rashdi")"""
"""
def display_address(**kwargs):
    for keys,value in kwargs.items() :
        print(f"{keys} : {value}")
        
        
display_address(street = "123-fake street",
                aprt = 109, 
                city = "pir-jo-goth",
                district="khairpur",
                province="sindh")
"""
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end = " ")
    print()
    for keys,value in kwargs.items() :
        print(f"{keys} : {value}")  
    



shipping_label("Mr.","Haseeb","Shah","Rashdi",
               street = "123-fake street",
               aprt = 109, 
               city = "pir-jo-goth",
               district="khairpur",
               province="sindh"
               )
