# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:44:46 2021

@author: Neha Nayak
"""

# Python Program to Print Numbers from 1 to N
 
n = int(input("Please Enter any Number: "))
i = 1

print("The List of Numbers from 1 to {0} are".format(n)) 

while ( i <= n):
    print (i, end = '  ')
    i = i + 1
    
#to check whether the n is positive or negative

n = int(input("Please Enter any Number: "))
if(n<0):
    print(n,"is a negative number")
else:
    print(n,"is a positive number")