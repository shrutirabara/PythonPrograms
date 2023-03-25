import datetime
import os.path
'''
This program asks the user for employee information and saves it to a list. 
It then adds each employee from the employees list and creates a txt file and adds in that information.
Utilizes python data structures, functions, error handling and file reading!
'''


def get_int_input(s):
    while True:
        try:
            value = int(input(s))
            return value
        except ValueError:
            print("Please enter an integer")


def get_emp_name(s):
    while True:
        name = input(s)
        if len(name.split()) != 2:
            print("Invalid name")
        else:
            return name


def get_emp_age(n):
    while True:
        age = get_int_input(n)
        if age < 18:
            print("Must be atleast 18 years old")
        else:
            return age


emp_num = get_int_input(
    "How many employees do you want to add? (Enter an integer): ")
employees = []

for i in range(emp_num):
    print(f"Enter information for employee {i+1}: ")

    name = get_emp_name("Enter employee name (first and last): ")
    firstName, lastName = name.split()
    firstName = firstName.capitalize()
    lastName = lastName.capitalize()

    age = get_emp_age("Enter employee age: ")
    currentYear = datetime.datetime.now().year
    birthYear = currentYear - age

    email = f"{firstName}.{lastName}{str(birthYear)[-2:]}@company.com"

    employee = {
        "name": name,
        "age": age,
        "birthYear": birthYear,
        "email": email
    }
    employees.append(employee)


def append_to_file(fileName, employee):
    with open(fileName, "a") as f:
        f.write(f"Name: {employee['name']}\n")
        f.write(f"Age: {employee['age']}\n")
        f.write(f"Birth Year: {employee['birthYear']}\n")
        f.write(f"Email: {employee['email']}\n\n")


fileName = "employee_data_txt"
if not os.path.isfile(fileName):
    with open(fileName, "w") as f:
        pass

for employee in employees:
    append_to_file(fileName, employee)