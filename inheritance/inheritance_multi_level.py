"""
--> Method overriding
"""
class ClassA:
    def methodA(self):
        print("I am coming from class A")

    def hello_world(self):
        print("Hello World from class A")

class ClassB(ClassA):
    def methodB(self):
        print("I am coming from class B")

    def hello_world(self):
        print("Hello World from class B")


class ClassC(ClassB):
    def methodC(self):
        print("I am coming from class C")

    def hello_world(self):
        print("Hello World from class C")


obj1 = ClassC()
obj1.methodA()
obj1.methodB()
obj1.methodC()
obj1.hello_world()

