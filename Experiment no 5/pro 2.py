# To implement python programs using dictionaries & sets
Created on Mon Mar 9 14:45:31 2026
@author: Abhishek Jagdale

set1 = set(map(int, input("Enter elements of first set (space-separated): ").split(',')))


set2 = set(map(int, input("Enter elements of second set (space-separated): ").split(','
union_set = set1 | set2
intersection_set = set1 & set2
print("Union of the sets:", union_set)
print("Intersection of the sets:", intersection_set)
