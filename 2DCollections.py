# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:08:25 2025

@author: M Haseeb Shah
"""

#2D COLLECTIONS --- 2D LISTS

fruits = ["Apple","Orange","Grapes","Banana"]
vagetables = ["Potatoes","carrots","Onion"]
meats = ["Chicken","Fish","Turkey"]

groceries = [fruits,vagetables,meats]

#print(groceries)
"""
for colletion in groceries:
    print(colletion)             here we iterate through rows
"""
"""
for colletion in groceries :
    for food in colletion  :
        print (food, end=" ")
    print()
"""
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for row in num_pad :
    for num in row :
        print(num , end=" ")
    print()