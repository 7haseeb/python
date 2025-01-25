# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 20:12:44 2025

@author: M Haseeb Shah
"""

#Magic methods : DUNDER methods (double underscore) __init__ , __str__ , __eq__
#                They are automatically called by many python's buit-in operations
#                   they allow developers to define or customize the behaviour of objects.

class Student:
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        
        
    def __str__(self):
        return f"name : {self.name} gpa : {self.gpa}"
    
    def __eq__(self,other):
        return self.name == other.name
    
    def __gt__(self,other):
        return self.gpa == other.gpa
    
    
student1 = Student("HASEEB", 3.6)
student2 = Student("SUFI", 3.9)
student3 = Student("Vishal", 3.4)

print(student1)

print(student1 == student2)    

print(student1 > student2)    