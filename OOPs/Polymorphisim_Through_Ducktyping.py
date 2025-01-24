# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:19:39 2025

@author: M Haseeb Shah
"""

#Duck typing : Another way to achieve polymorphism besides inheritance
#              object must have the minimum necessary attributes / methods
#               "IF IT LOOKS LIKE A DUCK AN QUACKS LIKE A DUCK ,IT MUST BE A DUCK"

class Animal :
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("BOW .... BOW")
        
class Cat(Animal):
    def speak(self):
        print("MEOW...Meow")
        
class Car:
    alive  = False
    def speak(self):
        print("Honk")
        
        
animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)