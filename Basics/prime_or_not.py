# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:20:47 2021

@author: Neha Nayak
"""
num=int(input("enter a number:"))

if num > 1:
    for i in range(2, num):
         if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
         print(num, "is a prime number")
        
else:
     print(num, "is not a prime number")
    