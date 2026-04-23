# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:02:20 2026

@author: abhishek jagdale
"""
import math

# Step 1: Pahilya point che coordinates ghene (x1, y1)
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))

# Step 2: Dusrya point che coordinates ghene (x2, y2)
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

# Step 3: Distance formula vaparun calculation karne
# math.sqrt mhanje square root ani math.pow mhanje power
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Step 4: Result display karne
print("-" * 30)
print(f"The distance between two points is: {round(distance, 2)}")
print("-" * 30)
