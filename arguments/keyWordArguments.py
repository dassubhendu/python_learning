def printNames(**kwargs):
    print(kwargs)
    print(kwargs["city"])
    for key, value in kwargs.items():
        print(key, value)


# **kwargs receives values as a dictionary
printNames(name='John', age=25, city='London')


# We can pass *args and **kwargs together in a function
def printValues(*args, **kwargs):
    print(args)
    print(kwargs)
    # for i in args:
    #     print(i)
    # for key, value in kwargs.items():
    #     print(key, value)


printValues(1, 2, 3, 4, 5, name='John', age=25, city='London')

print("***********************************************")


# Tricky example
def printValues2(fname, *args, **kwargs):
    print(fname)
    print(args)
    print(kwargs)
    # for i in args:
    #     print(i)
    # for key, value in kwargs.items():
    #     print(key, value)


# If nothing has been passed for name parameter, then it will take the first value for name
printValues2(1, 2, 3, 4, 5, age=25, city='London')
