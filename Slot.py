# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:04:20 2025

@author: M Haseeb Shah
"""
import random

def spin_row():
    symbols = ["🍒"," 🍉", "🍋"," 🔔" ,"🌟"]
    #results = []
    
    #for symbol in range (3):
        #results.append(random.choice(symbols))
    return [random.choice(symbols) for _ in range(3)]
        

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")
def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif row[0] == "🍉":
            return bet*4
        elif row[0] == "🍋":
            return bet*5
        elif row[0] == "🔔":
            return bet*10
        elif row[0] == "🌟":
            return bet*20
    return 0
        


def main():
    balance = 100
    print("*************************")
    print("Welcome to casino royale")
    print("Symbols : 🍒 🍉 🍋 🔔 🌟")
    print("*************************")

    while balance > 0 :
        print(f"Current balance : ${balance}")
        
        bet = input("Place your bet amount : $")
        
        if not bet.isdigit():
            print("please enter a valid number")
            continue
        bet = int(bet)
        if bet > balance :
            print("Insufficient funds")
            continue
        if bet <=0 :
            print("Bet must be greater than zero")
            continue
            
        balance -= bet 
        
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        payout = get_payout(row,bet)
        
        if payout > 0 :
            print(f"You won ${payout:.2f}")
        else :
            print("Sorry you lose..")
            
        balance += payout
 
        play_again = input("Do you want to play again (Y:N): ").upper()
        if play_again != "Y":
            break
    print("***********************************************")
    print(f"Game is over your final balance is :${balance}")
    print("***********************************************")
if __name__  == "__main__":
    main()