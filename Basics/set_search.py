# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:09:14 2021

@author: Neha Nayak
"""

#import sys
a=set()
n=int(input("enter the length of the set: "))
for i in range(n):
    ele=input("enter the elements: ")
    a.update(ele)
print(a)
key=input("enter the element to be searched: ")

