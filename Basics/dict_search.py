# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:16:45 2021

@author: Neha Nayak
"""
#import sys
a={}
n=int(input("enter the length of the dict:"))
for i in range(n):
    key=input("enter the key: ")
    value=input("enter the value: ")
    a.update({key:value})
print(a)
search_key=input("enter the key to be searched: ")

if key in a:
    print("key is found at",a[key])
else:
    print("key in not found")
"""
for i in range(len(a)):
    if search_key == a[key]:
        print("key is found at",i+1)
        sys.exit()
print("key in not found")
 

def searchkey(a,key):
    if key in a:
        print("key is found at",a[key])
    else:
        print("key in not found")

searchkey(a,search_key)"""