num1 = int(input("Enter the first number: "))
if num1 == 0:
    raise AssertionError("Number cannot be zero")
print("You entered: ", num1)