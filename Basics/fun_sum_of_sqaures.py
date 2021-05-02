# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:46:39 2021

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
    return (n*(n+1)*(2*n+1))/2  

def recursion_sum(n):
    if n==1:
        return 1
    else:
        return recursion_sum(n-1)+n