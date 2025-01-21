# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:45:41 2025

@author: M Haseeb Shah
"""

import random

options =  ("rock","paper","Scissors")
cards = ["2","3","4","5","Q","K","J"]

#num = random.randint(1, 20)#returns a random number bw  given range.
#num = random.random()#returns a number bw zero and one
option = random.choice(options)# choice fuction chooses a random from given option 
random.shuffle(cards)#shuffle the sequence of elements in a collection
print(cards)
print(option)