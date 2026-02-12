# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 10:21:01 2026

@author: User
"""

year = int(input("Enter year:"))
if (year % 400 == 0)or(year % 4 == 0 and year % 100!= 0):
        print("leap year")
else:
        print("Not a leap year")