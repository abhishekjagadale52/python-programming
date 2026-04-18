#Copy backup data from one file to another.
Created on Mon Mar 23 15:32:09 2026
@author: Abhishek jagdale

source_file = "source. txt"
with open(source_file, "w") as file:
file.write("This is the original file. \n")



file.write("It contains important data. \n")



file.write("This data will be copied as backup. \n")
print(f"Data written to {source_file} successfully. \n")
with open(source_file, "r") as file:
content = file.read()
print("Reading source file content:")



print(content)
backup_file = "backup. txt"

In [1]: %runfile 'C:/Users/SANKET NIKAM/Desktop/nikhil nikam python/untitled36.py'

with open(backup_file, "w") as file:

-- wdir

file.write(content)

Data written to source.txt successfully.

print(f"Data copied to {backup_file} successfully. \n")

Reading source file content:

print("Reading backup file content:")

This is the original file.

with open(backup_file, "r") as file:

It contains important data.

print(file.read())
