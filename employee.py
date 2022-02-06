#!/usr/bin/env python3
# Python 3.9.6

from distutils.command.build_scripts import first_line_re


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + "." + last_name + "@example.com"

    def getFullName(self):
        return f"{self.first_name} {self.last_name}"

    def getEmail(self):
        return f"{self.email.lower()}"


employee_1 = Employee("Md", "Khan", 100000)
employee_2 = Employee("Alex", "Jurdo", 100000)

print(employee_1.email)
print(employee_1.getFullName())
print(employee_2.getEmail())
