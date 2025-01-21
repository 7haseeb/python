# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:39:04 2025

@author: M Haseeb Shah
"""

#---------------------------------------<SHOPING-CART>---------------------------------------------------
foods = []
prices = []
total = 0

while True :
    food = input("Enter a food item to buy (Q to quit) :")
    if food.upper() == "Q" :
        break
    else :
        price = float(input(f"Enter the price of {food} : $"))
        foods.append(food)
        prices.append(price)
        

print("----------YOUR-CART-----------")

for food in foods : 
    print(food,end=" ")
    
for price in prices : 
    total+=price
print(end="\n")
print(f"Your total bill is : ${total}")