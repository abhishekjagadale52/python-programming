# To calculate simple interest using functions
Created on Mon Feb 16 15:26:04 2026
@author: Abhishek Jagdale
def simple_interest(principal, rate, time):



si = (principal*rate*time)/100



return si
p = float(input("Enter principal amount:"))



r = float(input("Enter rate of interest:"))



t = float(input("Enter time (in years):"))
interest = simple_interest(p,r,t)
print("Simple interest is:", interest)
