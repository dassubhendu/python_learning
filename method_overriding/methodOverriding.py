"""
--> While overriding a method in a child class, we can call the parent class method using super() method.
"""


class BaseClass:
    def hello_world(self):
        print("Hello World from Parent Class")


class ChildClass(BaseClass):
    def hello_world(self):
        print("Hello World from Child Class")
        super().hello_world()


child = ChildClass()
child.hello_world()