# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:39:23 2025

@author: M Haseeb Shah
"""

#--------------------------------<TYPE-CASTING>------------------------------
#Typecasting: the process of converting a variable from one data type to other
#typecast funtions str(), int(), float(), bool()
#if we convert a string to boolean it always give True.
name = "Haseeb"
age = 21
cgpa = 3.62
is_stu = True

print(type(cgpa))
print(f"CGPA intially : {cgpa}")
cgpa = int(cgpa)
print(type(cgpa))
print(f"CGPA after typecasting into Int : {cgpa}")



print(type(age))
print(f"your age INT : {age}")
age = float(age)
print(type(age))
print(f"your age Float : {age}")


print(type(age))
print(f"your age float : {age}")
age = str(age)
print(type(age))
print(f"your age string : {age}")

