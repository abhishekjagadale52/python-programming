# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:59:54 2026

@author: abhishek jagdale
"""

import datetime

# Step 1: datetime module vaparun aajchi date ani vel ghene
current_data = datetime.datetime.now()

# Step 2: Date la hospital system sathi 'Day-Month-Year' format madhe convert karne
# %d = Day, %B = Month Name, %Y = Year
formatted_date = current_data.strftime("%d %B %Y")

# Step 3: Hospital appointment sathi message print karne
print("-" * 40)
print("--- SHREE HOSPITAL APPOINTMENT SYSTEM ---")
print(f"Appointment Booking Date: {formatted_date}")
print("-" * 40)
