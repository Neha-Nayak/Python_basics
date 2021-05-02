# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:50:55 2021

@author: Neha Nayak
"""

def iteration_sum(num):
#iteration
    if num < 0:
        print("invalid")
    else:
        sum = 0
        while(num > 0):
            sum=sum+num
            num-=1
    return sum

 
def formula_sum(n):
    return n*(n+1)/2  

def recursion_sum(n):
    if n==1:
        return 1
    else:
        return recursion_sum(n-1)+n