# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:25:27 2021

@author: Neha Nayak
"""

def bmi(weight,height):
    return weight/(height*height)
"""
weight=float(input("enter weight in kilograms:"))
height=float(input("enter height in meters:"))
print(bmi(weight,height))
"""
def category(bmi):
    if bmi < 18.5:
        print("underweight")
    elif 18.5< bmi <24.9:
        print("normal")
    elif 25.0< bmi< 34.9:
        print("overwieght")
    else:
        print("obese")
    return 0
