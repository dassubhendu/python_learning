"""
--> While going out of the with block, the file will be closed automatically.
--> This is the advantage of using context manager.
"""
with open("Demo.txt") as f:
    print("Checking the current state of the file: ", f.closed)
    data = f.read()
    print(data)

print("Checking the current state of the file: ", f.closed)

