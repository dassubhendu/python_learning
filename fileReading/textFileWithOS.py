import os

# file_path = os.getcwd()
# print(file_path)
# print(os.path.dirname(file_path))

with open(os.path.dirname(os.getcwd()) + "\\testFiles\\demo1.txt") as f:
    print("Checking the current state of the file: ", f.closed)
    data = f.read()
    print(data)
