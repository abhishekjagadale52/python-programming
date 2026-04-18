#Create a student attendance file and append new records.
Created on Mon Mar 23 15:30:46 2026
@author: Abhishek jagdale

file_name = "attendance.txt"


with open(file_name, "w") as file:
file.write("Student Attendance Record: \n")



file.write("1. om - Present\n")



file.write("2. raj - Absent\n")
file.write("3. sourav - Present\n")



print(f"Data written to {file_name} successfully. \n")

print("Reading file content:")

-- wdir

with open(file_name, "r") as file:

Data written to attendance.txt successfully.

content = file.read()
print(content)
with open(file_name, "a") as file:

2. raj - Absent

file.write("4. Priya - Present\n")

3. sourav - Present

file.write("5. shreyash - Absent\n")

After appending new records:

print("After appending new records:")

Student Attendance Record:

with open(file_name, "r") as file:

1. om - Present

print(file.read())
with open(file_name, "r") as file:

4. Priya - Present

lines = file.readlines()

5. shreyash - Absent

print("Total number of students:", len(lines) - 1)
