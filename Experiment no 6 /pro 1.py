#To Create a text file and add course outcomes of this course.
Created on Mon Mar 23 14:54:31 2026
@author: Abhishek jagdale

file_name = "course_outcomes.txt"



with open(file_name, "w") as file:
file.write("Course Outcomes (COs): \n")



file.write("1. Understand the basics of Python programming. \n")



file.write("2. Apply loops, functions, and data structures. \n")
file.write("3. Handle files and perform basic I/0 operations. \n")
file.write("4. Solve programming problems using logic and algorithms. \n")
file.write("5. Develop small projects using Python. \n")
print(f"Data written to {file_name} successfully. \n")
