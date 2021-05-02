# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:32:38 2021

@author: Neha Nayak
"""
#to assign qaudrant
x=int(input("enter the value of x coordinate:"))
y=int(input("enter the value of y coordinate:"))

if(x>=0 and y>=0):
    print(x,",",y,"are in 1st quadrant")
elif(x<=0 and y>=0):
    print(x,",",y,"are in 2nd quadrant")
elif(x<=0 and y<=0):
    print(x,",",y,"are in 3rd quadrant")
else:
    print(x,",",y,"are in 4th quadrant")
    
