# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 20:29:28 2025

@author: M Haseeb Shah
"""

class Book : 
    
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self,other):
        return self.title == other.title and  self.author == other.author
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __add__(self,other):
        return self.num_pages + other.num_pages
        
    def __contains__(self,Keyword):
        return Keyword in self.title or Keyword in self.author  
    
    
    def __getitem__(self,keyword):
        
        
        if keyword == 'title':
            return self.title
        elif keyword == 'author':
            return self.author
        elif keyword == 'num_pages':
            return self.num_pages
        else:
            return "INVALID KEY"
        
        
        
book1 = Book("The HOBBIT","J.R.R. TOLKIEN",310)
book2 = Book("The RETURN OF THE KING","J.R.R. TOLKIEN",412)
book3 = Book("Harry potter and the half blood prince","J.K. ROWLING",223)
book4 = Book("The HOBBIT","J.R.R. TOLKIEN",310)

print(book3)
print(book2["num_s"])





