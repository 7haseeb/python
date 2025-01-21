# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:46:02 2025

@author: M Haseeb Shah
"""

#Nested loop : A loop within another loop

rows = int(input("Enter the number of rows : "))
cols = int(input("Enter the number if columns : "))
symbol = input("Enter a symbol to use : ")


for i in range (rows):
    for j in range (cols):
        print(symbol, end="")
    print()        
