class classA:
    def methodA(self):
        print("This is methodA of classA")

    def hello_world(self):
        print("Hello World from classA")


class classB:
    def methodB(self):
        print("This is methodB of classB")

    def hello_world(self):
        print("Hello World from classB")


# classC inherits from classA and classB
# Multiple inheritance follows method resolution order (MRO)
# MRO is the order in which Python looks for a method in a hierarchy of classes
# Method with same name in classA and classB, classA method will be called
class classC(classA, classB):
    def methodC(self):
        print("This is methodC of classC")


c = classC()
c.hello_world()
print(classC.mro())
# [<class '__main__.classC'>, <class '__main__.classA'>, <class '__main__.classB'>, <class 'object'>]
