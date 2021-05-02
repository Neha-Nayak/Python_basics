# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:31:27 2021

@author: Neha Nayak
"""

def quadrants(x,y):
    if(x>=0 and y>=0):
        print(x,",",y,"are in 1st quadrant")
    elif(x<=0 and y>=0):
        print(x,",",y,"are in 2nd quadrant")
    elif(x<=0 and y<=0):
        print(x,",",y,"are in 3rd quadrant")
    else:
        print(x,",",y,"are in 4th quadrant")

x=int(input("enter the value of x coordinate:"))
y=int(input("enter the value of y coordinate:"))
output= quadrants(x,y)

