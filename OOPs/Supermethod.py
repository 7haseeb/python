# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:34:41 2025

@author: M Haseeb Shah
"""

# super() : Function used in child class to call the methods from a parent class(super class) 
#           Allows you to extend the funtionality of the inherited class

class Shape :
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled
    
    def describe(self):
        print(f"It is {self.color} and {'Filled' if self.filled else 'NOT FILLED'}")
        
        
"""
class Circle(Shape):
    def __init__(self,color,filled,radius):
        self.color = color
        self.filled = filled
        self.radius = radius
class Square(Shape):
    def __init__(self,color,filled,width):
        self.color = color
        self.filled = filled
        self.width = width
class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        self.color = color
        self.filled = filled
        self.width = width
        self.height = height
"""  
class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius  
        
    def describe(self):
        print(f"It is a circle with an area of {3.14159 * self.radius * 2}")
        super().describe()
        
class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width = width
    
        
    def describe(self):
        print(f"It is a SQUARE with an area of {self.width**2}")
        super().describe()
        
class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width = width
        self.height = height
        
        
    def describe(self):
        print(f"It is a TRIANGLE with an area of {self.width* self.height / 2}")
        super().describe()
        
circle = Circle("Red", True, 6)
square = Square("green", False, 6)
triangle = Triangle("PURPLE", True, 13, 35)
print(f"Circle ==RADIUS : {circle.radius} : IS_FILLED : {circle.filled}  :  COLOR : {circle.color}")
print(f"Triangle == WIDTH : {triangle.width}  : HEIGTH : {triangle.height} : IS_FILLED : {triangle.filled} : COLOR : {triangle.color}")
print(f"SQUARE == WIDTH : {square.width} : IS_FILLED : {square.filled}  : COLOR : {square.color}")

circle.describe()
square.describe()
triangle.describe()











