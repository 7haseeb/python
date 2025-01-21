# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:24:38 2025

@author: M Haseeb Shah
"""

# Functions : 
    
    
"""    
def display_info(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")
    
display_info("Haseeb", 25.78, "12-3-2025")
"""
"""
def is_even(num):
    return num % 2 == 0

print(is_even(5))
print(is_even(4))
"""

"""
def add(a,b):
    return a + b


print(f"Sum of 10 + 19 is {add(10,19)}")
"""

def  create_name(first,last):
    first =  first.capitalize()
    last = last.capitalize()
    return first+last

first = "haseeb"
last = "shah"
print(f"Name : {create_name(first,last)}")