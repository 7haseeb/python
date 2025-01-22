# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:53:55 2025

@author: M Haseeb Shah
"""

class Car:
    
    def __init__(self,model,color,year,for_sale):
       self.model=model
       self.color=color
       self.year=year
       self.for_sale=for_sale
       print("data Processesing >>>>>")
       
        
        
    def drive(self):
        print(f"you drive the {self.model}")
    
    def stop(self):
        print(f"you stopped the {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
 
        
 
car1 = Car("Mustang","Black","1969",False)
car1.drive()
car1.stop()
car1.describe()