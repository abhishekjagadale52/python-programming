# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:18:34 2026

@author: abhishek jagdale
"""
import datetime

# Get current date and time (Comment nantar Enter daba)
now = datetime.datetime.now()

# Print current date
print("Current Date:", now.strftime("%Y-%m-%d"))

# Print current time (He navin line var ghy)
print("Current Time:", now.strftime("%H:%M:%S"))

# Print current weekday (He pan navin line var ghy)
print("Weekday:", now.strftime("%A"))
