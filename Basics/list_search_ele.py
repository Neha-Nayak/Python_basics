# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:06:00 2021

@author: Neha Nayak
"""
import sys
a=list()
n=int(input("enter the length of the list:"))

for i in range(0,n):
    ele=int(input("enter the elements of the list:"))
    a.append(ele)
print(a)
key=int(input("enter the key element to be searched:"))

for i in range(len(a)):
    if key == a[i]:
        print("key is found at",i+1)
        sys.exit()

        
print("key in not found")
    
    
    
    
"""flag=0
j=0
for i in range(len(a)):
    if a[i] == key:
        flag==1
        break
    
        
if flag==1:
    print("key is found at",j)
    sys.exit()
else:
    print("key in not found")"""   

       
        
        
        
        
    
        