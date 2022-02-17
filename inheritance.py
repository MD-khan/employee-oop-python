#!/usr/bin/env python3
# Python 3.9.6


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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, salary, programing_language):
        super().__init__(first_name, last_name, salary)
        self.programing_language = programing_language


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmployee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def removEmployee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def showEmployee(self):
        for employee in self.employees:
            print('--->', employee.getFullName())


dev_1 = Developer("Md", "Khan", 1200000, 'python')
dev_2 = Developer("Alex", "Jurdo", 100000, 'php')

mng_1 = Manager("Sue", 'Smith', 900000, [dev_1])
mng_1.addEmployee(dev_1)
mng_1.addEmployee(dev_2)

mng_1.removEmployee(dev_2)

mng_1.showEmployee()

print(isinstance(mng_1, Developer))
print(issubclass(Manager, Employee))

# print(mng_1.email)

# print(dev_1.salary)
# print(dev_1.programing_language)


# dev_1.applyRaise()
# print(dev_1.salary)
# print(help(Developer))
# print(Employee.total_employee)
# print(employee_1.total_employee)
# print(employee_1.__dict__)
