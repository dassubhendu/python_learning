with open('writeTest.txt', 'w') as f:
    f.write('Hello, world!\n')

"""
--> If no file exists, it will be created.
"""
with open('writeTest1.txt', 'w') as f:
    f.write('Hello, Subhendu!\n')

"""
--> If you want to append to an existing file, pass 'a' as the second argument to open().
--> The append mode also creates the file if it doesn't exist.
"""
with open('writeTest1.txt', 'a') as f:
    f.write('Hello this is Saurav \t')
    f.write('Hello this is Sachin \t')
    f.write('Hello, This is me!\n')