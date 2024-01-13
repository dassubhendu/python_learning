"""
1. What is the difference between shallow copy and deep copy?
--> The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
--> A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
--> A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
"""

# **************** Important Shallow copy and deep copy is incomplete ****************

import copy

# Shallow copy example
old_shallow_list = [[5, 8, 2], [40, 32, 45], [10, 20, 40]]
new_shallow_list = copy.copy(old_shallow_list)
print("old shallow list: ", old_shallow_list)
print("new shallow list: ", new_shallow_list)
old_shallow_list[1][1] = 100
print("old data after shallow copy: ", old_shallow_list)
print("Shallow copied data: ", new_shallow_list)

print("\n")

# Deep copy example
old_deep_list = [[5, 8, 2], [40, 32, 45], [10, 20, 40]]
new_deep_list = copy.deepcopy(old_deep_list)
print("old deep list: ", old_deep_list)
print("new deep list: ", new_deep_list)
old_deep_list[1][1] = 100
print("old data after deep copy: ", old_deep_list)
print("Deep copied data: ", new_deep_list)

