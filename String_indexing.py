# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:13:52 2025

@author: M Haseeb Shah
"""

#indexing = accessing elements of a sequence usinig [] (indexing operator)
#[Start : end : step]
#negative index strats from back 
credit_number = "1234-5678-9012-3456"
#print(credit_number[0:4])
#print(credit_number[5:])
#print(credit_number[::2])
last_digits = credit_number[-4::1]
print(last_digits)
reversenums = credit_number[::-1]
print(reversenums)