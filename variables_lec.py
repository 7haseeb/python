# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:00:26 2025

@author: M Haseeb Shah
"""

#this is my second python program..

#strings
first_name = "haseeb"
food = "biryani"
email = "haseeb123@gmail.com"

#Integers

age = 21
quantity = 3
num_of_stu =34

#float
price = 199.57
cgpa =3.62
distance = 5.9

#boolean
is_stu = True
for_sale =False
is_online = True

print(first_name)
print(f"Hello {first_name }")
print(f"your fvrt food is {food}")
print(f"your email is {email}")
print(f"you are {age} years hold")
print(f"your class has {num_of_stu} students")
print(f"you are buying {quantity} items")
print(f"the price is {price} ruppes")
print (f"your CGPA is {cgpa}")
print(f"you ran {distance} kilometers")
#print(f"are you a student ? : {is_stu}")
if is_stu :
    print("you are a student")

if for_sale :
    print("This item is for sale")
else:
    print("This item is not for sale")

if is_online :
    print("You are Online")
else:
    print("You are Offline")    