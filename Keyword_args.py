# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:16:50 2025

@author: M Haseeb Shah
"""

#keyword arguments

"""
def hello(greetings,title,first,last):
    print(f"{greetings} {title} {first} {last} ")
    
    
    
hello("hello", first="hhaseeb" , title="mr", last= "shah")"""

def get_phone(country,area,first,last):
    return f"{country}{area}-{first}{last}"

print(get_phone("+92",area="305",first="1799",last="209"))