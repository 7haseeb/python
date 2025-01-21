# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:12:27 2025

@author: M Haseeb Shah
"""

#Strings
#.find() finds the first aaccourance of a letter in a string
#.rfind() finds the last accourance of a letter in a String
#.capitalize() capitalize the first letter of the stirng
#.upper() convert the whole letters in uppercase
#.lower() convert the whole letters in lowercase
#.isdigit() and .isalpha() return true if string has all letters or numbers
#.count() counts the accourance of a character in a string
#.replace() replaces a char with another within a String
#name = input("Enter your full name : ")
#result = len(name)
#print(f" {result}")
#print(name.find(" "))
#name = name.capitalize()
#print(f"{name}")
#name = name.upper()
#print(f"{name}")
#name = name.lower()
#print(f"{name}")
#rslt = name.isdigit()
#print(f"{rslt}")
#rslts = name.isalpha()
#print(f"{rslts}")
#print(name.count("a"))
#print(name.replace("a","e"))

# Validate user input exersize
# username is no more than 12 characters 
# username must not contains space
# username must not contains any digits

username = input("Enter username : ") 
result = len(username)
if result > 12:
    print("your username can't be more than 12 characters.")
elif  not username.find(" ") == -1:
    print("your username can't contain space")
elif not username.isalpha():
    print("your username can't contain numbers")
else : 
    print(f"Welcome {username}")
























