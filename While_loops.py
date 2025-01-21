# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:28:37 2025

@author: M Haseeb Shah
"""

#while loop = execute some code while some condition remains true.
#EX-1
"""name = input("Enter your name : ")
while name == "" :
    print("You did not enter your name ")
    name = input("Enter your name : ")
print(f"Hello {name}")"""

#EX-2
"""
age = int(input("Enter your age : "))

while age<0 :
    print("Age can't be negative : ")
    age = input("reenter your age : ")
print(f"you are {age} years old ")
"""
food = input("Enter a food you like (q to quit) : ")
 
while not food == "q" :
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit) : ")
print("Bye")