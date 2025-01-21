# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:00:37 2025

@author: M Haseeb Shah
"""

def show_balance(balance):
    print("**************************")
    print(f"Your balannce is ${balance:.2f}")
    print("**************************")

def deposite(balance):
    print("**************************")
    amount = float(input("Enter the amount to be deposited : $"))
    print("**************************")
    
    if amount <= 0:
        print("**************************")
        print("Thats not a valid amount")
        print("**************************")
    else:
        return amount

def withdraw(balance):
    print("**************************")
    amount = float(input("Enter the amount to be withdraw : $"))
    print("**************************")
    
    if amount > balance :
        print("**************************")
        print("Insufficient funds : ")
        print("**************************")
        return 0
    elif amount < 0 :
        print("**************************")
        print("Amount must be greater than zero")
        print("**************************")
        return 0
    else :
        return amount
    

def main():
    balance = 0
    is_running = True
    
    while is_running :
        print("**************************")
        print("      Banking Program     ")
        print("**************************")
        print("1. Show balance")
        print("2. Deposite")
        print("3. Withdraw")
        print("4. Exit")
        print("**************************")
        choice = input("Enter your choice (1-4) : ")
        
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposite(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else :
            print("**************************")
            print("This is not a valid choice.")
            print("**************************")
            
    print("**************************")       
    print("Thank you have a nice day.")
    print("**************************")
            
    
if __name__ == "__main__":
    main()
        