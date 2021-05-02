# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:39:57 2021

@author: Neha Nayak
"""
a=list()
b=list()
n=int(input("enter the length of the list:"))

for i in range(0,n):
    elea=int(input("enter the elements of the list a:"))
    eleb=int(input("enter the elements of the list b:"))
    a.append(elea)
    b.append(eleb)
    
print(a)
print(b)
res=list()
for i in range(len(a)):
    res.append(a[i] + b[i])
  
print("Result is:",res)