# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:43:57 2025

@author: M Haseeb Shah
"""

# List comprehension : A concise way to create lists in python
#                       compact and easier to read than traditional loops
#                       [expression for a value in iterable if condition]
"""                           Method 1
doubles = []
for x in range(1,11):
    doubles.append(x*2)
"""
"""                          Method 2
doubles = [x*2 for x in range(1,11)]  
print(doubles)
"""
"""
fruits = ["apple","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)"""
  
numbers =[1,-2,-3,4,-4,2,9]
pos_nums = [num for num in numbers if num >= 0] 
neg_nums = [nums for nums in numbers if nums< 0]
even_nums = [num for num in numbers if num %2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums) 