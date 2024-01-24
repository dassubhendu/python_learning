"""
1. What is the difference between shallow copy and deep copy?
--> The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
--> A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
--> A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
"""

# **************** Important Shallow copy and deep copy is incomplete ****************

import copy
import re

# Shallow copy example
print(" ***************** Shallow copy example *****************")
old_shallow_list = [[5, 8, 2], [40, 32, 45], [10, 20, 40]]
new_shallow_list = copy.copy(old_shallow_list)
print("old shallow list: ", old_shallow_list)
print("new shallow list: ", new_shallow_list)
old_shallow_list[1][1] = 100
print("old data after shallow copy: ", old_shallow_list)
print("Shallow copied data: ", new_shallow_list)

print("\n")

# Deep copy example
print(" ***************** Deep copy example *****************")
old_deep_list = [[5, 8, 2], [40, 32, 45], [10, 20, 40]]
new_deep_list = copy.deepcopy(old_deep_list)
print("old deep list: ", old_deep_list)
print("new deep list: ", new_deep_list)
old_deep_list[1][1] = 100
print("old data after deep copy: ", old_deep_list)
print("Deep copied data: ", new_deep_list)

print("\n")

"""
2. What is the difference between list and tuple?
--> List is mutable and tuple is immutable.
--> List is slower than tuple.
--> List is written as [1, 2, 3] and tuple is written as (1, 2, 3).
--> List is better for performing operations, such as insertion and deletion, and tuple is better for accessing the elements.
--> List consumes more memory than tuple.
"""

"""
3. Can we modify a tuple while lies inside a list?
--> Yes, we can modify the entire tuple while lies inside a list.
--> But we can modify the tuple elements individually while lies inside a list.
"""
print(" ***************** Can we modify a tuple while lies inside a list? *****************")
list001 = [10, True, "Hello", (1, 2, 3)]
print("list001 which contains tuple: ", list001)
print("tuple inside list001: ", list001[3][1])
# list001[3][1] = 100
print("list001 after modifying tuple: ", list001)
list001[3] = (4, 5, 6)
print("list001 after modifying tuple: ", list001)

print("\n")

"""
4. Can we modify a list while lies inside a tuple?
--> No, it is not allowed to modify a list while lies inside a tuple.
--> Not even the list elements individually.
"""
print(" ***************** Can we modify a list while lies inside a tuple? *****************")
tuple001 = (10, True, "Hello", [1, 2, 3])
print("tuple001 which contains list: ", tuple001)

"""
5. How multithreading is achieved in Python?
--> Multithreading can be achieved in Python by using the following modules:
    1. threading
    2. multiprocessing
    3. concurrent.futures
--> The threading module provides an API similar to the thread module.
--> Global Interpreter Lock (GIL) prevents multiple threads from executing Python bytecodes at once.
"""

print("\n")

"""
6. How can the ternary operators be used in python?
--> The Ternary operator is the operator that is used to show the conditional statements.
--> This consists of the true or false values with a statement that has to be evaluated for it.
--> Syntax:
    [on_true] if [expression] else [on_false]
"""
print(" ***************** Ternary operator example *****************")
x, y = 25, 50
small = x if x < y else y
print("small: ", small)

"""
7. What is monkey patching in Python?
--> Monkey patching is a technique that allows the programmer to modify or extend other code at runtime.
--> Monkey patching is not a standard technique and is frowned upon by some developers since it violates the open/closed principle of software development,
--> Monkey patching example:
    def monkey_f(self):
        print("monkey_f() is being called")
    class A:
        def f(self):
            print("f() is being called")
    a = A()
    a.f()
    A.f = monkey_f
    a.f()
**** Still not clear about monkey patching ****
"""

"""
8. What is the difference between range & xrange?
"""

print("\n")

"""
9. How to randomize the items of a list in place in Python?
"""
print(" ***************** Randomize the items of a list in place in Python *****************")
from random import shuffle

