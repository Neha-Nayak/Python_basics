# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 00:05:31 2021

@author: Neha Nayak
"""

# Python Program to Count Vowels and Consonants in a String

str= input("Enter a String : ")
vowels = 0
consonants = 0

for i in str:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Number of Vowels are= ", vowels)
print("Number of Consonants are= ", consonants)