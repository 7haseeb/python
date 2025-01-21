# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:28:07 2025

@author: M Haseeb Shah
"""

#--------------------------<PYTHON-CALCULATOR>-------------------------------
operator = input("Select the operater (+,-,*,/) : ")
num1 = float(input("Enter the first number :  "))
num2 = float(input("Enter the second number : "))

if operator == "+":
    result = num1+num2
    print(round(result,3))
elif operator == "-":
    result = num1-num2
    print(round(result,3))
elif operator == "*" :
    result = num1*num2
    print(round(result,3))
elif operator =="/" :
    result = num1/num2
    print(round(result,3))
else :
    print(f"{operator} is not valid operator")