# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:41:24 2021

@author: Neha Nayak
"""

def Palindrome(str):
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
str=input("enter the string:")
ans = Palindrome(str)
 
if (ans):
    print("Yes,{} is a palindrome.".format(str))
else:
    print("No,{} is not a palindrome.".format(str))