class Person:

    # Method belongs to class
    def welcome(self):
        print("Welcome to Python")


# Function does not belong to any class
def hello_world():
    print("Hello World")


p = Person()
p.welcome()
hello_world()
print(hello_world)  # <function hello_world at 0x00000150281F8CC0>
print(p.welcome)    # <bound method Person.welcome of <__main__.Person object at 0x00000150281F8C50>>
