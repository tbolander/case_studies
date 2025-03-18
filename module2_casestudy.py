"""
Name: Tyler Bolander
File Name: module2_casestudy.py
Description: accepts students last name, first name, and GPA. Outputs students status.
"""


while True:
    # get last name or ZZZ to end
    last_name = input("Please enter the student's last name (or ZZZ to end): ")
    if last_name == 'ZZZ':
        break
    # get first name
    first_name = input("Please enter the student's first name: ")
    # get student GPA as float value
    gpa = float(input("Please enter the student's GPA: "))
    # >= 3.5 GPA? dean's list
    if gpa >= 3.5:
        print(f"{first_name} {last_name} is on the Dean's List. \n")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} is on the Honor Roll. \n")
    else:
        print(f"{first_name} {last_name} is an average student. \n")