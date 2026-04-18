Count frequency of purchased items
Created on Mon Mar 9 14:45:31 2026
@author: Abhishek Jagdale

items = ["apple", "banana", "apple", "orange", "banana", "apple"]



Frequency = {
for item in items:



if item in frequency:



frequency[item] += 1
else:
frequency[item] = 1
print("Item Frequency:", frequency)
