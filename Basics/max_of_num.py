# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:56:29 2021

@author: Neha Nayak
"""
#to detemine the maximum of two numbers
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a>=b:
    print("{} is greater than {}".format(a,b))
else:
    print("{} is greater than {}".format(b,a))
    
   
    
    
#to detemine the maximum of three numbers   
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a>b and a>c):
    print(a,"is the largest of the given numbers.")
elif(b>a and b>c):
    print(b,"is the largest of the given numbers.")
else:
    print(c,"is the largest of the given numbers.")