list002 = [10, 20, 30, 40, 50]
print("list002 before randomizing: ", list002)
shuffle(list002)
print("list002 after randomizing: ", list002)

print("\n")

"""
10. Write a sorting algorithm for a numerical dataset in Python. [List Comprehension]
--> List.sort() and sorted() can be used to achieve sorting in Python.
--> List comprehension can be used to achieve sorting in Python.
"""
print(" ***************** Sorting algorithm for a numerical dataset in Python *****************")
list003 = [50, 10, 40, 20, 15]
list003.sort()
print("list003 after sorting: ", list003)
list004 = ["50", "10", "40", "20", "15"]
list004 = [int(i) for i in list004]
list004.sort()
print("list004 after sorting: ", list004)

print("\n")

"""
11. zip() function in Python
--> The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
    and then the second item in each passed iterator are paired together etc.
"""
print(" ***************** zip() function in Python *****************")
t1 = ('a', 'b', 'c', 'd', 'e')
t2 = (1, 2, 3, 4, 5)
t3 = dict(zip(t1, t2))
print("t3: ", t3)

print("\n")

"""
12. How to creare a list using range() function?
"""
print(" ***************** How to creare a list using range() function? *****************")
list005 = list(range(10))
print("list005: ", list005)

print("\n")

"""
13. Dictionary comprehension
--> Dictionary comprehension is an elegant and concise way to create dictionaries.
--> Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.
"""
print(" ***************** Dictionary comprehension *****************")
myDict = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
print("myDict: ", myDict)

print("\n")

"""
14. How to find / remove duplicate elements from a list?
"""
my_list = [10, 20, 30, 40, 50, 60, 10, 30]
__size = len(my_list)
repeated = []
for i in range(__size):
    k = i + 1
    for j in range(k, __size):
        if my_list[i] == my_list[j] not in repeated:
            repeated.append(my_list[i])
print("The duplicate element in list: ", repeated)

print("\n")

"""
15. Explain split(), sub(), subn() methods of "re" module in Python.
--> split() ==> uses a regex pattern to "split" a given string into a list.
--> sub() ==> finds all substrings where the regex pattern matches and then replace them with a different string.
--> subn() ==> does the same work as sub() but returns the new string along with the no. of replacements.
"""
print(" ***************** split(), sub(), subn() methods of 're' module in Python *****************")
myString = "Hello 12345 World"
print("myString: ", myString)
pattern = ' '
print("myString.split(): ", re.split(pattern, myString))
print("myString.sub(): ", re.sub(pattern, '-', myString))
print("myString.subn(): ", re.subn(pattern, '-', myString))

print("\n")

"""
16. What is the difference between re.search() and re.match()?
"""

print("\n")

"""
17. What is the difference between "is" and "=="?
"""

print("\n")

"""
18. What is inheritance in Python?
--> Inheritance is a powerful feature in object oriented programming.
--> It refers to defining a new class with little or no modification to an existing class.
--> The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.
--> Inheritance is done by passing the parent class as an argument to the definition of a child class.
--> Syntax:
    class BaseClass:
        Body of base class
    class DerivedClass(BaseClass):
        Body of derived class
--> Multiple inheritance is also allowed in Python.
--> Syntax:
    class BaseClass1:
        Body of base class 1
    class BaseClass2:
        Body of base class 2
    class DerivedClass(BaseClass1, BaseClass2):
        Body of derived class
--> Multilevel inheritance is also allowed in Python.
--> Syntax:
    class BaseClass:
        Body of base class
    class DerivedClass1(BaseClass):
        Body of derived class 1
    class DerivedClass2(DerivedClass1):
        Body of derived class 2
--> Hierarchical inheritance is also allowed in Python.
--> Syntax:
    class BaseClass:
        Body of base class
    class DerivedClass1(BaseClass):
        Body of derived class 1
    class DerivedClass2(BaseClass):
        Body of derived class 2
--> Hybrid inheritance is also allowed in Python.
--> Syntax:
    class BaseClass1:
        Body of base class 1
    class BaseClass2:
        Body of base class 2
    class DerivedClass1(BaseClass1, BaseClass2):
        Body of derived class 1
    class DerivedClass2(BaseClass1, BaseClass2):
        Body of derived class 2
    
"""

