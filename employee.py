#!/usr/bin/env python3
# Python 3.9.6

from distutils.command.build_scripts import first_line_re


class Employee:

    raise_amount = 1.04  # employee default raise amount
    total_employee = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + "." + last_name + "@example.com"

        # Emplyee wille be aded once new emplyee instance created
        # self.total_employee += 1 is wrong here
        Employee.total_employee += 1

    def getFullName(self):
        return f"{self.first_name} {self.last_name}"

    def getEmail(self):
        return f"{self.email.lower()}"

    def applyRaise(self):
        self.salary = int(self.salary * self.raise_amount)


employee_1 = Employee("Md", "Khan", 100000)
employee_2 = Employee("Alex", "Jurdo", 100000)

# print(Employee.total_employee)
# print(employee_1.total_employee)

# print(employee_1.email)
# print(employee_1.getFullName())
# print(employee_2.getEmail())
# print(employee_2.applyRaise())
# print(employee_1.salary)
# employee_1.raise_amount = 1.05
# employee_1.applyRaise()
# print(employee_1.salary)

# print(employee_1.__dict__)
