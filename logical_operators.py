# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 22:36:32 2025

@author: M Haseeb Shah
"""

#logical operators  or, and, not
# ex1

#temp = 25
#isRainging =False

#if temp>=35 or isRainging:
#    print("Iam not going outside ")
#else:
#   print("yes iam going out")
    
# EX-2
temp = 0
is_sunny = False
if temp>=28 and is_sunny :
    print("It is very Hot Outside")
    print("It is sunny")
elif temp<=0 and is_sunny :
    print("It is cold outside")
    print("Its sunny ")
elif 28 > temp > 0 and is_sunny :
    print("it is warm outside")
    print("it is sunny")
elif temp>=28 and not is_sunny :
    print("It is very Hot Outside")
    print("It is cloudy")
elif temp<=0 and not is_sunny :
    print("It is cold outside")
    print("Its cloudy ")
elif 28 > temp > 0 and not is_sunny :
    print("it is warm outside")
    print("it is cloudy")