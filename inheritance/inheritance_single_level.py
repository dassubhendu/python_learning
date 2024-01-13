"""
--> In python all class by default inherit from object class
"""
class Base:
    name = "Subhendu"
    def baseMethod(self):
        print("I am in base class")


class Child(Base):
    company = "Google"
    def childMethod(self):
        print("I am in child class")


c = Child()
c.childMethod()
c.baseMethod()
print(c.name)
print(c.company)
