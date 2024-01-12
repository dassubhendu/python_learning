class Person:

    def welcome(self):
        print("Welcome to Python")

    def hello_world(self):
        print("Hello World")

    def sum(self, num1, num2):
        print(num1 + num2)


p1 = Person()
p1.name = "John"
p1.phone = "1234567890"
p1.country = "India"
p1.city = "Bangalore"

q1 = Person()
q1.name = "David"
q1.phone = "0987654321"
q1.country = "USA"
q1.city = "New York"

print(p1.name)
print(q1.phone)
