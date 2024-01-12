class Person:

    def __init__(self, f, l):
        self.fname = f
        self.lname = l
        print("Hello " + self.fname + " " + self.lname)

    def sum(self, x, y):
        self.v1 = x
        self.v2 = y
        return self.v1 + self.v2


x = Person("Subhendu", "Das")
print(x.sum(10, 20))
