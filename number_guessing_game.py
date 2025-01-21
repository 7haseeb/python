# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:01:47 2025

@author: M Haseeb Shah
"""

import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print("--------------Welcome-------------")
print(f"Select a number between {low} and {high} ")

while is_running :
    guess = input("Enter your guess : ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        
        if guess < low or guess > high:
            print("That nummber is out of range")
            print("Enter a valid number : ") 
        elif guess < answer :
            print("Too low! try again")
        elif guess > answer :
            print("Too high! try again")
        else :
            print(f"Correct the answer was : {answer}")
            print(f"The nummber of guesses you take : {guesses}")
            is_running = False
            
    else :
        print("Invalid guess")