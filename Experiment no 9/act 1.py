# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:19:47 2026

@author: abhishek jagdale
"""

import math

# Step 1: Input ghene
P = float(input("Enter loan amount (Principal): "))
annual_rate = float(input("Enter annual interest rate (in %): "))
years = int(input("Enter loan tenure in years: "))

# Step 2: Monthly calculation sathi convert karne
r = annual_rate / (12 * 100) # Monthly rate
n = years * 12               # Total months

# Step 3: math.pow vaparun EMI formula
numerator = math.pow(1 + r, n)
emi = P * r * numerator / (numerator - 1)

# Step 4: Output dakhvane
print("-" * 30)
print(f"Monthly EMI: {round(emi, 2)}")

# Total Interest calculate karne
total_payment = emi * n
total_interest = total_payment - P
print(f"Total Interest Payable: {round(total_interest, 2)}")
print("-" * 30)
