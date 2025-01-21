# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:34:54 2025

@author: M Haseeb Shah
"""

#---------------------------------------(<<QUIZ-GAME>>)--------------------------------------------
questions =  ("How many elements are there in perodic table? : ",
              "Which animal lays the largest eggs ? : ",
              "What is the most abundant gas in earths Atmosphere? : ",
              "How many bones are in human body ? : ",
              "Which planet is the most hottest in the solar system ? : ")

options = (("A)116.", "B)117.","C)118.", "D)119." ),
           ("A)Whale.","B)Crocodile.","C)Elephant.","D)Ostrich."),
           ("A)Nitrogen.","B)Oxygen.","C)Carbon-Dioxide.","D)Hydrrogen."),
           ("A)206.","B)207.","C)208.","D)209."),
           ("A)Mercury.","B)venus.","C)Earth.","D)Mars"))

answers = ("C","D","A","A","B")

guesses = []
score = 0
question_no = 0

for question in questions :
    print("------------------------------------")
    print(question)
    for option in options[question_no] :
       print(option)      
        
    guess = input("ENTER (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_no] :
        score+=1
        print("CORRECT")
    else :
        print("INCORRECT")
        print(f"{answers[question_no]} is the correct answer.")
    question_no+=1

print("------------------------------------")
print("--------------RESULTS---------------")
print("------------------------------------")
print("Answers : ",end="")
for answer in answers :
    print(answer,end=" ")
print()

print("Guesses : ",end="")
for guess in guesses :
    print(guess,end=" ")
print()

score = int((score/len(questions)) *100)
print(f"Your score is c: {score}%")






