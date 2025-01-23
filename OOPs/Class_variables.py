# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:39:36 2025

@author: M Haseeb Shah
"""

class Student :
    
    class_year = 2027
    num_of_stu = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_of_stu += 1
    
    
student1 = Student("Haseeb",19)
student2 = Student("Ahsan", 21)
student3 = Student("Sufi",18)
student4 = Student("Shakir",22)
"""
print(f"{student1.name} {student1.age} {Student.class_year}")
print(f"{student2.name} {student2.age} {Student.class_year}")
"""
print(f"my graduating class of {Student.class_year} has {Student.num_of_stu} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)S