print("\n")

"""
19. sys.version_info
--> sys.getrefcount()
-->
"""

"""
20. How to remove a variable from memory in Python?
--> del keyword is used to remove a variable from memory.
"""

print("\n")

"""
21. What is the difference between range & xrange?
--> range() ==> returns a list whereas xrange() ==> returns an object that acts like an iterator.
--> xrange() is faster than range() because it does not create any list.
--> xrange() is deprecated in Python 3.
--> xrange() is used only in Python 2.
"""
a = range(1, 10)
for i in a:
    print(i)
# b = xrange(1, 100)
print(type(a))

print("\n")

"""
22. How to convert a list of integers to a comma separated string in Python?
"""
print(" ***************** How to convert a list of integers to a comma separated string in Python? *****************")
list006 = [10, 20, 30, 40, 50]
print("list006: ", list006)
numbers = ','.join(str(i) for i in list006)
print("numbers: ", numbers)

print("\n")

"""
23. Take the below two lists as input and print expected output.
    list1 = ['My', 'name']
    list2 = ['is', 'John']
    Expected output: My name is John
"""
list1 = ['My', 'name']
list2 = ['is', 'John']
print(" ***************** Take the below two lists as input and print expected output. *****************")
list1.extend(list2)
print(' '.join(list1))

print("\n")

"""
24. Covert two lists into a dictionary.
"""
list3 = ['a', 'b', 'c']
list4 = [1, 2, 3]
list5 = dict(zip(list3, list4))
print("list5: ", list5)

# Using dictionary comprehension
list6 = {list3[i]: list4[i] for i in range(len(list3))}
print("list6: ", list6)

# Using for loop
list7 = {}
for key in list3:
    for value in list4:
        list7[key] = value
        list4.remove(value)
        break
print("list7: ", list7)

"""
25. Write a program to count the number of times a class is called
"""
print(" ***************** Write a program to count the number of times a class is called *****************")


class A:
    count = 0

    def __init__(self):
        A.count += 1
        print("Count: ", A.count)


a1 = A()
a2 = A()
print(A.count)

"""
26. Write a program to find duplicate characters in a list
"""
list8 = ['India', 'is', 'my', 'country']
str1 = ''.join(list8)
print("str1: ", str1)
duplicates = []
for char in str1:
    if str1.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)
print("duplicates: ", duplicates)
print(*duplicates)  # * is used to print the list without brackets and commas

print("\n")

"""
27. Write a program to find the sum of all the numbers in a list
"""
list9 = [10, 20, 30, 40, 50]
sum1 = 0
for i in list9:
    sum1 += i
print("sum1: ", sum1)

print("\n")

"""
28. Write a program to find the sum of all the even numbers in a list
"""
list10 = [10, 21, 30, 40, 50]
sum2 = 0
for i in list10:
    if i % 2 == 0:
        sum2 += i
print("sum2: ", sum2)

"""
29. Write a program to find the sum of all the odd numbers in a list
"""
list11 = [10, 21, 30, 40, 50]
sum3 = 0
for i in list11:
    if i % 2 != 0:
        sum3 += i
print("sum3: ", sum3)

print("\n")

"""
30. Write a program to find unique characters in a string
"""
str2 = "Hello World"
unique = []
for char in str2:
    if str2.count(char) == 1 and char not in unique:
        unique.append(char)
print("unique: ", unique)
print(*unique)

print("\n")

"""
31. What would be the output of the following code?
--> MRO (Method Resolution Order) is the order in which base classes are searched when executing a method.
"""
print(" ***************** MRO (Method Resolution Order) *****************")


