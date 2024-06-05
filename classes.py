import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._born = datetime.datetime.now().year - age

    def print_name(self):
        print(self.name)

me = Person("Marcello", 37)
me.print_name()
print("value in class: ", me.name)
print("value in class: ", me._born)