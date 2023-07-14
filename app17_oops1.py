# Classes and Objects in Python.

class MyClass :
    x = 5
    y = 12

p1 = MyClass()  # P1 is an object of the class MyClass.
print(p1.x)

class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

p2 = Person('John', 21)
print(p2.name, p2.age)

class Boy :
    pass

# You can initialise a class with pass if you dont know what attributes you need.