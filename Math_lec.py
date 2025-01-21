# -*- coding: utf-8 -*-
import math
"""
Created on Wed Jan  8 23:56:22 2025

@author: M Haseeb Shah
"""

#Airthmetics and Math functios.
#Augmented Assignment operators +=, -=, *=, /=, **= (num**=2 means num^num)
# % modulas(it give us reminder) ceil() always roundup floor() always rounddown
friends = 4


#friends = friends +1
#friends +=1

#friends = friends -1
#friends -=1

#friends = friends *3
#friends *=3


#friends = friends /2
#friends /=2

#friends **=2;

#friends %=3

#print(friends)

#print(round(67.88))
#print(abs(-88))
#print(pow(3,3))
#print(max(67,99))
#print(min(55,-9,6))

#print(math.pi)
#print(math.e)
#print(math.sqrt(64))
#print(math.ceil(9.1))
#print(math.floor(9.99))

r = float(input("Enter the radius of the circle : "))
circumference = 2 * math.pi* r
area = math.pi*pow(r,2)
print(f"the circle's circumference will be : {round(circumference)} cm")
print(f"the circle's area will be : {round(area)} cm_sq")

base = float(input("Enter the length of side A (base) : "))
perp = float(input("Enter the length of side B (perpendicular) : "))
hyp_s = pow(base,2)+pow(perp,2)
hyp = math.sqrt(hyp_s)
print(f"Hypotenous will be : {hyp}")