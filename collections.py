# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:01:06 2025

@author: M Haseeb Shah
"""

# Collection = single "Variable" used to store multiple values.
# list = [] ordered and changeable . Duplicate OK
# Set =  {}  unorderd and immutable , Add and remove ok but no duplicates.
# Tuple = () ordered and unchangeable , Duplicates ok And Faster
"""
fruits = ["Apple", "Banana","Lemon","Orange"]
print(fruits)

for fruit in fruits :
    print(fruit ,end=" ")

#print(dir(fruits))  # prints all the functions of the collections.
#print(help(fruits)) # descripstions of all the functions of collections.
#print(len(fruits))
#print("Apple" in fruits )
#fruits[0] = "Pineapple"
fruits.append("Pineapple")#                 LISTS
fruits.remove("Lemon")
fruits.insert(0,"Grapes")
fruits.sort()
fruits.reverse()
print(fruits.index("Banana"))
fruits.clear()
print(fruits)
"""
"""
fruits = {"Apple", "Banana","Lemon","Orange"}
print(fruits)
print(len(fruits))
print("Apple" in fruits )
fruits.remove("Lemon")
fruits.pop()                         SETS
fruits.clear()
print(fruits)
"""



fruits = ("Apple", "Banana","Lemon","Orange")
print(fruits)
print(len(fruits))
print("Lemon" in fruits )
print(fruits.index("Apple"))
print(fruits.count("Orange"))

for fruit in fruits :
    print(fruit, end = " ")














