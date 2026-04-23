# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:45:00 2026

@author: abhishek jagdale
"""

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # This should be a list of marks

    def calculate_grade(self):
        # Calculate the average percentage
        average = sum(self.marks) / len(self.marks)
        
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "Fail"

    def display_report(self):
        average_score = sum(self.marks) / len(self.marks)
        grade = self.calculate_grade()
        
        print("--- Student Progress Report ---")
        print(f"Name:        {self.name}")
        print(f"Roll No:     {self.roll_number}")
        print(f"Average:     {average_score:.2f}%")
        print(f"Final Grade: {grade}")
        print("-" * 31)

# --- Example Usage ---
# 1. Create a student with a list of marks for 3 subjects
# (Make sure 'marks' is inside square brackets [ ])
student1 = Student("Abhishek", "2026-ENG-01", [85, 78, 92])

# 2. Display the grade report
student1.display_report()
