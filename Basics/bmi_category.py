# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:05:07 2021

@author: Neha Nayak
"""

import fun_bmi
weight=float(input("enter weight in kilograms:"))
height=float(input("enter height in meters:"))
bmi=0
print("bmi is:")
print(fun_bmi.bmi(weight,height))
fun_bmi.category(bmi)