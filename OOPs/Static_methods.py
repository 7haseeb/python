# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:17:39 2025

@author: M Haseeb Shah
"""

#Static methods : A method that belong to a class rather than any object from that class(instance
#                  usually used for genreal utility funtions ).
#Instance methods : Best for operrations on intances of class(objects)
#Static methods   : BEST for utility funtions that do not need access to class data.

class Employee : 
    def __init__(self,name,position):
        self.name =name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    
    @staticmethod
    def is_valid_position(position):
         valid_positions = ["Manager","Cashier","Cook","Janitor","The king in the north"]
         return position  in valid_positions
     
employee1 = Employee("John Snow", "The king in the north")
employee2 = Employee("HASEEB", "MANAGER")
print(employee1.get_info())
print(employee2.get_info())
print(Employee.is_valid_position("Cook"))
