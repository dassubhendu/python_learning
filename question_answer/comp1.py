"""
1. What is suite in Python?
--> In Python, a suite is a block of code that consists of one or more statements.
    It is used to group related statements together, and is typically used when defining functions,
    classes, and control structures. A suite is typically indented,
    with each line of the suite being indented the same amount.
"""

"""
2. What are the data types we have in Python?
"""
print("\n")

"""
3. What are different ways to concatenate two tuples.
"""
t1 = (10, 30, 30)
t2 = ('a', 'b', 'c')
t3 = t1 + t2
print('Concatenating two tuples: ', t3)
# Another way of concatenating tuples

print("\n")

"""
4. What is slice operator in Python?
"""
# Slicing a list
l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print('Printing with list slicing: ', l1[2:5])
# Slicing tuple
t1 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print('Printing with tuple slicing: ', t1[3:6])
# Slicing String
s1 = 'hello good morning'
print('Printing String with Slicing: ', s1[2:5])

print("\n")

"""
5. What are the different types of functions we have in python?
--> Mainly, there are two types of functions:
--> User-defined functions – These functions are defined by the user to perform a specific task.
--> Built-in functions – These functions are pre-defined functions in Python.
"""

print("\n")

"""
6. Write a class which has two parameters. How to print those parameters.
"""


class Employee:

    def __init__(self, emp_id, name):
        self.employee_id = emp_id
        self.emp_name = name
        print('The employee id: ', self.employee_id)
        print('The employee name: ', name)


e1 = Employee(1001, 'Subhendu')
