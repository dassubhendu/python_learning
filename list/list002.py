list1 = [10, 20, "python", 30.5, "java", True]
list2 = [20, 40, 50, 60, 70, 80, 90, 20]
list3 = "ruby"

list1.extend(list2)
print(list1)
# If we extend a list with a string, each character of the string will be added to the list as an element
list1.extend(list3)
print(list1)

# If we use pop method on a list, it will remove the last element of the list and return it
list1.pop()
print(list1)

# If we use pop method on a list with an index, it will remove the element at the given index and return it
list1.pop(2)
print(list1)

# If we need to remove a specific element from a list, we can use the value
list1.remove(20)
print(list1)

# If we extend a list with a tuple, each element of the tuple will be added to the list as an element

# If we extend a list with a dictionary, each key of the dictionary will be added to the list as an element

# If we extend a list with a set, each element of the set will be added to the list as an element
