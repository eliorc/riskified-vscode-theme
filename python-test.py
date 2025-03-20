def hello():
    print("Hello, World!")


hello()

print("yes")

"""
LONG STRING
"""


class Person:
    def __init__(self, name: str, age):
        # What do you mean
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def say_bye(self):
        print(f"Bye, my name is {self.name} and I am {self.age} years old.")

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person = Person("John", 30)
person.say_hello()


print(2)
