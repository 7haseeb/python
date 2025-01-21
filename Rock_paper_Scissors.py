# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:26:16 2025

@author: M Haseeb Shah
"""
import random
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Rock-Paper-Scissors<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
options = ("Rock","Paper","Scissors")
player = None
computer = random.choice(options)
running = True

while running : 

    player = None
    computer = random.choice(options)
    while player not in options :
        player = input("Enter a choice (Rock,Paper,Scissors) : ")
        
        
    print(f"Player :  {player}")
    print(f"Computer : {computer}")
    
    if player==computer :
        print("Its a tie,")
    elif player =="Rock" and computer =="Scissors" :
        print("You win")
    elif player =="Paper" and computer =="Rock" :
        print("You win")
    elif player =="Scissors" and computer =="Paper" :
        print("You Win")
    else :
        print("You LOSE")
        
    if not input("Play again ? (Y or N)").upper() =="Y":
        break
        running =False
    
    
print("Thanks for playing")