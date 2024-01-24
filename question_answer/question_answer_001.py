"""
1. What is python interpreter?
--> Python interpreter is a program that reads and executes python program.
--> There are two ways to use interpreter:
    1. Interactive mode
    2. Script mode
--> Interactive mode: In this mode, you can type python code and get the result immediately.
--> Script mode: In this mode, you can write your python code in a file and run it.
--> To run python program in script mode, you need to save your code in a file with .py extension.
--> To run python program in script mode, you need to use command prompt.
"""

"""
2. Does python supports SWITCH statement?
--> No, python does not support switch statement.
--> But we can use dictionary to implement switch statement.
Example:
def switch_demo(argument):
    switcher = {
        0: "This is case zero",
        1: "This is case one",
        2: "This is case two",
    }
    return switcher.get(argument, "nothing") 
"""

"""
3. What is pickling and unpickling?
--> Pickling: It is a process where a python object hierarchy is converted into a byte stream.
--> Unpickling: It is the inverse of pickling process where a byte stream is converted into an object hierarchy.
"""
# Pickling
import pickle

person = {"name": "John", "age": 23, "salary": 3500.0}
with open("person.txt", "wb") as file:
    pickle.dump(person, file)
print("Pickling done!!")

# Unpickling
with open("person.txt", "rb") as file:
    person = pickle.load(file)
    print('After completion of unpickling: ', person)

print('------------------------------------------ \n')

"""
4. What is lamda function in python?
--> *** A lambda function can take any number of arguments, but can only have one expression. ***
--> In python, anonymous function is a function that is defined without a name.
--> While normal functions are defined using the def keyword, in python anonymous 
    functions are defined using the lambda keyword.
--> Hence, anonymous functions are also called lambda functions.
--> Syntax:
    lambda arguments: expression
--> Example:
    double = lambda x: x * 2
    print(double(5))
"""
x = lambda a, b: a * b
print('The result using lambda function: ', x(5, 6))

y = lambda a, b, c: a + b + c
print(y(5, 6, 4))

print('------------------------------------------ \n')

"""
5. Where you prefer lambda function?
--> *** whenever you want to create a function that will only contain simple expressions ***
--> Lambda function is used when you need a nameless function for a short period of time.
--> Lambda function is used along with built-in functions like filter(), map() etc.
"""

"""
6. What is the difference between remove and del?
--> remove() is a built-in function of list.
--> remove() will remove the first occurrence of the value.
--> del is a statement in python.
--> del will delete the item at a specific index.
--> del can also be used to delete slices of a list or clear the entire list.
"""
# Example of remove()
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list1.remove(5)
print('After removing 5 from list1: ', list1)

# Example of del
list2 = [10, 20, 30, 40, 50, 60, 70, 80]
del list2[2]
del list2[3:5]
print('After deleting 30 from list2: ', list2)

print('------------------------------------------ \n')

"""
7. What is membership and identity operators?
--> Membership operators: in, not in
--> Identity operators: is, is not
"""
# Example of membership operators
list3 = [1, 2, 3, 4, 5, 6, 7, 8]
print('Is 5 present in list3: ', 5 in list3)

# Example of identity operators
x = 5
y = 5
print('Is x and y are same: ', x is y)

print('------------------------------------------ \n')

"""
8. Does python script supports arrays?
--> No, python does not support arrays.
--> But python supports list.
** Work around using numpy library, we can use arrays. But in core python array is not supported.
"""

"""
9. How to sort a dictionary in python?
--> We can use sorted() function to sort a dictionary.
--> sorted() function sorts the elements of a given iterable in a specific order (either ascending or descending)
"""
# Example of sorted() function
dict1 = {'name': 'John', 'age': 23, 'salary': 3500.0}
print('Sorted dictionary: ', sorted(dict1))
dict2 = {10: 'balls', 20: 'bats', 30: 'gloves', 40: 'pads'}
print('Sorted dictionary: ', sorted(dict2))

print('------------------------------------------ \n')

"""
10. Check that a string contains only character?
"""
# Example of isalpha() method
str1 = 'HelloWorld'
print('Is str1 contains only character: ', str1.isalpha())

print('------------------------------------------ \n')

"""
11. What is list comprehension?
--> List comprehension is an elegant way to define and create list in python.
--> We can create lists just like mathematical statements and in one line only.
--> **** List comprehension offers a shorter syntax when you want to create a new 
    list based on the values of an existing list. ****
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
  if "a" in x:
    new_list.append(x)

print('After completion of list comprehension: ', new_list)
