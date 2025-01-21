# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:01:53 2025

@author: M Haseeb Shah
"""

import time

my_time = int(input("Enter the time in secs :"))

 # delay the execution for given secs
"""
for x  in range (0,my_time):
    print(x)
    time.sleep(1)

print("Times up")
"""

for x in range (my_time,0,-1) :
    secs = x % 60 
    mins = int( x/60 ) % 60
    hours = int (x/3600) % 24
    
    print(f"{hours:02} : {mins:02} : {secs:02}")
    time.sleep(1)

print("times up")    
