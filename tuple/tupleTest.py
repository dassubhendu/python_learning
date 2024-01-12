"""
--> Tuple is immutable, list is mutable
--> Tuple is faster than list
--> Tuple is used for heterogeneous (different) datatypes and list is used for homogeneous (similar) datatypes
--> Tuple consumes less memory as compared to list
--> Tuple is used in dictionary, string and list is used in array
--> Tuple has only two built-in methods count() and index() to use
--> List has many built-in methods
--> Tuple is hashable while list is not
--> Tuple is used in fetching data from database, list is used in insertion, deletion and updation
--> Tuple is used in passing data to function, list is used in loops
--> Tuple is ordered collection of items, list is ordered collection of items
"""

# Tuple creation
tuple1 = (1, "python", 2, "robot", True, 4.5, 2, "java", 2)
print(tuple1)
# Access tuple elements using index
print(tuple1[1])
print(tuple1[-1])
# If we need to count the number of occurrences of an element in a tuple, we can use count() method
print(tuple1.count(1)) # The count of 1 would be 1 but the result is 2, as the boolean value True is also 1
print(tuple1.count(2))
# If we need to find the index of an element in a tuple, we can use index() method
print(tuple1.index("python"))
# Slice tuple
print(tuple1[1:5])
# How to convert a tuple into a list. If we pass tuple inside list constructor, it will return a list.
list1 = list(tuple1)
print(list1)
print(type(list1))
# How to convert a list into a set. If we pass list inside set constructor, it will return a set.
set1 = set(list1)
print(set1)
print(type(set1))
# Interesting fact about tuple
# --> When a tuple contains only single sting then length of it will show based on the number of characters in the string
tuple2 = ("python")
print(len(tuple2))
# --> But if we put a comma after the string then it will show the length as 1
tuple3 = ("python",)
print(len(tuple3))
# --> Can we create list of tuples? Yes
list2 = [(1, "python"), (2, "robot"), (3, "java")]
print(list2)
print(list2[1])
print(list2[1][1])
# Another way of creating tuple
tuple4 = tuple((1, "python", 2, "robot", True, 4.5, 2, "java", 2))
print(tuple4)
# Tuple unpacking   --> Unpacking means assigning values of tuple to variables
# Tuple unpacking we must have the same number of variables as the number of items in the tuple
tuple5 = (1, "python", 2, "robot", True, 4.5, 2, "java", 2)
a, b, c, d, e, f, g, h, i = tuple5
print(b)


