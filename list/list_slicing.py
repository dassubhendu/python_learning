#                  0        1        2       3       4       5       6
#               "python"  30.5    "java"    True     10      20     "ruby"
#                 -7       -6       -5       -4      -3      -2      -1

list1 = [10, 20, "python", 30.5, "java", True, 40, 20, 60, 70, 80, 90]
print(list1[0:])  # If it needs to go to the end of the list, just leave the second index blank
print(list1[2:])
print(list1[2:6])  # The second index is not included, it is just stop calculator

# List is immutable, so we can't change the value of an element in a list
list1[0] = 100
print('List element is modified: ', list1)

# How to delete an element from a list

# How to add an element to a list
list1.append(200)
list1.append("ruby")
print('Item is appended at the last in the list: ', list1)

# How to insert an element at a specific index in a list
list1.insert(2, "C++")
print('Item is inserted at the specific index in the list: ', list1)
