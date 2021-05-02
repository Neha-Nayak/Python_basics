# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:48:34 2021

@author: Neha Nayak
"""
             
import sys
b=tuple()
a=list(b)
n=int(input("enter the length of the tuple:"))

for i in range(0,n):
    ele=str(input("enter the elements of the tuple:"))
    a.append(ele)
print(a)
key=str(input("enter the key element to be searched:"))
for i in range(len(a)):
    if key == a[i]:
        print("key is found at",i+1)
        sys.exit()
print("key in not found")
    