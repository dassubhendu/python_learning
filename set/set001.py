"""
--> Set is a collection of unordered and un-indexed elements.
--> Set is written in curly brackets.
--> Set is mutable.
--> Set does not allow duplicate elements.
--> Set is unordered, so we cannot access elements using index.
-->
"""

mySet = {35, 23, 54.3, 98, 10, 'python', 'java', True, 23, 10}
print(mySet)
# How to add element in set
mySet.add(100)
print(mySet)
# How to remove element from set
mySet.pop()
print(mySet)
# How to remove specific element from set
mySet.remove(98)
print(mySet)
# While removing element from set, if element is not present in set then it will throw error
# But if we use discard() method then it will not throw error
mySet.discard(23)
print(mySet)
# How to get length of set
print(len(mySet))
