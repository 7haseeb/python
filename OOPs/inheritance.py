# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:00:50 2025

@author: M Haseeb Shah
"""

class Animal :
    
    def __init__(self,name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is asleep")
        
        
class Dog(Animal):
    def speak(self):
        print("WOOOW...WOOW")

class Cat(Animal):
    def speak(self):
        print("meow....meow")

class Mouse(Animal):
    def speak(self):
        print("Sqeek....sqeek")


dog = Dog("BoB")
cat = Cat("Tom")
mouse = Mouse("jerry")

print(dog.name)
print(cat.name)
print(mouse.name)

dog.eat()
cat.eat()
mouse.eat()


dog.sleep()
cat.sleep()
mouse.sleep()

dog.speak()
cat.speak()
mouse.speak()