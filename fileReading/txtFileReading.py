"""
--> While opening file and not mentioning the mode, it will open the file in read mode by default.
--> If the file is not present, it will throw an error.
--> Context manager is used to open the file.
--> Context manager will close the file automatically.
"""
try:
    f = open("Demo.txt")
    data = f.read()
    print(data)
    print('The file mode: ', f.mode)
    print('The file name: ', f.name)
except Exception as err:
    print('File not found', err)
finally:
    f.close()
