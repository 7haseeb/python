# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:44:40 2025

@author: M Haseeb Shah
"""

#Class methos : Allows operations related to class itself.
#               TAKE (cls) as a first parameter , which represents the class itself.
#               BEST for class level data or required access to the class itself.


class Student : 
    
    count = 0
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa  = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
        
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def  get_count(cls):
        return f"Total # of students : {cls.count}"       
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else :
            return f"AVERAGE GPA : {cls.total_gpa/cls.count:.2f}"
    
    
s1 = Student("Haseeb", 3.6)
s2 = Student("SUFI", 3.9)  
s3 = Student("Vishal",3.2)

print(s1.get_info())
print(s2.get_info())
print(Student.get_count())
print(Student.get_avg_gpa())