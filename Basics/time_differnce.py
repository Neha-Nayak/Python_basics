# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:19:29 2021

@author: Neha Nayak
"""
import datetime
time1= datetime.datetime.strptime(input('enter time in HH:MM format: '), "%H:%M")
print(time1.strftime("%H:%M"))
time2= datetime.datetime.strptime(input('enter time in HH:MM format: '), "%H:%M")
print(time2.strftime("%H:%M"))



time_diff=time1-time2

print(time_diff.total_seconds()/60)
#output only in 12 hr format

