list1 = [10, 40, 30, 20, 50, 4, 2, 8, 5]
print(list1)
list1.sort()
print('Printing the list after sorting: ', list1)
list1.sort(reverse=True)
print('Printing the list after sorting with reverse true: ', list1)
list1.reverse()
print('Printing the list after reversing: ', list1)

# List inside another list
myList = [10, 30, 20, [40, 60, 50, "Hello", "world"]]
print(myList)
print(myList[3][3])
print(myList[3][-1])
print(myList[3][3][0])
