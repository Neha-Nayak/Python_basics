# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 23:37:23 2021

@author: Neha Nayak
"""
#simple calculator
def addition(a,b):
    return a+b
     
def subtraction(a,b):
    return a-b
    
def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b
   
print("choose operation")   
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

while True:
    choice=input("Enter choice:")
    if choice in ('1', '2', '3', '4'):
        a=float(input("Enter the first number: "))
        b= float(input("Enter the second number: "))

        if choice == '1':
            print(a, "+", b, "=", addition(a,b))

        elif choice == '2':
            print(a, "-", b, "=", subtraction(a,b))

        elif choice == '3':
            print(a, "*", b, "=", multiplication(a,b))

        elif choice == '4':
            print(a, "/", b, "=", division(a,b))
        break
    else:
        print("Invalid Input")
        break