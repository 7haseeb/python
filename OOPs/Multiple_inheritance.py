# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:37:48 2025

@author: M Haseeb Shah
"""

#Multiple inheritance : inherit from more than one parent class.
#                        c(a,b)
#Multilevel inheritance : inherit from a parent which inherits from another parent
#                        c(b)<- b(a)<-a

class Animal:
    def __init__(self,name):
        self.name =name
    def sleep(self):
        print(f"{self.name} is sleeping")
    def eat(self):
        print(f"{self.name} is eating")
        


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
    
        
        
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Falcon")
fish = Fish("Nemo")

rabbit.flee()
rabbit.eat()
rabbit.sleep()
hawk.hunt()
fish.flee()
fish.hunt()