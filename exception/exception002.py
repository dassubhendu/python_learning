try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result is: ", result)
except TypeError as err:
    print("Please provide only digits: ", err)
except ZeroDivisionError as err:
    print("Please provide number greater than 0: ", err)
except ValueError as err:
    print("Please provide valid value: ", err)
except Exception as err:
    print("Something went wrong: ", err)
else:
    print("This else block will execute only if there is no exception")
finally:
    print("This finally block will always execute")