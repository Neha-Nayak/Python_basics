# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:53:54 2021

@author: Neha Nayak
"""
"""
import time
import datetime
today = datetime.("%m/%d/%Y")
today_format = datetime.datetime.strptime(today, "%m/%d/%Y")
print (today_format)

exp_date = str(today_format + datetime.timedelta(days=365)).split(" ")
exp = exp_date[0]
print (exp)`

"""
import datetime
current_date= datetime.date.today().strftime("%d-%m-%Y")
print(current_date)
#%m = Month as a decimal number [01,12].
#%d + Day of the month as a decimal number [01,31].
#%Y = Year with century as a decimal number[2020].
