# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:53:07 2025

@author: M Haseeb Shah
"""

# Dictionary : A collection of {key:value} pairs
#             these are ordered and changeable : NO duplicates

capitals = {"pakistan":"karachi",
            "India":"New delhi",
            "China":"beiging",
            "Russia":"Moscow"
    }

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("India")) returns the value maped to the given key
capitals.update({"Germany":"Berlin"})# update method insert new key value pair also updates the exixting one
capitals.pop("China")# delete the key pair value for given key
capitals.popitem()# popitem method deletes the recently entered key value pair
#capitals.clear()#clear method clears the whole dictionary.
"""
keys = capitals.keys()# return all the keys of the dictionary
print(keys)
print(capitals)

values = capitals.values()

for value in values :
    print(value,end=" ")"""

items = capitals.items()#returns all the key value pairs

for key,value in items:
    print(f"{key} : {value}")    

















