# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:59:28 2025

@author: M Haseeb Shah
"""

#intrest calculator..

principle = 0
rate = 0
time = 0

while principle <=0 : 
    principle = float(input("Enter the principle amount : "))
    if principle <=0 :
        print("Principle amount can't be lesser than or equal to zero ")
        
while rate <=0 : 
    rate = float(input("Enter the intrest rate  : "))
    if rate <=0 :
        print("intrest rate can't be lesser than or equal to zero ")

while time <=0 : 
    time = int(input("Enter the time in years  : "))
    if time <=0 :
        print("Time can't be lesser than or equal to zero ")

        
total = principle *pow((1 +rate / 100),time)
print(f"Balance after {time} year/s : ${total:.2f}") 