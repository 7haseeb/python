# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:16:23 2025

@author: M Haseeb Shah
"""
from math import e
#Variable Scope : Where a variable is visible and accessible 
#Scope resolution : (LEGB) local ->enclosed ->global ->built-in
"""
def fun1():
    a = 1       # here a local to fun1 and has no relation with fun2
    print(a)
                                Example of local variables
def fun2():
    a = 2       # here a local to fun2 and has no relation with fun1
    print(a)
"""
"""
x = 99

def fun1():
    print(x)
def fun2():           Exampels of Global varialbe
    print(x)
"""
def fun1():
    print(e)       #"""Example of Built-in methods """

fun1()