class A1:
    def demo(self):
        print("In class A1")


class B1(A1):
    def demo(self):
        print("In class B1")


class C1(A1):
    def demo(self):
        print("In class C1")


class D1(B1, C1):
    pass


test = D1()
test.demo()

print("\n")

"""
32. Write a one line for loop to print all the words in a list which starts with 'i'
"""
print(
    " ***************** Write a one line for loop to print all the words in a list which starts with 'i' *****************")
list12 = ['india', 'is', 'my', 'country']
print([word for word in list12 if word.startswith('i')])

print("\n")

"""
33. What is the difference between 'is' and '=='
--> is ==> compares the identity of two objects. Reference / address comparison and returns True or False.
--> == ==> compares the values of two objects. Content comparison and returns True or False.
"""
print(" ***************** is and == *****************")
a = [1, 2, 3]
b = [1, 2, 3]
print("a is b: ", a is b)
print("a == b: ", a == b)
c = a  # Aliasing - a and c are pointing to the same object
print("a is c: ", a is c)

print("\n")

"""
34. Explain about ternary or conditional operator in Python
--> Binary operator ==> takes two operands.
--> Ternary operator ==> takes three operands.
--> Nesting of ternary operator is possible.    
Example:
    x = 'first value' if condition else 'second value' # Three operands
"""
# Find max of two numbers
print(" ***************** Find max of two numbers *****************")
a = 10
b = 20
max1 = a if a > b else b
print("Maximum value: ", max1)
print(f'The maximum value is: {max1}')

# Find max of three numbers
print(" ***************** Find max of three numbers *****************")
a = 10
b = 20
c = 30
max2 = a if a > b and a > c else b if b > c else c

print("\n")

"""
35. What are various data types in Python?
--> Fundamental Data Type: int, float, complex, bool, str
--> Derived Data Type: list, tuple, set, dict, frozenset
--> Special Data Type: None
--> User Defined Data Type: class, enum, function, lambda
==> complex numbers: 1 + 2j
==> Frozenset: immutable set
"""

print("\n")

"""
36. Explain mutability and immutability in Python.
--> List objects are mutable.
--> Tuple objects are immutable.
--> String objects are immutable.
--> Set objects are mutable.
--> Dictionary objects are mutable.
===> All fundamental data types are immutable.
===> All derived data types are mutable except tuple.
===> Frozenset is immutable.
===> Bytes objects are immutable.
===> Bytearray objects are mutable.
===> Range objects are immutable.
"""

print("\n")

"""
37. Explain the difference between List and Tuple.
--> List is mutable and Tuple is immutable.
--> List is slower than Tuple.
--> List is written as [1, 2, 3] and Tuple is written as (1, 2, 3).
--> List is better for performing operations, such as insertion and deletion, and Tuple is better for accessing the elements.
--> List consumes more memory than Tuple.
--> List can be converted to Tuple and vice versa.
--> List can be used as a key in a dictionary and Tuple cannot be used as a key in a dictionary.
--> Comprehension is applicable for list and not tuple
"""

# Special difference ==> Same reference would be pointed for tuples if those contain same set of value.
l1 = [10, 20, 30, 40]
l2 = [10, 20, 30, 40]
t1 = (10, 20, 30, 40)
t2 = (10, 20, 30, 40)
print(id(l1))
print(id(l2))
print(id(t1))
print(id(t2))

print("\n")

"""
38. Set and Dictionary stores object with hashcode.
--> List doesn't store object with hashcode.
--> We can not add List object in Set.
    Example: s = {10, 20, 30, [50, 60]} # TypeError: un-hashable type: 'list'
--> We can add Tuple in Set
    Example: s = {10, (20, 30), 40} # This would not throw any error.
--> We can not add List as key in Dictionary.
    Example: d = {[10, 20]: 'subhendu'} # TypeError: un-hashable type: 'list'
--> We can add Tuple as key in Dictionary.
    Example: d = {(10, 20): 'subhendu'}
"""
# s1 = {10, 20, 30, [50, 60]}
# print(s1)
s2 = {10, (20, 30), 40}
print(s2)

