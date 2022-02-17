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

    # calculate two emplyess salary using spesial method __add__
    def __add__(self, other):
        return self.salary + other.salary

    # count email characters
    def __len__(self):
        return len(self.email)

    def __repr__(self):
        return f"Employee {self.first_name}, {self.last_name}: {self.salary}"

    # if __str__ present __repr__ will not print
    def __str__(self):
        return f"{self.getFullName()} , {self.email}"


employee_1 = Employee("Md", "Khan", 930000)
employee_2 = Employee("Alex", "Jurdo", 89000)

# def __add__(self, other) method magic method atumatically get called
print(employee_1 + employee_1)
print(len(employee_2))

# print(Employee.total_employee)
# print(employee_1)
# repr(employee_1)
# str(employee_1)
