# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:38:38 2026

@author: abhishek jagdale
"""
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_total_salary(self, bonus_percentage):
        bonus_amount = (bonus_percentage / 100) * self.base_salary
        return self.base_salary + bonus_amount

    def display_details(self, bonus_percentage):
        total = self.calculate_total_salary(bonus_percentage)
        # Pre-calculating bonus to keep the print statement simple
        bonus_val = (bonus_percentage / 100) * self.base_salary
        
        print("--- Employee Payroll Details ---")
        print(f"Employee Name: {self.name}")
        print(f"Employee ID:   {self.employee_id}")
        print(f"Base Salary:   ${self.base_salary}")
        print(f"Bonus:         {bonus_percentage}% (${bonus_val:.2f})")
        print(f"Total Salary:  ${total:.2f}")
        print("-" * 32)

# --- Example Usage ---
emp1 = Employee("John Doe", "E101", 50000)
emp1.display_details(10)
""