print("\n")

"""
39. Unpacking is possible in List, but packing is not possible in list.
--> Unpacking and packing are possible in tuple.
"""
# List unpacking [List packing is not possible ]
l1 = [10, 20, 30, 40]
a, b, c, d = l1
print('This is list unpacking: ', a, b, c, d)

# Tuple unpacking [Tuple packing also possible]
t1 = [10, 20, 30, 40]
e, f, g, h = t1
print('This is tuple unpacking: ', e, f, g, h)

# Tuple packing
a = 10
b = 20
c = 30
d = 40
t3 = a, b, c, d
print('After packing the tuple is: ', t3)

print("\n")

"""
40. What is the difference between Set and FrozenSet?
--> All properties of Set and FrozenSet are same except Set is mutable and FrozenSet is immutable.
"""
# Set is multable
s = {30, 40, 50, 70}
s.add(60)
print('Set after adding a new element: ', s)

# Frozen set is immutable and no add, remove function is available for it.

print("\n")

"""
41. Can we count duplicate element in Set?
--> Yes, for this first we need to convert the set into list and then count the duplicate element.
--> ************ Need to find the right answer ***************
"""
s1 = {10, 20, 30, 40, 50, 30, 60, 70, 30}
l1 = list(s1)
print('The set after converted to list: ', l1)

print("\n")

"""
42. Can we reverse SET objects.
--> If you ever need to reverse an iterator like this, then you should first convert it to a list using list() . 
    In this example, when you try to use reversed() with a set object, you get a TypeError . 
    This is because sets don't keep their items ordered, so Python doesn't know how to reverse them.
"""

print("\n")

"""
43. What is the difference between set() method and set {} object
"""
my_str1 = 'subhendu'
s1 = set(my_str1)
print(s1)
s2 = {10, 'name', 34, 'test', 6.7}
print(s2)

print("\n")

"""
44. Define multi dimensional list. Can we have a single variable with all type of derived data types?
"""
l1 = [
        [10, 20, 30, 40],
        ('a', 3, 'b', 4),
        {"name": "subhendu", "roll_no": 34, "address": "kolkata"},
        {45, 65, 67.4, 56}
]
print(l1)

print("\n")

"""
45. Mention three pre-defined method for Dictionary.
--> Copy, pop, clear, update, keys, values
"""
my_dict = {"name": "subhendu", "roll_no": 34, "address": "kolkata"}
my_dict["state"] = "west_bengal"
print(my_dict)
my_dict.update({"age": 35})
print(my_dict)
my_dict["name"] = "saurav"
print(my_dict)

print("\n")

"""
46. Does dictionary have null key?
--> Yes, key can be null.
"""
my_dict1 = {"": "subhendu", "roll_no": 34, "address": "kolkata"}
print(my_dict1)

print("\n")

"""
47. Does dictionary comprises of duplicate keys?
--> Yes, dictionary can have duplicate keys. Bit it will pick the last entry.
"""
my_dict3 = {"name": "subhendu", "name": "saurav", "name": "sachin", "address": "kolkata"}
print(my_dict3)

print("\n")

"""
48. If we need to Create, Read and Write in file, what would be the approach?
--> "x" - Create - will create a file, returns an error if the file exist
--> "a" - Append - will create a file if the specified file does not exist
--> "w" - Write - will create a file if the specified file does not exist
--> "r+" - Read / Write
--> "w+" - Write / Read
"""
# Creating a file
f = open("myfile.txt", "w")
# Reading the empty file
f1 = open("myfile.txt", "r+")
print('Reading the file when it is empty: ', f1.read())
f1.write('This is a test file')
f1.seek(0)
print('Reading the file with content: ', f1.read())


