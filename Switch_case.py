# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:29:40 2025

@author: M Haseeb Shah
"""

#Match-case Statements : An alternative of using many 'elif' statements
#                       execute some code if a value matches a 'case'
"""
def day_of_week(day):
    if day == 1:
        print("its monday")
    elif day == 2:
        print("its tuesday")
    elif day == 3:
        print("its wednesday")
    elif day == 4:
        print("its thursday")
    elif day == 5:
        print("its friday")
    elif day == 6:
        print("its saturday")
    elif day == 7:
        print("its sunday")
    else :
        print("Invalid day")
"""
def day_of_week(day):
    match day:
        case 1:
            print("its monday")
        case 2:
            print("its tuesday")
        case 3:
            print("its wednesday")
        case 4:
            print("its thursday")
        case 5:
            print("its friday")
        case 6:
            print("its saturday")
        case 7:
            print("its sunday")
        case _ :
            print("Invalid day")   
            
def is_weekend(day):
    match day:
        case "Saturday"|"Sunday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case _ :
            return False

print(is_weekend("Sunday"))