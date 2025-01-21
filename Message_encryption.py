# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:29:48 2025

@author: M Haseeb Shah
"""

import string
import random

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)
"""
print(f"Chars : {chars}")
print(f"Keys : {keys}")
"""
#Encryption
plain_text = input("Enter a mesage to encrypt : ")
cipher_text = ""

for letter in plain_text :
    index = chars.index(letter)
    cipher_text += keys[index]
    
print(f"orignal message : {plain_text}")
print(f"Encrypted message :{cipher_text}")

#DECryptting
cipher_text = input("Enter a  encrypted mesage : ")
plain_text = ""

for letter in cipher_text :
    index = keys.index(letter)
    plain_text += chars[index]
print(f"Encrypted message :{cipher_text}")   
print(f"orignal message : {plain_text}")
