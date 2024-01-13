"""
1. What is the difference between shallow copy and deep copy?
--> The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
--> A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
--> A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
"""

# **************** Important Shallow copy and deep copy is incomplete ****************

import copy

# Shallow copy example
old_list = [10, 20, 40, 30.5]
new_list = copy.copy(old_list)
print("old list: ", old_list)
print("new list: ", new_list)
old_list[1] = 100
print("old data after shallow copy: ", old_list)
print("Shallow copied data: ", new_list)

# Deep copy example
# list3 = [10, 20, 40, 30.5]
# list4 = copy.deepcopy(list3)
# print(list4)
# print(id(list3))
# print(id(list4))

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)
