# If file is not found then it will throw an error.
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\testing\\RND\\Python\\python_learning\\exception\\files\\test.txt'
# To handle this error we can use try except block.

try:
    content = open("C:\\testing\\RND\\Python\\python_learning\\exception\\files\\test1.txt", "r")
    print(content.read())
# except:
#     print("File not found in my physical machine")
except FileNotFoundError as err:
    print("Something went wrong", err)
