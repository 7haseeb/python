# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:44:34 2025

@author: M Haseeb Shah
"""

#conditional expressions (Ternary operators)
# X if condition else Y
# one line short cut for if else statements
num = 7
result = "Positive" if num>0 else"Negative"
print(f"{result}")
print("even" if num % 2 == 0 else "Odd")
a = 6
b = 7
max_num = a if a>b else b
min_num = a if a<b else b
print(f"Max number is {max_num}")
print(f"Min number is {min_num}")

temp =30
weather = "Hot" if temp> 25 else "Cold"
print(f"Weather is {weather}")