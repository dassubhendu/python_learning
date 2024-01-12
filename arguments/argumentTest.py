def printValue(*args):
    print(args)
    print(type(args))
    print(args[1])
    # Using for loop to access all args values
    for i in args:
        print(i)


# *args receives values as a tuple
# This is not mandatory to write *args, you can write anything instead of args like *test
printValue(1, 2, 3, 4, 5)
printValue("python", "java", "c++", "c#", "javascript", "php", "ruby", "go", 2700)


# Using *args in function call
def get_sum_of_all_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
    return sum


get_sum_of_all_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def get_min_value(*args):
    min = args[0]
    for i in args:
        if i < min:
            min = i
    print(min)
    return min


get_min_value(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def get_max_value(*args):
    max = args[0]
    for i in args:
        if i > max:
            max = i
    print(max)
    return max


get_max_value(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
