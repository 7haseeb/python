# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:47:40 2025

@author: M Haseeb Shah
"""

#format spacifiers = {value : flags} format a value on what flags are inserted

#.(number)f = round to that  many decimal places (fixed points)
# :(number) = allocate that  many spaces
#  :03 = allocate and zero pad that many spaces
# :< = justify left
# :> = justify right
# :^ = center align
# :+ = use a plus sign to indicate positive value
# :- = use a minus sign to indicate negative value
# := = place a sign to the leftmost position
# :  = place a space before positive numbers
# :, = comma seprator

#EX--1
price1 = 3765.14159
price2 = 67455.897798
price3 = 57876.3457

print(f"{price1:.2f}")
print(f"{price2:.2f}")
print(f"{price3:.2f}")

print(f"{price1:10}")
print(f"{price2:10}")#10 spaces reserved for each num
print(f"{price3:10}") 

print(f"{price1:010}")
print(f"{price2:010}")#each num is 0-padded 
print(f"{price3:010}")

print(f"{price1:<10}")
print(f"{price2:<10}")#eachnumber is now  left  justified
print(f"{price3:<10}")

print(f"{price1:>10}")
print(f"{price2:>10}")#eachnumber is now  right  justified
print(f"{price3:>10}")

print(f"{price1:+}")
print(f"{price2:+}")# places + sign in front  of positive numbers
print(f"{price3:+}")

print(f"{price1:+,.2f}")
print(f"{price2:+,.2f}")
print(f"{price3:+,.2f}")

print(f"{price1:^10}")
print(f"{price2:^10}")#justifies to center
print(f"{price3:^10}")