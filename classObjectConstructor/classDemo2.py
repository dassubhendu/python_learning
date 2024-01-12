class Person:

    def welcome(self):
        print("Welcome to Python")

    def hello_world(self):
        print("Hello World")

    def sum(self, num1, num2):
        print(num1 + num2)


p1 = Person()
# We can call the method using the object reference in two ways
p1.welcome()
Person.welcome(p1)
# While we are calling the method using the object reference, the object reference is passed as the first argument to the method.
# Self is the instance of the class. It is the first argument to the method.
p1.sum(10, 20)
